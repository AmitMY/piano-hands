# Piano Hands

This dataset contains object tagging of right and left hands on a piano background.

Its purpose is to detect hands from videos of piano playing.

## Using the dataset
The directory [versions](versions) includes all of the available versions for this dataset.
They can also be found under the `releases` tab on GitHub.

## Object Detection Model
We fine-tuned a "Faster RCNN Inception v2 COCO" model from the tensorflow official repository.

#### Easy Video
![Detection Results](model/assets/video.gif)

#### Harder Video
![Detection Results](model/assets/harder.gif)


We include the training script, checkpoint, and a simple python file for example of use. 

## Manually tagging the dataset
- From `videos` execute `download.sh` which downloads 200+ youtube videos.
- From `videos` execute `extract_frames.py` which creates a top level `frames` directory with random frames from the videos.
- Using [labelImg](https://github.com/tzutalin/labelImg) tag the directory `frames` to `annotations`.
- From `versions` execute `generate_version.py`, after changing the version number.


