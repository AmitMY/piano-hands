import os
import random
import subprocess

import cv2

files = []
for file in os.listdir("."):
    if file.endswith(".mp4") or file.endswith(".mkv") or file.endswith(".webm"):
        files.append(file)

print(len(files), "files")

for file in files:
    cap = cv2.VideoCapture(files[0])

    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    # print(frames, fps)

    for i in range(3):
        random_frame = random.randint(0, frames)
        time = random_frame / fps

        compressed_filename = file.replace(' ', '_') + "_" + str(random_frame)

        cmd = ["ffmpeg", "-ss", str(time), "-i \"" + file + "\" -frames:v 1 \"../frames/" + compressed_filename + ".jpg\""]
        subprocess.run(" ".join(cmd), shell=True, check=True)
