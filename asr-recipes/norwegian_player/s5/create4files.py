# -*- coding: utf-8 -*-
"""
Created on Tue May 11 14:55:28 2021

@author: kosti
"""

import os
import json

test_folder = os.scandir("/other/data/norwegian_resources/audio/metadata/test/")

wav = open("/other/users/konspat/asr-tts-class-2021/asr-recipes/norwegian_player/s5/wav.txt", "w")
text = open("/other/users/konspat/asr-tts-class-2021/asr-recipes/norwegian_player/s5/text.txt", "w")
utt2spk = open("/other/users/konspat/asr-tts-class-2021/asr-recipes/norwegian_player/s5/utt2spk.txt", "w")
spk2utt = open("/other/users/konspat/asr-tts-class-2021/asr-recipes/norwegian_player/s5/spk2utt.txt", "w")

for test_file in test_folder:
    if test_file.is_file and test_file.name.endswith(".json"):
        with open(test_file, "r") as read_file:
            data = json.load(read_file)
        for i in data:
            pid = data["pid"]
            speaker = pid[:8]
            spk2utt.write(speaker + " ")
            try:
                for i in data['val_recordings']:
                    restofcode = i.get('file')[:-4]
                    utterance = str(pid + "_" + restofcode)
                    line_text = i.get('text').upper()
                    wav.write(pid + "_" + restofcode + " |\n") 
                    text.write(utterance + " " + line_text + "\n") 
                    utt2spk.write(utterance + " " + speaker + "\n") 
                    spk2utt.write(utterance + " ")
            except:
                continue
            