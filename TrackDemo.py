# Demo code for "A Recurrent Encoder-Decoder Network for Sequential Face Alignment", ECCV, 2016
# Xi Peng, xipeng.cs@rutgers.edu
# V0.1

import os,sys
import numpy as np
from PIL import Image, ImageDraw
WORKPATH = os.path.dirname(os.path.abspath(__file__))
print WORKPATH
sys.path.append(WORKPATH+'/pylib/')
import PXIO, PXPts, PXTrack

# set caffe/python path
sys.path.append('path/to/caffe/python/')
import caffe

SL = 128
NLMK = 7

def TrackFrame(frame_list, initial_bbox, mean_shape, save_path):
    ch, hei, wid = 11, SL, SL
    data = np.zeros((1,ch,hei,wid))
    pts2 = np.zeros((NLMK,2))
    cnt = 1
    for img_path in frame_list:
        token = img_path.split('/')
        fold, img_name = token[-3], token[-1]
        print fold+' '+img_name

        if cnt == 1:
            bbox = initial_bbox
        else:
            bbox = PXTrack.Lmk2Bbox_7lmks(pts, 3)

        zoom_ratio = float(bbox[2]-bbox[0]) / SL
        img = Image.open(img_path)
        img_crop = img.crop(bbox)
        img2 = img_crop.resize((SL, SL), Image.ANTIALIAS)
        img2 = np.asarray(img2)

        data[0,0:3,:,:] = np.transpose(img2, (2,0,1))
        data[0,3:11,:,:] = mean_shape
        net.blobs['img_lmk'].data[...] = data
        net.forward()
        prob_map = net.blobs['prob_s2'].data[...]
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
        save_name = save_path + img_name[:-4] + '.png'
        img.save(save_name)
        del draw

        cnt = cnt + 1

if __name__ == '__main__':
    # select video
    # 300VW_001/, 300VW_540/, 300VW_557/, ASL/, YTC/
    video = '300VW_001/'

    # working path
    model_path = WORKPATH + '/model/'
    data_path = WORKPATH + '/data/'
    result_path = WORKPATH + '/result/'

    # load caffe model
    caffe.set_mode_gpu()
    caffe.set_device(1)
    net = caffe.Net(model_path+'deploy.prototxt', model_path+'/deploy_weights.caffemodel', caffe.TEST)

    # generate frame list
    if video =='YTC/':
        frame_list = PXIO.ListFileInFolder(data_path+video+'/img/','.png')
    else:
        frame_list = PXIO.ListFileInFolder(data_path+video+'/img/','.jpg')

    # provide initial bbox
    # set bbox = [left, top, right, bottom]
    # or use the landmark annotation of the 1st frame to generate bbox
    if video == 'ASL/' or video == 'YTC/':
        initial_bbox = np.loadtxt(data_path+video+'bbox.txt').astype(int)
    else:
        first_frame = frame_list[0].split('/')[-1]
        pts = PXPts.Pts2Lmk(data_path+video+'/annot/'+first_frame[:-4]+'.pts')
        pts = PXPts.Lmk68to7(pts)
        initial_bbox = PXTrack.Lmk2Bbox_7lmks(pts, 3)

    # mean shape
    mean_shape = np.zeros((1,8,SL,SL))

    # save tracking result
    save_path = result_path + video
    PXIO.DeleteThenCreateFolder(save_path)

    # track frames
    try:
        TrackFrame(frame_list, initial_bbox, mean_shape, save_path)
    except:
        print video + ": tracker abnormal!"




