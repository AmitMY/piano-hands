# Piano Hands

This dataset contains object tagging of right and left hands on a piano background.

Its purpose is to detect hands from videos of piano playing.

## Using the dataset
The directory [versions](versions) includes all of the available versions for this dataset.
They can also be found under the `releases` tab on GitHub.

## Object Detection Model
We fine-tuned a "Faster RCNN Inception v2 COCO" model from the tensorflow official repository.
Note our model does not include any tracking. Every video frame is processed independently.

#### Easy Video - [Alan Walker - Faded](https://www.youtube.com/watch?v=LSwXh1Y5thY)
![Detection Results](https://drive.google.com/uc?id=1WtXa9Z8VCgOx5VZpRuwTGy2QRjb5oKKQ)

#### Harder Video - [Liszt - La Campanella](https://www.youtube.com/watch?v=H1Dvg2MxQn8)
![Detection Results](https://drive.google.com/uc?id=1bMsWLAWXi776aowMWmEDrgci3Ndd4bjw)


We include the training script, checkpoint, and a simple python file for example of use. 
**PRO TIP:** If you train a model, make sure there is no "horizontal flip" augmentation.
If you know there are a maximum of 2 hands in a frame, you can heuristically fix mistakes of tagging both hands as left or right.

## Manually tagging the dataset
- From `videos` execute `download.sh` which downloads 200+ youtube videos.
- From `videos` execute `extract_frames.py` which creates a top level `frames` directory with random frames from the videos.
- Using [labelImg](https://github.com/tzutalin/labelImg) tag the directory `frames` to `annotations`.
- From `versions` execute `generate_version.py`, after changing the version number.


