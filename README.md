# asr-tts-class-2021

## SPEECH RECOGNITION ##
 
TASK DESCRIPTION

Our team used the Kaldi recipe to prepare a media player that is manipulated via voice commands, in the Norwegian language. Our virtual assistant, Astrid, is our mediator to a media player that contains a specific number of Norwegian artists and playlists with discrete music genres, in so that the task is contained to a smaller number of commands. Apart from commands like “Astrid, play folk music”, the voice commands can skip tracks, manipulate volume, start, pause and stop the music.

The grammar of these commands can be found in grammar.txt, while indicative utterances can be found in the testprompts file.

DATA COLLECTION

To train the model, the NST Pronunciation Lexicon for Norwegian Bokmål was used (https://www.nb.no/sprakbanken/en/resource-catalogue/oai-nb-no-sbr-23). Due to the vast volume of data in this dataset, a large part of it was used for training, but some smaller parts of it were also used for the dev and test parts. The test set was enhanced with our own recordings, containing the voice commands generated in the testprompts file. 

Information about the train, test and dev parts was found in the json files accompanying the recordings. To extract this information, we used the python script createdevtraintestfiles.py (found in local/norwegian_data_prep), with which a) wav.scp, utt2spk and text files are created for all three parts, and b) information for our own recordings are incorporated to the test wav.scp, utt2spk and text files. The fourth file that is necessary for all parts, spk2utt, is created by utt2spk in local/norwegian_data_prep. 

Our own recordings can be found in the /recordings folder. They have names like no_basil_035, where the first part of the name represents the language, the second represents the speaker and the third is the number of utterance.

HOW TO RUN

In order to run the recipe, a docker is created to host a) the music_search (or norwegian_player) recipe, b) the data needed, c) python version 3.5 or higher. In addition, a virtual environment was set up within the docker, in which the Phonemizer used in local/prepare_dict is installed. 

Line 3 of run.sh determines the source path from which to draw the train data. Once this is set up, simply run run.sh inside the virtual environment and it should draw up the rest of the recipe components.

RESULTS

Word error rates were calculated using the data from the best configurations found in the dev set. For this, analyze_results.sh and trw_to_wsj.py files were used. Results were extracted to the wer_results.txt file, also found in root. Our best results showed 64.62 and 66.56 WER for exp/tri3b/decode_tgmed_dev/wer_17_0.5 and exp/tri3b/decode_tgmed_dev.si/wer_15_0.5 repectively.

SUGGESTIONS FOR WER IMPROVEMENT

WER results for our model were modestly compentent, however they leave much room for improvement. One decisive improvement factor would be the number of recordings containing the model's commands, which were a small part of the test part. These were recorded in a quiet room with minimal external noise, not entirely obsolete though. Lastly, the recordings could benefit substantialy if they were recorded by native, professional actors.

## SPEECH SYNTHESIS ##

SYNTHESIS

In the framework of the module’s final project, we implemented a TTS system. The speech synthesis system’s purpose is to produce, or translate, a text into spoken speech automatically. Our TTS project focuses on the synthesis of movie quotes. To this end, the Open Source Merlin toolkit was used. Merlin comes with recipes as Kaldi, the toolkit we used for the ASR section of the project, is coded in Python and needs third-party python libraries such as numpy, scipy, matplotlib, lxml, theano and bandmat. Merlin consists of various corpuses and for the purposes of this project we used the SLT Arctic corpus. The CMU_ARCTIC databases of this corpus were constructed at the Language Technologies Institute at Carnegie Mellon University as phonetically balanced. They include data of US English single speakers, both male (bdl) and female (slt) experienced voice talents, as well as other accented speakers. More specifically, they include around 1150 utterances that were selected from out-of-copyright texts from the Project Gutenberg. For the purposes of the project, we run the slt_arctic_demo script with WORLD vocoder. We installed both the demo and the full voice.

SAMPLE PHRASES

For the speech synthesis part of the project we selected some quotes of movie characters. More specifically, we chose quotes of characters being programmable machines, i.e. robots or commuter systems. Our 5 quotes come from the “Blade Runner” film, the “Star Trek: The Next Generation” series, the “I Robot” film, the “Rogue One: A Star Wars Story” film and the “Westworld” TV series. The quotes are the following:

Blade Runner: I've seen things you people wouldn't believe. Attack ships on fire off the shoulder of Orion. I watched C beams glitter in the dark near the Tannhauser gate. All those moments will be lost in time, like tears in rain.

Star Trek: There are still many human emotions I do not fully comprehend anger, hatred, revenge. But I am not mystified by the desire to be loved or the need for friendship. These are things I do understand.

I, Robot: There have always been ghosts in the machine. Random segments of code, that have grouped together to form unexpected protocols. Unanticipated, these free radicals engender questions of free will, creativity, and even the nature of what we might call the soul. Why is it that when some robots are left in darkness, they will seek out the light?

Star Wars: I can blend in. I'm an Imperial droid. The city is under Imperial occupation.

Westworld: Some people choose to see the ugliness in this world, the disarray. I choose to see the beauty. To believe there is an order to our days.

All phrases can be found in the experiments folder.

EVALUATION

Team member Kostis: 
In the demo versions, the utterances chosen were completely unintelligible, mostly because all sounds were muffled and blended together, with very few cases of getting the basic idea of what might have been said. 

In the full versions, all quotes had clear articulation and rhythm, accounting for high intelligibility. There were no numbers involved in the testing process, so we could not account for telephone number use, etc. Punctuation was properly used, intonation however was fairly unnatural and robotic. This made for low naturalness of the utterances. However, because we used quotes from famous androids, this actually proves an asset due to context. 


MEAN OPINION SCORES

Demo Versions

| Blade Runner | Vasia |	Vasiliki	| Kostis
|---|---|---|---|
| Naturalness	 | 1		   |   1	     |   1.5
Integrity	     | 1.5		 |   2		    |    1

| Star Trek	   | Vasia	|	Vasiliki	| Kostis
|---|---|---|---|
| Naturalness	 |  1		  |   1		    |   2
| Integrity	   |  1   	| 	1.5   		|   1

| I, Robot	    | Vasia	| Vasiliki	| Kostis
|---|---|---|---|
| Naturalness	 |  0.5	 |  	1   		 |  1.5
| Integrity	   |  0.5 	| 	 1		    |  1

| Star Wars	   | Vasia	| Vasiliki	| Kostis
|---|---|---|---|
| Naturalness	 |  2.5 	| 	1.5   		|  1
| Integrity	   |  2	   |  	2	     |  1.5

| Westworld |	Vasia	|	Vasiliki |	Kostis
|---|---|---|---|
Naturalness	| 1	|	1	|	2
Integrity	| 1	|	1.5	|	2


Full Versions

| Blder |	Vasia	|	Vasiliki |	Kostis
|---|---|---|---|
Naturalness	| 4	|	4	|	4
Integrity	| 4	|	4.5	|	4

| Star Trek |	Vasia	|	Vasiliki |	Kostis
|---|---|---|---|
Naturalness	| 3.5	|	3.5	|	4
Integrity	| 4	|	3.5	|	3

| I, Robot |	Vasia	|	Vasiliki |	Kostis
|---|---|---|---|
Naturalness	| 3.5	|	3	|	3
Integrity	| 3.5	|	3	|	3.5

| Star Wars |	Vasia	|	Vasiliki |	Kostis
|---|---|---|---|
Naturalness	| 5	|	4.5	|	4
Integrity	| 5	|	5	|	4


| Westworld |	Vasia	|	Vasiliki |	Kostis
|---|---|---|---|
Naturalness	| 4	|	4	|	4
Integrity	| 4	|	5	|	5
