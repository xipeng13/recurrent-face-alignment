import os, sys
import cv2
import numpy as np
from PIL import Image

def GetCenterDist_7lmks(lmk):
    eyec = np.mean(lmk[0:4,:], axis=0)
    mouc = np.mean(lmk[5:7,:], axis=0)
    eyec_mouc_dist = np.sqrt(np.sum((eyec-mouc)**2))
    cx = int((eyec[0]+mouc[0]) / 2)
    cy = int((eyec[1]+mouc[1]) / 2)
    return (cx, cy, eyec_mouc_dist)

def Lmk2Bbox_7lmks(lmk, DISTRATIO):
    cx,cy,dist = GetCenterDist_7lmks(lmk)
    sl = int(dist * DISTRATIO)
    bbox = (cx-sl/2, cy-sl/2, cx+sl/2, cy+sl/2) # left, top, right, bottom 
    return bbox

