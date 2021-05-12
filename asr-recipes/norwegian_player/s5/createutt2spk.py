


utt2spk = open("/other/users/konspat/asr-tts-class-2021/asr-recipes/norwegian_player/s5/utt2spk.txt", "w")

for test_file in test_folder:
    if test_file.is_file and test_file.name.endswith(".json"):
        with open(test_file, "r") as read_file:
            data = json.load(read_file)
        for i in data:
            pid = data["pid"]
            speaker = pid[:8]
            try:
                for i in data['val_recordings']:
                    restofcode = i.get('file')[:-4]
                    utterance = str(pid + "_" + restofcode)
                    utt2spk.write(utterance + " " + speaker + "\n")   
                    print(utterance + " " + speaker)
            except:
                continue