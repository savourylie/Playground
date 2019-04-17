import numpy as np
import torch


def iou(outputs: torch.Tensor, labels: torch.Tensor, smooth=1e-6, thresh=0.5):
    # You can comment out this line if you are passing tensors of equal shape
    # But if you are passing output from UNet or something it will most probably
    # be with the BATCH x 1 x H x W shape
    outputs[outputs >= thresh] = 1
    outputs[outputs < thresh] = 0

    outputs = outputs.squeeze(1)  # BATCH x 1 x H x W => BATCH x H x W
    outputs, labels = outputs.int(), labels.int()

    intersection = (outputs & labels).float().sum((1, 2))  # Will be zero if Truth=0 or Prediction=0
    union = (outputs | labels).float().sum((1, 2))  # Will be zzero if both are 0

    iou = (intersection + smooth) / (union + smooth)  # We smooth our devision to avoid 0/0

    # thresholded = torch.clamp(20 * (iou - 0.5), 0, 10).ceil() / 10  # This is equal to comparing with thresolds
    # return thresholded.mean().item()  # Or thresholded.mean() if you are interested in average across the batch
    print(iou)

    return iou.mean().item()

if __name__ == '__main__':
    output, target = np.zeros((3, 10, 10)), np.ones((3, 10, 10))
    output[0, 3:6, 3:6] = 1
    output[1, 0, 0] = 1
    output[2, 0:2, 0:2] = 1

    output_torch = torch.tensor(output)
    target_torch = torch.tensor(target)

    print(iou(output_torch, target_torch))
