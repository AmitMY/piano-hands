#!/usr/bin/env bash

#
#
# Warning This was migrated from a different project, therefore, the directory structure might not be correct.
#
#

cd libs

# Setup Object Detection
mkdir object_detection
cd object_detection
git clone https://github.com/tensorflow/models.git
cd models/
MAIN_DIR=$(pwd)
export PYTHONPATH="${PYTHONPATH}:$MAIN_DIR:$MAIN_DIR/research:$MAIN_DIR/research/slim"

cd research
setup.py build
setup.py install
cd object_detection/
wget http://download.tensorflow.org/models/object_detection/faster_rcnn_inception_v2_coco_2018_01_28.tar.gz
tar xvzf faster_rcnn_inception_v2_coco_2018_01_28.tar.gz
wget http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_coco_2018_01_28.tar.gz
tar xvzf ssd_mobilenet_v1_coco_2018_01_28.tar.gz


git clone https://github.com/EdjeElectronics/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10.git detection
cd detection
rm -r training/*
rm -r inference_graph/*
rm -r images/*
mkdir images/train
mkdir image/test
cp -r . ../
cd ..
rm -r detection

protoc --python_out=. ./object_detection/protos/anchor_generator.proto ./object_detection/protos/argmax_matcher.proto ./object_detection/protos/bipartite_matcher.proto ./object_detection/protos/box_coder.proto ./object_detection/protos/box_predictor.proto ./object_detection/protos/eval.proto ./object_detection/protos/faster_rcnn.proto ./object_detection/protos/faster_rcnn_box_coder.proto ./object_detection/protos/grid_anchor_generator.proto ./object_detection/protos/hyperparams.proto ./object_detection/protos/image_resizer.proto ./object_detection/protos/input_reader.proto ./object_detection/protos/losses.proto ./object_detection/protos/matcher.proto ./object_detection/protos/mean_stddev_box_coder.proto ./object_detection/protos/model.proto ./object_detection/protos/optimizer.proto ./object_detection/protos/pipeline.proto ./object_detection/protos/post_processing.proto ./object_detection/protos/preprocessor.proto ./object_detection/protos/region_similarity_calculator.proto ./object_detection/protos/square_box_coder.proto ./object_detection/protos/ssd.proto ./object_detection/protos/ssd_anchor_generator.proto ./object_detection/protos/string_int_label_map.proto ./object_detection/protos/train.proto ./object_detection/protos/keypoint_box_coder.proto ./object_detection/protos/multiscale_anchor_generator.proto ./object_detection/protos/graph_rewriter.proto ./object_detection/protos/calibration.proto ./object_detection/protos/flexible_grid_anchor_generator.proto
cd object_detection
cp -r ../../../../../components/hand_dataset/frames/* images/train/
cp -r ../../../../../components/hand_dataset/annotations/* images/train/
mv images/train/A* images/test/

cp ../../../../../components/hand_dataset/configuration/Object_detection_video.py Object_detection_video.py
cp ../../../../../components/hand_dataset/configuration/generate_tfrecords.py generate_tfrecords.py
cp ../../../../../components/hand_dataset/configuration/labelmap.pbtxt training/labelmap.pbtxt
cp ../../../../../components/hand_dataset/configuration/faster_rcnn_inception_v2.config training/faster_rcnn_inception_v2.config
cp ../../../../../components/hand_dataset/configuration/ssd_mobilenet_v1_coco.config training/ssd_mobilenet_v1_coco.config

python xml_to_csv.py
python generate_tfrecords.py --csv_input=images/train_labels.csv --image_dir=images/train --output_path=train.record
python generate_tfrecords.py --csv_input=images/test_labels.csv --image_dir=images/test --output_path=test.record

pip install pycocotools
mkdir out/
python model_main.py --logtostderr --train_dir=training/ --pipeline_config_path=training/faster_rcnn_inception_v2.config --model_dir=out/

python export_inference_graph.py --input_type image_tensor --pipeline_config_path training/faster_rcnn_inception_v2.config --trained_checkpoint_prefix out/model.ckpt-189599 --output_directory inference_graph
python Object_detection_video.py