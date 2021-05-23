import json
import sys
import os 
import os.path

train_folder = os.scandir(sys.argv[1])

train_wav = open(sys.argv[2], "w") 
train_text = open(sys.argv[3], "w")
train_utt2spk = open(sys.argv[4], "w")

dev_wav = open(sys.argv[5], "w") 
dev_text = open(sys.argv[6], "w")
dev_utt2spk = open(sys.argv[7], "w")

wav_list = []
text_list = []
utt2spk_list = []

for train_file in train_folder: 
    if train_file.name.endswith(".json"):    
        #print(type(train_file))
        with open(train_file.path, encoding= 'utf-8') as read_file:
            data = json.load(read_file)
            pid = data["pid"]
            speaker = pid[:8]
            try:
                for i in data['val_recordings']:
                    restofcode = str(i.get('file')[:-4])
                    utterance = str(pid + "_" + restofcode)
                    line_text = str(i.get('text').upper())
                    wav_list.append(utterance + ".wav")
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

counter = 0
for i in wav_list:
    counter +=1
    if counter < 2000:
        train_wav.write(i + "\n")
    elif counter <4000:
        dev_wav.write(i + "\n")
    else:
        break
print("I have a problem after this!")

counter = 0
for i in text_list:
    counter +=1
    if counter < 2000:
        train_text.write(i + '\n')
    elif counter <4000:
        dev_text.write(i + "\n")
    else:
        break

counter = 0
for i in utt2spk_list:
    counter +=1
    if counter < 2000:
        train_utt2spk.write(i + "\n")
    elif counter <4000:
        dev_utt2spk.write(i + "\n")
    else:
        break

print("I have a problem before this!")