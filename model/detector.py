from functools import lru_cache

import numpy as np
from Pillow import Image

import tensorflow as tf

PATH_TO_CKPT = 'checkpoint.pb'
PATH_TO_LABELS = 'components/hand_dataset/configuration/labelmap.pbtxt'

THRESHOLD = 0.9


@lru_cache()
def get_detector():
    # Load the Tensorflow model into memory.
    detection_graph = tf.Graph()
    with detection_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')

        sess = tf.Session(graph=detection_graph)

    # Define input and output tensors (i.e. data) for the object detection classifier

    # Input tensor is the image
    image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

    # Output tensors are the detection boxes, scores, and classes
    # Each box represents a part of the image where a particular object was detected
    detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

    # Each score represents level of confidence for each of the objects.
    # The score is shown on the result image, together with the class label.
    detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
    detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')

    # Number of objects detected
    num_detections = detection_graph.get_tensor_by_name('num_detections:0')

    return sess, image_tensor, [detection_boxes, detection_scores, detection_classes, num_detections]


if __name__ == "__main__":
    frame = np.uint8(Image.read("assets/image.png"))
    frame_expanded = np.expand_dims(frame, axis=0)
    sess, image_tensor, other_tensors = get_detector()

    ([boxes], [scores], [classes], [num]) = sess.run(other_tensors, feed_dict={image_tensor: frame_expanded})

    relevant = [boxes[i] for i, score in enumerate(scores) if score > THRESHOLD]

    for box in relevant:
        print("Box", box)
