import os,sys
import numpy as np
sys.path.append('/home/xpeng/Dropbox/Code/lib/pyliy/')
import PXIO

img_path = '/media/xpeng/Research/resource/face_align/300W2/afw/'
ann_path = '/media/xpeng/Research/resource/face_align/300W2/afw/'
img_list = PXIO.ListFileInFolder(img_path,'.jpg')
print img_list

