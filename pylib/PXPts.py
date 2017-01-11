import os
import numpy as np

def Pts2Lmk(fname):
    n_lmk = 68
    lmk = np.genfromtxt(fname, delimiter=' ', skip_header=3, skip_footer=1)
    return lmk

def Lmk68to7(lmk):
    lmk2 = np.zeros( (7,2) )
    lmk2[0] = lmk[37-1]
    lmk2[1] = lmk[40-1]
    lmk2[2] = lmk[43-1]
    lmk2[3] = lmk[46-1]
    lmk2[4] = lmk[31-1]
    lmk2[5] = lmk[49-1]
    lmk2[6] = lmk[55-1]
    return lmk2

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

def ReadLmkFromTxt(path,format):
    ct = 0
    list = []
    for root, dirs, files in os.walk(path):
        for file in sorted(files):
            if file.endswith(format):
                lmk = np.loadtxt(root+file) # 68x2
                n,d = lmk.shape
                lmk = lmk.reshape((n*d))
                list.append(lmk)
                ct = ct + 1
                if ct == 10000:
                    return list
    return list

def ReadLmkFromTxtRecursive(path,format):
    ct = 0
    list = []
    for root, dirs, files in os.walk(path):
        for fold in dirs:
            files = os.listdir(root+fold)
            for file in sorted(files):
                if file.endswith(format):
                    lmk = np.loadtxt(root+fold+'/'+file) # 68x2
                    n,d = lmk.shape
                    lmk = lmk.reshape((n*d))
                    list.append(lmk)
                    ct = ct + 1
                    if ct == 10000:
                        return list
    return list


if __name__=='__main__':
    print 'Python pts to landmark by Xi Peng'

