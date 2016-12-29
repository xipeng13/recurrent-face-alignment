# A Recurrent Encoder-Decoder Network for Sequential Face Alignment
This is a quick demo for:

"A Recurrent Encoder-Decoder Network for Sequential Face Alignment"

Xi Peng, Rogerio S. Feris, Xiaoyu Wang, Dimitris N. Metaxas

European Conference on Computer Vision (ECCV), Amsterdam, 2016.

# How to Run
1. Code: Clone/Download the project to "recurrent-face-alignment/"

2. Mode: Download pre-trained caffe model from https://drive.google.com/open?id=0B-FLp_bljv_1eGdyM3JkTmRFQ28. Copy "model/" to "recurrent-face-alignment/"

3. Video: Download demo videos from https://drive.google.com/open?id=0B-FLp_bljv_1ampOZXFBRE5MWEk. Copy "data/" to "recurrent-face-alignment/"

3. Modify: Edit "TrackDemo.py" to set (a) "path/to/caffe/python/", and (b) "video names to be tracked" 

4. Track: "python TrackDemo.py"

5. Result: Check tracking results in "root/result/"

# Tracking protocol
For research convenience, we split testing video into frames using ffmpeg.

The tracker need the bbox of the face at the first frame for initialization. 

Dependency: caffe (support batch normalization layer); python 2.7.

# Reference
Bibtex

@InProceedings{PengECCV16,

author = "Peng, Xi and Feris, Rogerio S.and Wang, Xiaoyu and Metaxas, Dimitris N.",

title = "A Recurrent Encoder-Decoder Network for Sequential Face Alignment",

booktitle = "14th European Conference on Computer Vision (ECCV)",

year = "2016",

pages="38--56"
}
