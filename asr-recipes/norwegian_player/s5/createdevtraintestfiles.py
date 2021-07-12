import json
import sys
import os 
import os.path
import re

train_folder = os.scandir(sys.argv[1])

train_wav = open(sys.argv[2], "w") 
train_text = open(sys.argv[3], "w", encoding='utf-8')
train_utt2spk = open(sys.argv[4], "w")

dev_wav = open(sys.argv[5], "w") 
dev_text = open(sys.argv[6], "w", encoding='utf-8')
dev_utt2spk = open(sys.argv[7], "w")

test_wav = open(sys.argv[8], "w") 
test_text = open(sys.argv[9], "w", encoding='utf-8')
test_utt2spk = open(sys.argv[10], "w")

nr_path = "/data/norwegian_resources/audio/no/"

wav_list = []
text_list = []
utt2spk_list = []

for train_file in train_folder: 
    if train_file.name.endswith(".json"):    
        with open(train_file.path, 'r', encoding= 'utf-8') as read_file:
            data = json.load(read_file)
            pid = data["pid"]
            speaker = pid[:8]
        try:
            for i in data['val_recordings']:
                restofcode = i.get('file')[:-4]
                utterance = str(pid + "_" + restofcode)
                line_text = i.get('text').upper()
                line_text = re.sub(r'[^\w\s]', "", line_text)
                wav_list.append(utterance + " " + nr_path + pid + "/" + utterance + "-1.wav")
                text_list.append(utterance + " " + line_text)
                utt2spk_list.append(utterance + " " + speaker)
        except:
            continue

wav_list = sorted(wav_list)
text_list = sorted(text_list)
utt2spk_list = sorted(utt2spk_list)

print()
print(len(wav_list))
print(len(text_list))
print(len(utt2spk_list))
print()

train_num = 50000
dev_num = 70000
test_num = 75000

counter = 0
for i in wav_list:
    counter +=1
    if counter < train_num:
        train_wav.write(i + "\n")
    elif counter < dev_num:
        dev_wav.write(i + "\n")
    elif counter < test_num:
        test_wav.write(i + "\n")
    else:
        break

counter = 0
for i in text_list:
    counter +=1
    if counter < train_num:
        train_text.write(i + '\n')
    elif counter < dev_num:
        dev_text.write(i + "\n")
    elif counter < test_num:
        test_text.write(i + "\n")
    else:
        break

counter = 0
for i in utt2spk_list:
    counter +=1
    if counter < train_num:
        train_utt2spk.write(i + "\n")
    elif counter < dev_num:
        dev_utt2spk.write(i + "\n")
    elif counter < test_num:
        test_utt2spk.write(i + "\n")
    else:
        break
