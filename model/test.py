import torch
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader

a = torch.FloatTensor([[1, 2, 3], [4, 5, 6]])
print(a.shape)
print(a)
data = a[..., :1]
print('data', data.shape)
print(data)