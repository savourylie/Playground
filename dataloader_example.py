from scipy import misc
import torch
from torch.utils.data import Dataset, DataLoader

class SomeImageDataset(Dataset):
    """The training table dataset.
    """
    def __init__(self):
        self.x_data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.y_data = [0, 1, 0, 1, 0, 1, 0, 1]

        self.len = len(self.x_data) # Size of data
        
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]
        
    def __len__(self):
        return self.len


def main():
    dataset = SomeImageDataset()
    train_loader = DataLoader(dataset=dataset,
                             batch_size=2,
                             shuffle=True,
                             num_workers=1
    )

    for epoch in range(2):
        for data in train_loader:
            x_data, y_data = data
        
            print(x_data)

def test_gen():
    x_list = range(10)

    for x in x_list:
        yield x

if __name__ == '__main__':
    # main()

    gen = test_gen()

    for epoch in range(2):
        for x in gen:
            print(x)
