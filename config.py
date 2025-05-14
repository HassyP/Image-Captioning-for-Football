import torch

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
IMAGE_PATH = "zidane.jpg"
