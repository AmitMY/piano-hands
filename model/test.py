import unittest
import numpy as np
from PIL import Image

from detector import get_detector, THRESHOLD


class TestDetector(unittest.TestCase):
    def __init__(self):
        super().__init__()
        frame = np.uint8(Image.read("assets/image.png"))
        self.frame_expanded = np.expand_dims(frame, axis=0)

    def test_detector(self):
        sess, image_tensor, other_tensors = get_detector()

        ([boxes], [scores], [classes], [num]) = sess.run(other_tensors, feed_dict={image_tensor: self.frame_expanded})

        relevant = [boxes[i] for i, score in enumerate(scores) if score > THRESHOLD]

        for box in relevant:
            print("Box", box)


if __name__ == '__main__':
    unittest.main()
