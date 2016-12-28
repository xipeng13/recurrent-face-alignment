# A Recurrent Encoder-Decoder Network for Sequential Face Alignment
This is a quick demo for:

"A Recurrent Encoder-Decoder Network for Sequential Face Alignment"

Peng, Xi and Feris, Rogerio S.and Wang, Xiaoyu and Metaxas, Dimitris N.

European Conference on Computer Vision (ECCV), Amsterdam, 2016.

# How to Run
1. Code: Clone the project to "root/"

2. Mode: Download pre-trained caffe model from http: . Unzip model.zip and copy "model/" to "root/"

3. Video: Edit "root/TrackDemo.py" to set "caffe/python/path" and "video/path"

4. Track: "python TrackDemo.py"

5. Result: Check tracking results in "root/result/"

# Tracking protocol
For research convenience, we split testing video into frames using ffmpeg.

The user need to provide the bbox of the face at the first frame to initial the tracker. Please check "TrackDemo.py" for more details.

# Reference
Bibtex

@InProceedings{PengECCV16,

author = "Peng, Xi and Feris, Rogerio S.and Wang, Xiaoyu and Metaxas, Dimitris N.",

title = "A Recurrent Encoder-Decoder Network for Sequential Face Alignment",

booktitle = "14th European Conference on Computer Vision (ECCV)",

year = "2016",

pages="38--56"
}
