# A Recurrent Encoder-Decoder Network for Sequential Face Alignment
This is a quick demo for:

"A Recurrent Encoder-Decoder Network for Sequential Face Alignment"

Xi Peng, Rogerio S. Feris, Xiaoyu Wang, Dimitris N. Metaxas

European Conference on Computer Vision (ECCV), Amsterdam, 2016.

# How to Run
1. Clone/Download the project to ```recurrent-face-alignment/```

2. Download folders ```model/``` and ```data/``` from https://drive.google.com/open?id=0B-FLp_bljv_1dzZGdUZIamstVkE

3. Copy folders ```model/``` and ```data/``` into ```recurrent-face-alignment/```

4. Edit ```TrackDemo.py``` to set (a) ```path/to/caffe/python/```, and (b) ```video names to be tracked``` 

5. ```python TrackDemo.py```

6. Check tracking results in ```recurrent-face-alignment/result/```

# Tracking protocol
For research convenience, we split video into frames using ffmpeg.

The tracker need the bbox of the face at the first frame for initialization. 

Dependency: caffe (support batch normalization layer); python 2.7.

# Reference
```
@InProceedings{PengECCV16,
author = "Peng, Xi and Feris, Rogerio S.and Wang, Xiaoyu and Metaxas, Dimitris N.",
title = "A Recurrent Encoder-Decoder Network for Sequential Face Alignment",
booktitle = "European Conference on Computer Vision (ECCV)",
year = "2016",
pages="38--56"}
```
