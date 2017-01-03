# Demo code to detect landmarks from static image
# "A Recurrent Encoder-Decoder Network for Sequential Face Alignment", ECCV, 2016
# Xi Peng, xipeng.cs@rutgers.edu
# V0.1

import os,sys
import numpy as np
from PIL import Image, ImageDraw
WORKPATH = os.path.dirname(os.path.abspath(__file__))
print WORKPATH
sys.path.append(WORKPATH+'/pylib/')
import PXIO, PXPts

# set caffe/python path
sys.path.append('path/to/caffe/python/')
import caffe

SL = 128
NLMK = 7

def DetectImage(img_path, bbox, save_path):
    ch, hei, wid = 11, SL, SL
    data = np.zeros((1,ch,hei,wid))
    pts2 = np.zeros((NLMK,2))
        
    zoom_ratio = float(bbox[2]-bbox[0]) / SL
    img = Image.open(img_path)
    img_crop = img.crop(bbox)
    img2 = img_crop.resize((SL, SL), Image.ANTIALIAS)
    img2 = np.asarray(img2)

    mean_shape = np.zeros((1,8,SL,SL))
    data[0,0:3,:,:] = np.transpose(img2, (2,0,1))
    for s in range(2):
        data[0,3:11,:,:] = mean_shape
        net.blobs['img_lmk'].data[...] = data
        net.forward()
        prob_map = net.blobs['prob'].data[...]
        prob_map = np.squeeze(prob_map[0,:,:,:])
        mean_shape = prob_map

    label_map = np.argmax(prob_map, axis=0)
    for l in range(NLMK):
        try:
            y,x = np.where(label_map == l+1)
            yc,xc = np.mean(y), np.mean(x)
            pts2[l,:] = [xc,yc]
        except:
            print l

    pts = pts2 * zoom_ratio
    pts = pts + np.tile( np.array([bbox[0],bbox[1]]), (NLMK,1) )

    draw = ImageDraw.Draw(img)
    for l in range(NLMK):
        draw.ellipse((pts[l,0]-3,pts[l,1]-3,pts[l,0]+3,pts[l,1]+3), fill='white')
    img.save(save_path)
    del draw

if __name__ == '__main__':
    # detect landmarks from static image
    folder = 'AFW/'

    # working path
    model_path = WORKPATH + '/model/'
    data_path = WORKPATH + '/data/'
    result_path = WORKPATH + '/result/'
    PXIO.DeleteThenCreateFolder(result_path + folder)

    # load caffe model
    caffe.set_mode_gpu()
    caffe.set_device(1)
    net = caffe.Net(model_path+'deploy.prototxt', model_path+'/deploy_weights.caffemodel', caffe.TEST)

    # load image and bbox list, bbox = [left,top,right,bottom]
    img_bbox = PXIO.ReadLineFromFile(data_path + folder + 'img_bbox.txt')
    for line in img_bbox:
        token = line.split(' ')
        img_path = token[0]
        img_name = img_path.split('/')[-1]
        print img_name
        bbox = map(int, token[1:])
        save_path = result_path + folder + img_name[:-4] + '.png'

        # detect landmarks
        try:
            DetectImage(img_path,bbox,save_path)
        except:
            print img_name + ': detect abnormal!'

