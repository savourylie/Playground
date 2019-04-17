import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn.modules.utils import _single, _pair, _triple

class OctConv2d(nn.modules.conv._ConvNd):
    def __init__(self, in_channels, out_channels, kernel_size, stride=1, dilation=1, bias=True, oct_type='regular', alpha_in=0.5, alpha_out=0.5):
        if oct_type not in ('regular', 'first', 'last'):
            raise InvalidOctType("Invalid oct_type was chosen!")

        oct_type_dict = {'first': (0, alpha_out), 'last': (alpha_in, 0), 'regular': (alpha_in, alpha_out)}

        kernel_size = _pair(kernel_size)
        stride = _pair(stride)
        padding = _pair(int((kernel_size[0] - 1) / 2))
        dilation = _pair(dilation)
        super(OctConv2d, self).__init__(
            in_channels, out_channels, kernel_size, stride, padding, dilation,
            False, _pair(0), 1, bias)

        self.oct_type = oct_type
        self.alpha_in, self.alpha_out = oct_type_dict[self.oct_type]
        
        self.num_high_in_channels = int((1 - self.alpha_in) * in_channels)
        self.num_low_in_channels = int(self.alpha_in * in_channels)
        self.num_high_out_channels = int((1 - self.alpha_out) * out_channels)
        self.num_low_out_channels = int(self.alpha_out * out_channels)

        self.high_hh_weight = self.weight[:self.num_high_out_channels, :self.num_high_in_channels, :, :].clone()
        self.high_hh_bias = self.bias[:self.num_high_out_channels].clone()

        self.high_hl_weight = self.weight[self.num_high_out_channels:, :self.num_high_in_channels, :, :].clone()
        self.high_hl_bias = self.bias[self.num_high_out_channels:].clone()

        self.low_lh_weight = self.weight[:self.num_high_out_channels, self.num_high_in_channels:, :, :].clone()
        self.low_lh_bias = self.bias[:self.num_high_out_channels].clone()

        self.low_ll_weight = self.weight[self.num_high_out_channels:, self.num_high_in_channels:, :, :].clone()
        self.low_ll_bias = self.bias[self.num_high_out_channels:].clone()

        self.high_hh_weight.data, self.high_hl_weight.data, self.low_lh_weight.data, self.low_ll_weight.data = \
        self._apply_noise(self.high_hh_weight.data), self._apply_noise(self.high_hl_weight.data), \
        self._apply_noise(self.low_lh_weight.data), self._apply_noise(self.low_ll_weight.data)

        self.avgpool = nn.AvgPool2d(2)
 
    def forward(self, x):
        high_group, low_group = x[:, :self.num_high_in_channels, :, :], x[:, self.num_high_in_channels:, :, :]

        high_group_hh = F.conv2d(high_group, self.high_hh_weight, self.high_hh_bias, self.stride,
                        self.padding, self.dilation, self.groups)
        high_group_pooled = self.avgpool(high_group)
        high_group_hl = F.conv2d(high_group_pooled, self.high_hl_weight, self.high_hl_bias, self.stride,
                        self.padding, self.dilation, self.groups)
        
        low_group = F.interpolate(low_group, scale_factor=0.5)

        low_group_lh = F.conv2d(low_group, self.low_lh_weight, self.low_lh_bias, self.stride,
                        self.padding, self.dilation, self.groups)
        low_group_upsampled = F.interpolate(low_group_lh, scale_factor=2)

        low_group_ll = F.conv2d(low_group, self.low_ll_weight, self.low_ll_bias, self.stride,
                        self.padding, self.dilation, self.groups)
        

        # print(high_group_hh.shape, low_group_lh.shape)

        high_group_out = high_group_hh + low_group_upsampled
        low_group_out = high_group_hl + low_group_ll

        # output = torch.cat([high_group_out, low_group_out], dim=1)

        return high_group_out, low_group_out

    @staticmethod
    def _apply_noise(tensor, mu=0, sigma=0.0001):
        noise = torch.normal(mean=torch.ones_like(tensor) * mu, std=torch.ones_like(tensor) * sigma)

        return tensor + noise


class Error(Exception):
    """Base-class for all exceptions rased by this module."""


class InvalidOctType(Error):
    """There was a problem in the OctConv type."""
