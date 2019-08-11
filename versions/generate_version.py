import json
from os import mkdir, path, listdir
from shutil import copytree
import xml.etree.ElementTree as ET

VERSION = "1"

if __name__ == "__main__":
    mkdir(VERSION)
    for d in ["frames", "annotations"]:
        copytree(path.join("..", d), path.join(VERSION, d))

    index = {}
    for a in listdir(path.join(VERSION, "annotations")):
        tree = ET.parse(path.join(VERSION, "annotations", a))
        root = tree.getroot()

        objects = []
        for o in root.findall('object'):
            category = o.find('name').text
            bbox = o.find('bndbox')

            xmin = int(bbox.find('xmin').text)
            xmax = int(bbox.find('xmax').text)
            ymin = int(bbox.find('ymin').text)
            ymax = int(bbox.find('ymax').text)

            objects.append({
                "category": category,
                "polygon": [(xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax)]
            })

        index[hash(a)] = {
            "image": "images/" + a.replace(".xml", ".jpg"),
            "annotation": "annotations/" + a,
            "objects": objects
        }

    json.dump(index, open(path.join(VERSION, "index.json"), "w"))
