#!/usr/bin/env bash

# Copyright 2014
# Apache 2.0
set -x
echo "Number of arguments is  $#"

if [ "$#" -ne 4 ]; then
  echo "Usage: $0 <src-dir> <part-info> <dst-dir>"
  echo "e.g.: $0 data/norwegian train.tsv data/train"
  exit 1
fi

src=$1
train=$2
dev=$3
test=$4

mkdir -p $train || exit 1;
mkdir -p $dev || exit 1;
mkdir -p $test || exit 1;

[ ! -d $src ] && echo "$0: no such directory $src" && exit 1;

for part in $train $dev $test; do 
  wav_scp=$part/wav.scp; [[ -f "$wav_scp" ]] && rm $wav_scp
  trans=$part/text; [[ -f "$trans" ]] && rm $trans
  utt2spk=$part/utt2spk; [[ -f "$utt2spk" ]] && rm $utt2spk
  done

# process tsv files to extract all required information 
python3 createdevtrainfiles3.py $src/train $train/wav.scp $train/text $train/utt2spk $dev/wav.scp $dev/text $dev/utt2spk 
python3 createtestfiles_copy.py $src/test $test/wav.scp $test/text $test/utt2spk

echo "I HAVE A PROBLEM AFTER THIS" 

for part in $train $dev $test; do 
  spk2utt=$part/spk2utt
  utt2spk=$part/utt2spk
  echo "Doing $utt2spk"
  utils/utt2spk_to_spk2utt.pl <$utt2spk >$spk2utt || exit 1
  sort -o $spk2utt{,}
  done

#python 3 sortspk2utt.py $train/$spk2utt

# data validation
ntrans=$(wc -l <$trans)
nutt2spk=$(wc -l <$utt2spk)
! [ "$ntrans" -eq "$nutt2spk" ] && \
  echo "Inconsistent #transcripts($ntrans) and #utt2spk($nutt2spk)" && exit 1;


for part in $train $dev $test; do 
  utils/validate_data_dir.sh --no-feats $part || exit 1;
  echo "$0: successfully prepared data in $part"
  done

