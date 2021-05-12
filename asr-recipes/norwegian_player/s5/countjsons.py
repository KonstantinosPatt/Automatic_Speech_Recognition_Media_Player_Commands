import os
import json

test_folder = os.scandir("/other/data/norwegian_resources/audio/metadata/test/")
train_folder = os.scandir("/other/data/norwegian_resources/audio/metadata/train/")

test_counter = 0
for test_file in test_folder:
    if test_file.is_file and test_file.name.endswith(".json"):
        test_counter +=1
print(test_counter)

train_counter = 0
for test_file in train_folder:
    if test_file.is_file and test_file.name.endswith(".json"):
        train_counter +=1
print(train_counter)