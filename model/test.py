import unittest
import numpy as np
from PIL import Image

from detector import get_detector, THRESHOLD


class TestDetector(unittest.TestCase):
    def test_detector(self):
        frame = np.uint8(Image.open("assets/piano.jpg"))
        frame_expanded = np.expand_dims(frame, axis=0)

        sess, image_tensor, other_tensors = get_detector()

        ([boxes], [scores], [classes], [num]) = sess.run(other_tensors, feed_dict={image_tensor: frame_expanded})

        relevant = [boxes[i] for i, score in enumerate(scores) if score > THRESHOLD]

        self.assertEqual(len(relevant), 2)
        self.assertEqual(tuple(relevant[0]), (0.5095517, 0.37182114, 0.7621389, 0.50664663))
        self.assertEqual(tuple(relevant[1]), (0.5725339, 0.57973766, 0.8249363, 0.7019011))

        self.assertEqual(classes[0], 1)
        self.assertEqual(classes[1], 2)


if __name__ == '__main__':
    unittest.main()
