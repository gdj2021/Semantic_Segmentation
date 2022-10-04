# # # #fake label data
# # # import numpy as np
# # # import torch
# # #
# # # import torch.nn.functional as F
# # # gt=np.random.rand(1,2,3)
# # # print(gt)
# # # print('========================================')
# # # gt=gt.astype(np.int64)
# # # print(gt)
# # # print('==========================================')
# # # gt=torch.from_numpy(gt)
# # # print(gt)
# # # print('---------------------------------------------------------------------------')
# # # x=torch.rand(1,2,2,3)
# # # print(x)
# # # print('============================================')
# # # out=F.log_softmax(x,dim=1)
# # # print('out',out)
# # # for i in range(5):
# # #     i+=1
# # #     print('-------------')
# # #     if i==3:
# # #         continue
# # #     print(i)
# # # b1=[1,2,3]
# # # b2=[2,3,4]
# # # b3=[val for val in b1 if val in b2]
# # # print(b3)
# # list=[1,2,3,4,5,6]
# # list1=list[-1:1:-1]
# # print(list1)
# # def adder(x):
# #     def wrapper(y):
# #         return x+y
# #     return wrapper
# # adder5=adder(5)
# # print(adder5(adder5(6)))
# import os
# os.makedirs(os.path.join('..','data'),exist_ok=True)
# data_file = os.path.join('..','data','house_tiny.csv')
# with open(data_file,'w')as f:
#     f.write('NumRooms,Alley,price\n')
#     f.write('NA,PAVE,127500\n')
#     f.write('2,NA,106000\n')
#     f.write('4,NA,178100\n')
#     f.write('NA,NA,140000\n')
#     #f.close()
# import pandas as pd
# data = pd.read_csv(data_file)
# print(data)
# inputs,outputs = data.iloc[:,0:2],data.iloc[:,2]
# #print(inputs)
# #print(outputs)
# inputs = inputs.fillna(inputs.mean())
# print(inputs)
# inputs = pd.get_dummies(inputs,dummy_na=True)
# print(inputs)
# import torch
# x,y = torch.tensor(inputs.values),torch.tensor(outputs.values)
# print(x)
# print(y)
#
# import torch
# x = torch.arange(4.0)
#
# print(x)
# print(x.shape)
# x = x.requires_grad_(True)
# print(x.grad)