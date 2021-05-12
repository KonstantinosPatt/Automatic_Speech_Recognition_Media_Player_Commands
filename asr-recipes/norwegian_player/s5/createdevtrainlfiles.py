import os
import json

train_folder = os.scandir("/other/data/norwegian_resources/audio/metadata/train/")

train_wav = open("/other/users/konspat/asr-tts-class-2021/asr-recipes/norwegian_player/s5/train/wav.scp", "w")
train_text = open("/other/users/konspat/asr-tts-class-2021/asr-recipes/norwegian_player/s5/train/text", "w")
train_utt2spk = open("/other/users/konspat/asr-tts-class-2021/asr-recipes/norwegian_player/s5/train/utt2spk", "w")
train_spk2utt = open("/other/users/konspat/asr-tts-class-2021/asr-recipes/norwegian_player/s5/train/spk2utt", "w")

dev_wav = open("/other/users/konspat/asr-tts-class-2021/asr-recipes/norwegian_player/s5/dev/wav.scp", "w")
dev_text = open("/other/users/konspat/asr-tts-class-2021/asr-recipes/norwegian_player/s5/dev/text", "w")
dev_utt2spk = open("/other/users/konspat/asr-tts-class-2021/asr-recipes/norwegian_player/s5/dev/utt2spk", "w")
dev_spk2utt = open("/other/users/konspat/asr-tts-class-2021/asr-recipes/norwegian_player/s5/dev/spk2utt", "w")

counter = 0
for train_file in train_folder:
    if train_file.is_file and train_file.name.endswith(".json"):
        with open(train_file, "r") as read_file:
            data = json.load(read_file)
            counter = counter +1
        if counter < 800:
            pid = data["pid"]
            speaker = pid[:8]
            train_spk2utt.write("\n" + speaker + " ")
            try:
                for i in data['val_recordings']:
                    restofcode = i.get('file')[:-4]
                    utterance = str(pid + "_" + restofcode)
                    line_text = i.get('text').upper()
                    train_wav.write(utterance + " |\n")
                    train_text.write(utterance + " " + line_text + "\n")
                    train_utt2spk.write(utterance + " " + speaker + "\n")
                    train_spk2utt.write(utterance + " ")
            except:
                continue
        else:
            pid = data["pid"]
            speaker = pid[:8]
            dev_spk2utt.write("\n" + speaker + " ")
            try:
                for i in data['val_recordings']:
                    restofcode = i.get('file')[:-4]
                    utterance = str(pid + "_" + restofcode)
                    line_text = i.get('text').upper()
                    dev_wav.write(utterance + " |\n")
                    dev_text.write(utterance + " " + line_text + "\n")
                    dev_utt2spk.write(utterance + " " + speaker + "\n")
                    dev_spk2utt.write(utterance + " ")

            except:
                continue