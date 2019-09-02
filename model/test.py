import unittest
import numpy as np
from PIL import Image

from detector import get_detector, THRESHOLD


class TestDetector(unittest.TestCase):
    def test_detector(self):
        frame = np.uint8(Image.open("assets/image.png"))
        frame_expanded = np.expand_dims(frame, axis=0)

        sess, image_tensor, other_tensors = get_detector()

        ([boxes], [scores], [classes], [num]) = sess.run(other_tensors, feed_dict={image_tensor: frame_expanded})

        relevant = [boxes[i] for i, score in enumerate(scores) if score > THRESHOLD]

        for box in relevant:
            print("Box", box)

        self.assertEqual(classes[0], 1)
        self.assertEqual(classes[1], 2)


if __name__ == '__main__':
    unittest.main()
