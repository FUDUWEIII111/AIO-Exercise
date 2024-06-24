import torch
import torch.nn as nn


class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self,  list):
        x_exp = torch.exp(list)
        # keepdim=True: keep the dimensions of the original tensor
        total = torch.sum(x_exp, 0, keepdim=True)
        return x_exp / total


class StableSoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self,  list):
        c = torch.max(list, dim=0)
        x_exp = torch.exp(list - c.values)
        total = torch.sum(x_exp, 0, keepdim=True)
        return x_exp / total


def main():
    data = torch.Tensor([1, 2, 3])
    my_softmax = MySoftmax()
    output = my_softmax(data)
    data2 = torch.Tensor([1, 2, 3])
    my_stable_softmax = StableSoftmax()
    output2 = my_stable_softmax(data2)
    print(output)
    print(output2)


if __name__ == "__main__":
    main()
