from torch.utils.data import DataLoader,Dataset
from skimage import io,transform
import matplotlib.pyplot as plt
import os
import torch
from torchvision import transforms
import numpy as np
from scipy.io import loadmat
import pandas as pd
import pdb
from ..encoding import Encoder, NullEncoder

class Nettalk(Dataset):
    def __init__(
        self, 
        root_dir, 
        image_encoder = None,
        label_encoder = None,
        transform = None
    ):
        self.root_dir = root_dir
        # m = loadmat("nettalk_small.mat") 
        m = loadmat(self.root_dir)
        # pdb.set_trace()
        # train_x, train_y, train_y_num, 
        # test_x, test_y, test_y_num
        # word_phoneme, word_phoneme_num, word_x
        self.train_x = m["train_x"]  # (5033,189)
        self.train_y = m["train_y"]
        self.train_y_num = m['train_y_num']
        self.test_x = m["test_x"]
        self.test_y = m["test_y"]
        self.test_y_num = m['test_y_num']

        self.transform = transform
        if image_encoder is None:
            image_encoder = NullEncoder()
        if label_encoder is None:
            label_encoder = NullEncoder()
        self.image_encoder = image_encoder
        self.label_encoder = label_encoder
        # self.images = os.listdir(self.root_dir)

    def __len__(self):
        # pdb.set_trace()
        return len(self.train_x)
    
    def __getitem__(self,index):
        vector = torch.Tensor(self.train_x[index,:])
        label = torch.Tensor(self.train_y_num[index])
        output = {
                "image": vector,
                "label": label,
                "encoded_image": self.image_encoder(vector),
                "encoded_label": self.label_encoder(label),
            }
        if self.transform:
            output = self.transform(output)
        return output

if __name__=='__main__':
    data = Nettalk(None, None, "nettalk_small.mat",transform=None)
    dataloader = DataLoader(data,batch_size=1,shuffle=False)
    for i_batch,batch_data in enumerate(dataloader):
        print(i_batch)
        print(batch_data['image'].size())
        print(batch_data['label'])