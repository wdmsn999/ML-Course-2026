import torch 
# 定义矩阵 A 和 B（浮点型，PyTorch推荐）
A = torch.tensor([[1.0, 2.0], [3.0, 4.0]]) 
B = torch.tensor([[5.0, 6.0], [7.0, 8.0]]) 
# 计算矩阵乘法（PyTorch专用矩阵乘法函数）
C = torch.matmul(A, B) 
# 打印结果
print("矩阵 A:\n", A) 
print("矩阵 B:\n", B) 
print("运算结果 C = A * B:\n", C)