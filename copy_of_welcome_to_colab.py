# -*- coding: utf-8 -*-
"""Copy of Welcome To Colab

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WcZBG16EsIgpX1AWy8NH5dU5F__JwtpP
"""

import torch
import torch.nn as nn
import torch.nn.functional as F

from torch.optim import SGD
import matplotlib.pyplot as plt
import seaborn as sns

class Malaknn(nn.Module):
  def __init__(self):
    super().__init__()
    self.w00=nn.Parameter(torch.rand(1),requires_grad=True)
    self.w01=nn.Parameter(torch.rand(1),requires_grad=True)
    self.w02=nn.Parameter(torch.rand(1),requires_grad=True)
    self.w11=nn.Parameter(torch.rand(1),requires_grad=True)
    self.w12=nn.Parameter(torch.rand(1),requires_grad=True)
    self.w13=nn.Parameter(torch.rand(1),requires_grad=True)
    self.w20=nn.Parameter(torch.rand(1),requires_grad=True)
    self.b00=nn.Parameter(torch.rand(1),requires_grad=True)
    self.b01=nn.Parameter(torch.rand(1),requires_grad=True)
    self.b02=nn.Parameter(torch.rand(1),requires_grad=True)

  def forward(self,input):
     # hidden layer
      input_to_layer01=input*self.w00+self.b00
      layer_01_output=F.sigmoid(input_to_layer01)
      layer_01_output=layer_01_output*self.w11

      input_to_layer02=input*self.w01+self.b01
      layer_02_output=F.sigmoid(input_to_layer02)
      layer_02_output=layer_02_output*self.w12

      input_to_layer03=input*self.w02+self.b02
      layer_03_output=F.sigmoid(input_to_layer03)
      layer_03_output=layer_03_output*self.w13

      # output layer
      output=layer_01_output + layer_02_output + layer_03_output
      output=F.tanh(output)
      output=output*self.w20
      return output

my_model=Malaknn()
x=torch.linspace(start=1, end=2.5, steps=40)
x

y=my_model(x)
y

sns.set(style="whitegrid")

sns.lineplot(
    x=x.detach().numpy(),
    y=y.detach().numpy(),
    color='red',
    linewidth=3
)


plt.xlabel('X')
plt.ylabel('Y')

class nournn(nn.Module):
  def __init__(self):
    super().__init__()
    self.w00=nn.Parameter(torch.rand(1),requires_grad=True)
    self.w01=nn.Parameter(torch.rand(1),requires_grad=True)
    self.w02=nn.Parameter(torch.rand(1),requires_grad=True)
    self.w11=nn.Parameter(torch.rand(1),requires_grad=True)
    self.w12=nn.Parameter(torch.rand(1),requires_grad=True)
    self.w13=nn.Parameter(torch.rand(1),requires_grad=True)
    self.w20=nn.Parameter(torch.rand(1),requires_grad=True)
    self.b00=nn.Parameter(torch.rand(1),requires_grad=True)
    self.b01=nn.Parameter(torch.rand(1),requires_grad=True)
    self.b02=nn.Parameter(torch.rand(1),requires_grad=True)

  def forward(self,input):
     # hidden layer
      input_to_layer01=input*self.w00+self.b00
      layer_01_output=F.sigmoid(input_to_layer01)
      layer_01_output=layer_01_output*self.w11

      input_to_layer02=input*self.w01+self.b01
      layer_02_output=F.sigmoid(input_to_layer02)
      layer_02_output=layer_02_output*self.w12

      input_to_layer03=input*self.w02+self.b02
      layer_03_output=F.sigmoid(input_to_layer03)
      layer_03_output=layer_03_output*self.w13

      # output layer
      output=layer_01_output + layer_02_output + layer_03_output
      output=F.tanh(output)
      output=output*self.w20
      return output

nournn=nournn()
new_y=nournn(x)
new_y

sns.set(style="whitegrid")

sns.lineplot(
    x=x.detach().numpy(),
    y=new_y.detach().numpy(),
    color='red',
    linewidth=3
)


plt.xlabel('X')
plt.ylabel('Y')

optimizer=SGD(nournn.parameters(),lr=0.01)
loss_fn=nn.MSELoss()

for epoch in range(100):
    total_loss = 0  # Initialize total loss for tracking

    for i in range(len(x)):
        input_i = x[i]
        actual_output_i = y[i]

        # Get the model's prediction
        pred_output_i = nournn(input_i)

        # Compute the loss for the current example
        loss_value = loss_fn(pred_output_i, actual_output_i)

        # Backpropagate the loss for this single example
        loss_value.backward()

        # Accumulate the loss for tracking purposes
        total_loss += loss_value.item()  # Use .item() to convert tensor to scalar for tracking

        # Update the model parameters and reset gradients
        optimizer.step()
        optimizer.zero_grad()

    # Print the total loss for the entire epoch
    print('Epoch: ', epoch, ' | Total Loss: ', total_loss)


# there is some thing is wrong i can't fix it and tried with (gpt)
#  but also no thing is change so idk what should i do ,
# Therefore i can't complete the assig.