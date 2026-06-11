import torch
import torch.nn as nn 
import torch.nn.functional as F 
import numpy as np 
import pandas as pd 

# sklearn preprocessing


# ENCODER
class Encoder(nn.Module):
    def __init__(self, input_dim, hidden_dim=128, dropout=0.1):
        super().__init()
        self.net = nn.Sequential(
            nn.Linear(input_dim, 512),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(512, hidden_dim),
            nn.ReLU()
        )
    def forward(self, x):
        return self.net(x)


# PROJECTION HEADS
class ProjectionHead(nn.Module):
    def __init__(self, input_dim, output_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, output_dim),
            nn.ReLU()
        )
    def forward(self, x):
        return self.net(x)