# Copyright 2021    Ke Li

""" This script estimates neural LM scores for each arc on lattices.
    It is called by steps/pytorchnn/lmrescore_lattice_pytorchnn.sh
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import argparse
from collections import defaultdict


def get_arc_scores(arc_path, score_path):
    r"""Estimate neural LM scores for each arc on lattices with state sequences
    of paths and the corresponding neural LM scores of words on these paths for
    each lattice as inputs. The sequences of states and word scores are
    generated by the binary latbin/lattice-path-cover.

    Assume the input state sequences in arc_path are in the following format:
        en_4156-A_030185-030248-1 0 1 2
        en_4156-A_030470-030672-1 0 1 2 10 11 12 13 14 15 16 17
        en_4156-A_030470-030672-2 0 1 2 3 4 5 6 7 8 9
        ...
    Each pair of two consecutive states represents an arc, e.g. (0, 1), (1, 2).
    
    The input file score_path of word scores has the following format:
        en_4156-A_030185-030248-1 2.7702 1.9545 0.9442
        en_4156-A_030470-030672-1 3.6918 3.7159 4.1794 0.1375 2.3944 9.3834 4.5469 7.0772 3.6172 7.2183 2.1540
        en_4156-A_030470-030672-2 3.6918 3.7159 4.5248 2.3689 8.9368 4.2876 7.0702 3.0812 7.5044 2.2388
        ...
    Each score is a neural LM score for the corresponding arc (word) given its
    history, e.g. 2.7702 is computed as p((0, 1)|<s>) for arc (0, 1).
    The last score in each line is the probability for end of sentence symbol
    given its history. It is added to the final weight of a state in the
    rescoring stage by binary latbin/lattice-add-nnlmscore. For example, 0.9442
    is for state 2 of the lattice with utterance id as en_4156-A_030185-030248.
    
    Note that an arc can occur in more than one path. Its neural LM score is
    estimated as the score computed with the best history for that arc. To this
    end, the lines of scores for each utterance in score_path have been sorted
    from the best to the worst.
    
    Args:
        arc_path (str):     A input file of state sequences to represent arcs.
        score_path (str):   A input file of neural LM scores in the above format.

    Returns:
        The estimated scores of all arcs represented by a dictionary of dictionary.
    """
    arc_scores = defaultdict(lambda: defaultdict(float))
    with open(arc_path, 'r', encoding='utf-8') as f1,\
         open(score_path, 'r', encoding='utf-8') as f2:
        all_arcs = f1.readlines()
        all_scores = f2.readlines()
        assert len(all_arcs) == len(all_scores)
        for arcs_per_line, scores_per_line in zip(all_arcs, all_scores):
            arcs_with_key = arcs_per_line.split()
            key = arcs_with_key[0]
            key = key.rsplit('-', 1)[0]
            arcs = arcs_with_key[1:]
            scores = scores_per_line.split()[1:]
            for i in range(len(arcs) - 1):
                arc = (int(arcs[i]), int(arcs[i + 1]))
                score = float(scores[i])
                if arc not in arc_scores[key]:
                    arc_scores[key][arc] = score
                else:
                    continue
            arc_final = (int(arcs[-1]), int(arcs[-1]))
            score_final = float(scores[-1])
            if arc_final not in arc_scores[key]:
                arc_scores[key][arc_final] = score_final
            else:
                continue
    return arc_scores


def write_scores(arc_scores, path):
    r"""Write out estimated neural LM scores for arcs on lattices.
    Each line represents an arc as (start_id, end_id) and its score:
        utterance-id start_id end_id neural LM score for arc (start_id, end_id)
        en_4156-A_030185-030248 0 1 2.7702
        en_4156-A_030185-030248 1 2 1.9545
        en_4156-A_030185-030248 2 2 0.9442
        en_4156-A_030470-030672 0 1 3.6918
        en_4156-A_030470-030672 1 2 3.7159
        en_4156-A_030470-030672 2 10 4.1794
        ...

    Args:
        arc_scores: Nueral LM scores of arcs of each lattice.
        path (str): Output file of arc scores in the above format.
    """
    with open(path, 'w', encoding='utf-8') as f:
        for key in arc_scores.keys():
            for arc, score in arc_scores[key].items():
                f.write('{0} {1} {2} {3}\n'.format(key, arc[0], arc[1], score))
    print("Write estimated neural LM scores to file {}.".format(path))


def main():
    parser = argparse.ArgumentParser(description="Estimate neural language model"
                                     "scores for arcs on lattices.")
    parser.add_argument('--arc-ids', type=str, required=True,
                        help="States sequences generated from a lattice.")
    parser.add_argument('--scores', type=str, required=True,
                        help="Input nueral language model scores of each word"
                             "in the generated sequences.")
    parser.add_argument('--outfile', type=str, required=True,
                        help="Output file of estimated scores for each word"
                             "in hypotheses of all utterances.")
    args = parser.parse_args()
    assert os.path.exists(args.arc_ids), "Path for input state sequences does not exist."
    assert os.path.exists(args.scores), "Path for neural language model scores does not exist."
    
    print("Load state sequences and neural LM scores.")
    arc_scores = get_arc_scores(args.arc_ids, args.scores)
    print("Write out estimated scores for each arc.")
    write_scores(arc_scores, args.outfile)

if __name__ == '__main__':
    main()
