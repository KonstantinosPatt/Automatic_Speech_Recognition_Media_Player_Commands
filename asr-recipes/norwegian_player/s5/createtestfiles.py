# -*- coding: utf-8 -*-
"""
Created on Tue May 11 14:55:28 2021

@author: kosti
"""

import os
import json

test_folder = os.scandir("/other/data/norwegian_resources/audio/metadata/test/")

test_wav = open("/other/users/konspat/asr-tts-class-2021/asr-recipes/norwegian_player/s5/test/wav.scp", "w")
test_text = open("/other/users/konspat/asr-tts-class-2021/asr-recipes/norwegian_player/s5/test/text", "w")
test_utt2spk = open("/other/users/konspat/asr-tts-class-2021/asr-recipes/norwegian_player/s5/test/utt2spk", "w")
test_spk2utt = open("/other/users/konspat/asr-tts-class-2021/asr-recipes/norwegian_player/s5/test/spk2utt", "w")

for test_file in test_folder:
    if test_file.is_file and test_file.name.endswith(".json"):
        with open(test_file, "r") as read_file:
            data = json.load(read_file)
        for i in data:
            pid = data["pid"]
            speaker = pid[:8]
            test_spk2utt.write("\n" + speaker + " ")
            try:
                for i in data['val_recordings']:
                    restofcode = i.get('file')[:-4]
                    utterance = str(pid + "_" + restofcode)
                    line_text = i.get('text').upper()
                    test_wav.write(pid + "_" + restofcode + " |\n")
                    test_text.write(utterance + " " + line_text + "\n")
                    test_utt2spk.write(utterance + " " + speaker + "\n")
                    test_spk2utt.write(utterance + " ")
            except:
                continue