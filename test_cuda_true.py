import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("使用设备:", device)

a = torch.rand(3,3).to(device)
b = torch.rand(3,3).to(device)

c = a @ b
print("计算结果:")
print(c)
print(torch.cuda.get_device_name(0))