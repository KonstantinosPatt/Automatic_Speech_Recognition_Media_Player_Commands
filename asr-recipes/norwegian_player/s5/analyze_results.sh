hypothesis_tra=exp/tri3b/decode_tgmed_dev/scoring/14.0.0.tra
ref_trw=exp/tri3b/decode_tgmed_dev/scoring/test_filt.txt

cat $hypothesis_tra | utils/int2sym.pl -f 2- exp/tri3b/graph_tgmed/words.txt | sed s:\<UNK\>::g | sed s/_/-/g > hypothesis.trw

python hypothesis.trw hypothesis.wsj
python $ref_trw ref.wsj

/opt/kaldi/tools/sctk/bin/sclite -i wsj -r ref.wsj -h hypothesis.wsj -o dtl