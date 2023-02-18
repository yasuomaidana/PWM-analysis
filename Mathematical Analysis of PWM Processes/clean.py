import os
import shutil

dir_list = os.listdir()

for dir in dir_list:
    if ".egg-info" in dir:
        shutil.rmtree(dir)

to_clean = ['build','dist']
for clean in to_clean:
    if os.path.exists(clean):
        shutil.rmtree(clean)
