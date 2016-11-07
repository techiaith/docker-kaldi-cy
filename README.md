# kaldi-env

Adnabod Lleferydd Cymraeg gyda Kaldi. 


### Allbwn hyfforddi llwyddianus (28/10/2016)

Gyda corpws Paldaruo v2 ([metashare.techiaith.cymru](http://metashare.techiaith.cymru/repository/browse/paldaruo-speech-corpus/ee11ba2c11de11e68e470242ac110068e5a5bf5511a54bfc8a286030314b88cc/))

```
root@0cbb1df73518:/usr/local/src/kaldi/egs/paldaruo_welsh# ./run.sh

===== PREPARING ACOUSTIC DATA =====


===== FEATURES EXTRACTION =====

utils/validate_data_dir.sh: Successfully validated data-directory data/train
fix_data_dir.sh: kept all 8461 utterances.
fix_data_dir.sh: old files are kept in data/train/.backup
utils/validate_data_dir.sh: Successfully validated data-directory data/test
fix_data_dir.sh: kept all 1933 utterances.
fix_data_dir.sh: old files are kept in data/test/.backup
steps/make_mfcc.sh --nj 3 --cmd run.pl data/train exp/make_mfcc/train mfcc
utils/validate_data_dir.sh: Successfully validated data-directory data/train
steps/make_mfcc.sh: [info]: no segments file exists: assuming wav.scp indexed by utterance.
Succeeded creating MFCC features for train
steps/make_mfcc.sh --nj 3 --cmd run.pl data/test exp/make_mfcc/test mfcc
utils/validate_data_dir.sh: Successfully validated data-directory data/test
steps/make_mfcc.sh: [info]: no segments file exists: assuming wav.scp indexed by utterance.
Succeeded creating MFCC features for test
steps/compute_cmvn_stats.sh data/train exp/make_mfcc/train mfcc
Succeeded creating CMVN stats for train
steps/compute_cmvn_stats.sh data/test exp/make_mfcc/test mfcc
Succeeded creating CMVN stats for test
                                                                                                                        [297/1389]
===== PREPARING LANGUAGE DATA =====

utils/prepare_lang.sh data/local/dict <UNK> data/local/lang data/lang
Checking data/local/dict/silence_phones.txt ...
--> reading data/local/dict/silence_phones.txt
--> data/local/dict/silence_phones.txt is OK

Checking data/local/dict/optional_silence.txt ...
--> reading data/local/dict/optional_silence.txt
--> data/local/dict/optional_silence.txt is OK

Checking data/local/dict/nonsilence_phones.txt ...
--> reading data/local/dict/nonsilence_phones.txt
--> data/local/dict/nonsilence_phones.txt is OK

Checking disjoint: silence_phones.txt, nonsilence_phones.txt
--> disjoint property is OK.

Checking data/local/dict/lexicon.txt
--> reading data/local/dict/lexicon.txt
--> data/local/dict/lexicon.txt is OK

Checking data/local/dict/extra_questions.txt ...
--> data/local/dict/extra_questions.txt is empty (this is OK)
--> SUCCESS [validating dictionary directory data/local/dict]

**Creating data/local/dict/lexiconp.txt from data/local/dict/lexicon.txt
fstaddselfloops data/lang/phones/wdisambig_phones.int data/lang/phones/wdisambig_words.int
prepare_lang.sh: validating output directory
utils/validate_lang.pl data/lang
Checking data/lang/phones.txt ...
--> data/lang/phones.txt is OK

Checking words.txt: #0 ...
--> data/lang/words.txt is OK

Checking disjoint: silence.txt, nonsilence.txt, disambig.txt ...
--> silence.txt and nonsilence.txt are disjoint
--> silence.txt and disambig.txt are disjoint
--> disambig.txt and nonsilence.txt are disjoint
--> disjoint property is OK

Checking sumation: silence.txt, nonsilence.txt, disambig.txt ...
--> summation property is OK

Checking data/lang/phones/context_indep.{txt, int, csl} ...
--> 10 entry/entries in data/lang/phones/context_indep.txt
--> data/lang/phones/context_indep.int corresponds to data/lang/phones/context_indep.txt
--> data/lang/phones/context_indep.csl corresponds to data/lang/phones/context_indep.txt
--> data/lang/phones/context_indep.{txt, int, csl} are OK

Checking data/lang/phones/nonsilence.{txt, int, csl} ...
--> 216 entry/entries in data/lang/phones/nonsilence.txt
--> data/lang/phones/nonsilence.int corresponds to data/lang/phones/nonsilence.txt
--> data/lang/phones/nonsilence.csl corresponds to data/lang/phones/nonsilence.txt
--> data/lang/phones/nonsilence.{txt, int, csl} are OK

Checking data/lang/phones/silence.{txt, int, csl} ...
--> 10 entry/entries in data/lang/phones/silence.txt
--> data/lang/phones/silence.int corresponds to data/lang/phones/silence.txt
--> data/lang/phones/silence.csl corresponds to data/lang/phones/silence.txt
--> data/lang/phones/silence.{txt, int, csl} are OK

Checking data/lang/phones/optional_silence.{txt, int, csl} ...
--> 1 entry/entries in data/lang/phones/optional_silence.txt
--> data/lang/phones/optional_silence.int corresponds to data/lang/phones/optional_silence.txt
--> data/lang/phones/optional_silence.csl corresponds to data/lang/phones/optional_silence.txt
--> data/lang/phones/optional_silence.{txt, int, csl} are OK

Checking data/lang/phones/disambig.{txt, int, csl} ...
--> 7 entry/entries in data/lang/phones/disambig.txt
--> data/lang/phones/disambig.int corresponds to data/lang/phones/disambig.txt
--> data/lang/phones/disambig.csl corresponds to data/lang/phones/disambig.txt
--> data/lang/phones/disambig.{txt, int, csl} are OK

Checking data/lang/phones/roots.{txt, int} ...
--> 56 entry/entries in data/lang/phones/roots.txt
--> data/lang/phones/roots.int corresponds to data/lang/phones/roots.txt
--> data/lang/phones/roots.{txt, int} are OK

Checking data/lang/phones/sets.{txt, int} ...
--> 56 entry/entries in data/lang/phones/sets.txt
--> data/lang/phones/sets.int corresponds to data/lang/phones/sets.txt
--> data/lang/phones/sets.{txt, int} are OK

Checking data/lang/phones/extra_questions.{txt, int} ...
--> 9 entry/entries in data/lang/phones/extra_questions.txt
--> data/lang/phones/extra_questions.int corresponds to data/lang/phones/extra_questions.txt
--> data/lang/phones/extra_questions.{txt, int} are OK

Checking data/lang/phones/word_boundary.{txt, int} ...
--> 226 entry/entries in data/lang/phones/word_boundary.txt
--> data/lang/phones/word_boundary.int corresponds to data/lang/phones/word_boundary.txt
--> data/lang/phones/word_boundary.{txt, int} are OK

Checking optional_silence.txt ...
--> reading data/lang/phones/optional_silence.txt
--> data/lang/phones/optional_silence.txt is OK

Checking disambiguation symbols: #0 and #1
--> data/lang/phones/disambig.txt has "#0" and "#1"
--> data/lang/phones/disambig.txt is OK

Checking topo ...

Checking word_boundary.txt: silence.txt, nonsilence.txt, disambig.txt ...
--> data/lang/phones/word_boundary.txt doesn't include disambiguation symbols
--> data/lang/phones/word_boundary.txt is the union of nonsilence.txt and silence.txt
--> data/lang/phones/word_boundary.txt is OK

Checking word-level disambiguation symbols...
--> data/lang/phones/wdisambig.txt exists (newer prepare_lang.sh)
Checking word_boundary.int and disambig.int
--> generating a 38 word sequence
--> resulting phone sequence from L.fst corresponds to the word sequence
--> L.fst is OK
--> generating a 89 word sequence
--> resulting phone sequence from L_disambig.fst corresponds to the word sequence
--> L_disambig.fst is OK

Checking data/lang/oov.{txt, int} ...
--> 1 entry/entries in data/lang/oov.txt
--> data/lang/oov.int corresponds to data/lang/oov.txt
--> data/lang/oov.{txt, int} are OK

--> data/lang/L.fst is olabel sorted
--> data/lang/L_disambig.fst is olabel sorted
--> SUCCESS [validating lang directory data/lang]

===== LANGUAGE MODEL CREATION =====
===== MAKING lm.arpa =====


===== MAKING G.fst =====

arpa2fst -
LOG (arpa2fst:Read():arpa-file-parser.cc:90) Reading \data\ section.
LOG (arpa2fst:Read():arpa-file-parser.cc:145) Reading \1-grams: section.
LOG (arpa2fst:Read():arpa-file-parser.cc:145) Reading \2-grams: section.
LOG (arpa2fst:Read():arpa-file-parser.cc:145) Reading \3-grams: section.
LOG (arpa2fst:RemoveRedundantStates():arpa-lm-compiler.cc:341) Reduced num-states from 456188 to 137295

===== MONO TRAINING =====

steps/train_mono.sh --nj 3 --cmd run.pl data/train data/lang exp/mono
steps/train_mono.sh: Initializing monophone system.
steps/train_mono.sh: Compiling training graphs
steps/train_mono.sh: Aligning data equally (pass 0)
steps/train_mono.sh: Pass 1
steps/train_mono.sh: Aligning data
steps/train_mono.sh: Pass 2
steps/train_mono.sh: Aligning data
steps/train_mono.sh: Pass 3
steps/train_mono.sh: Aligning data
steps/train_mono.sh: Pass 4
steps/train_mono.sh: Aligning data
steps/train_mono.sh: Pass 5
steps/train_mono.sh: Aligning data
steps/train_mono.sh: Pass 6
steps/train_mono.sh: Aligning data
steps/train_mono.sh: Pass 7
steps/train_mono.sh: Aligning data
steps/train_mono.sh: Pass 8
steps/train_mono.sh: Aligning data
steps/train_mono.sh: Pass 9
steps/train_mono.sh: Aligning data
steps/train_mono.sh: Pass 10
steps/train_mono.sh: Aligning data
steps/train_mono.sh: Pass 11
steps/train_mono.sh: Pass 12
steps/train_mono.sh: Aligning data
steps/train_mono.sh: Pass 13
steps/train_mono.sh: Pass 14
steps/train_mono.sh: Aligning data
steps/train_mono.sh: Pass 15
steps/train_mono.sh: Pass 16
steps/train_mono.sh: Aligning data
steps/train_mono.sh: Pass 17
steps/train_mono.sh: Pass 18
steps/train_mono.sh: Aligning data
steps/train_mono.sh: Pass 19
steps/train_mono.sh: Pass 20
steps/train_mono.sh: Aligning data
steps/train_mono.sh: Pass 21
steps/train_mono.sh: Pass 22
steps/train_mono.sh: Pass 23
steps/train_mono.sh: Aligning data
steps/train_mono.sh: Pass 24
steps/train_mono.sh: Pass 25
steps/train_mono.sh: Pass 26
steps/train_mono.sh: Aligning data
steps/train_mono.sh: Pass 27
steps/train_mono.sh: Pass 28
steps/train_mono.sh: Pass 29
steps/train_mono.sh: Aligning data
steps/train_mono.sh: Pass 30
steps/train_mono.sh: Pass 31
steps/train_mono.sh: Pass 32
steps/train_mono.sh: Aligning data
steps/train_mono.sh: Pass 33
steps/train_mono.sh: Pass 34
steps/train_mono.sh: Pass 35
steps/train_mono.sh: Aligning data
steps/train_mono.sh: Pass 36
steps/train_mono.sh: Pass 37
steps/train_mono.sh: Pass 38
steps/train_mono.sh: Aligning data
steps/train_mono.sh: Pass 39
steps/diagnostic/analyze_alignments.sh --cmd run.pl data/lang exp/mono
steps/diagnostic/analyze_alignments.sh: see stats in exp/mono/log/analyze_alignments.log
2192 warnings in exp/mono/log/align.*.*.log
1418 warnings in exp/mono/log/acc.*.*.log
200 warnings in exp/mono/log/update.*.log
exp/mono: nj=3 align prob=-84.74 over 26.34h [retry=0.5%, fail=0.4%] states=172 gauss=987
steps/train_mono.sh: Done training monophone system in exp/mono

===== MONO DECODING =====

tree-info exp/mono/tree
tree-info exp/mono/tree
fstpushspecial
fstminimizeencoded
fsttablecompose data/lang/L_disambig.fst data/lang/G.fst
fstdeterminizestar --use-log=true
fstisstochastic data/lang/tmp/LG.fst
-0.048088 -0.0490423
[info]: LG not stochastic.
fstcomposecontext --context-size=1 --central-position=0 --read-disambig-syms=data/lang/phones/disambig.int --write-disambig-syms=da
ta/lang/tmp/disambig_ilabels_1_0.int data/lang/tmp/ilabels_1_0
fstisstochastic data/lang/tmp/CLG_1_0.fst
-0.048088 -0.0490423
[info]: CLG not stochastic.
make-h-transducer --disambig-syms-out=exp/mono/graph/disambig_tid.int --transition-scale=1.0 data/lang/tmp/ilabels_1_0 exp/mono/tre
e exp/mono/final.mdl
fstdeterminizestar --use-log=true
fsttablecompose exp/mono/graph/Ha.fst data/lang/tmp/CLG_1_0.fst
fstminimizeencoded
fstrmsymbols exp/mono/graph/disambig_tid.int
fstrmepslocal
fstisstochastic exp/mono/graph/HCLGa.fst
0.00044789 -0.0977195
HCLGa is not stochastic
add-self-loops --self-loop-scale=0.1 --reorder=true exp/mono/final.mdl
steps/decode.sh --config conf/decode.config --nj 3 --cmd run.pl exp/mono/graph data/test exp/mono/decode
decode.sh: feature type is delta
steps/diagnostic/analyze_lats.sh --cmd run.pl exp/mono/graph exp/mono/decode
steps/diagnostic/analyze_lats.sh: see stats in exp/mono/decode/log/analyze_alignments.log
Overall, lattice depth (10,50,90-percentile)=(2,11,54) and mean=22.2
steps/diagnostic/analyze_lats.sh: see stats in exp/mono/decode/log/analyze_lattice_depth_stats.log
exp/mono/decode/wer_19
%WER 92.21 [ 13526 / 14669, 5048 ins, 127 del, 8351 sub ]
%SER 99.90 [ 1931 / 1933 ]

===== MONO ALIGNMENT =====

steps/align_si.sh --nj 3 --cmd run.pl data/train data/lang exp/mono exp/mono_ali
steps/align_si.sh: feature type is delta
steps/align_si.sh: aligning data in data/train using model from exp/mono, putting alignments in exp/mono_ali
steps/diagnostic/analyze_alignments.sh --cmd run.pl data/lang exp/mono_ali
steps/diagnostic/analyze_alignments.sh: see stats in exp/mono_ali/log/analyze_alignments.log
steps/align_si.sh: done aligning data.

===== TRI1 (first triphone pass) TRAINING =====

steps/train_deltas.sh --cmd run.pl 2000 11000 data/train data/lang exp/mono_ali exp/tri1
steps/train_deltas.sh: accumulating tree stats
steps/train_deltas.sh: getting questions for tree-building, via clustering
steps/train_deltas.sh: building the tree
WARNING (gmm-init-model:InitAmGmm():gmm-init-model.cc:55) Tree has pdf-id 0 with no stats; corresponding phone list: 1 2 3 4 5
** The warnings above about 'no stats' generally mean you have phones **
** (or groups of phones) in your phone set that had no corresponding data. **
** You should probably figure out whether something went wrong, **
** or whether your data just doesn't happen to have examples of those **
** phones. **
steps/train_deltas.sh: converting alignments from exp/mono_ali to use current tree
steps/train_deltas.sh: compiling graphs of transcripts
steps/train_deltas.sh: training pass 1
steps/train_deltas.sh: training pass 2
steps/train_deltas.sh: training pass 3
steps/train_deltas.sh: training pass 4
steps/train_deltas.sh: training pass 5
steps/train_deltas.sh: training pass 6
steps/train_deltas.sh: training pass 7
steps/train_deltas.sh: training pass 8
steps/train_deltas.sh: training pass 9
steps/train_deltas.sh: training pass 10
steps/train_deltas.sh: aligning data
steps/train_deltas.sh: training pass 11
steps/train_deltas.sh: training pass 12
steps/train_deltas.sh: training pass 13
steps/train_deltas.sh: training pass 14
steps/train_deltas.sh: training pass 15
steps/train_deltas.sh: training pass 16
steps/train_deltas.sh: training pass 17
steps/train_deltas.sh: training pass 18
steps/train_deltas.sh: training pass 19
steps/train_deltas.sh: training pass 20
steps/train_deltas.sh: aligning data
steps/train_deltas.sh: training pass 21
steps/train_deltas.sh: training pass 22
steps/train_deltas.sh: training pass 23
steps/train_deltas.sh: training pass 24
steps/train_deltas.sh: training pass 25
steps/train_deltas.sh: training pass 26
steps/train_deltas.sh: training pass 27
steps/train_deltas.sh: training pass 28
steps/train_deltas.sh: training pass 29
steps/train_deltas.sh: training pass 30
steps/train_deltas.sh: aligning data
steps/train_deltas.sh: training pass 31
steps/train_deltas.sh: training pass 32
steps/train_deltas.sh: training pass 33
steps/train_deltas.sh: training pass 34
steps/diagnostic/analyze_alignments.sh --cmd run.pl data/lang exp/tri1
steps/diagnostic/analyze_alignments.sh: see stats in exp/tri1/log/analyze_alignments.log
1 warnings in exp/tri1/log/init_model.log
35 warnings in exp/tri1/log/update.*.log
267 warnings in exp/tri1/log/align.*.*.log
1324 warnings in exp/tri1/log/acc.*.*.log
1 warnings in exp/tri1/log/build_tree.log
1 warnings in exp/tri1/log/questions.log
exp/tri1: nj=3 align prob=-83.23 over 26.33h [retry=0.5%, fail=0.5%] states=1657 gauss=11031 tree-impr=4.70
steps/train_deltas.sh: Done training system with delta+delta-delta features in exp/tri1

===== TRI1 (first triphone pass) DECODING =====

tree-info exp/tri1/tree
tree-info exp/tri1/tree
fstcomposecontext --context-size=3 --central-position=1 --read-disambig-syms=data/lang/phones/disambig.int --write-disambig-syms=da
ta/lang/tmp/disambig_ilabels_3_1.int data/lang/tmp/ilabels_3_1
fstisstochastic data/lang/tmp/CLG_3_1.fst
0 -0.0490423
[info]: CLG not stochastic.
make-h-transducer --disambig-syms-out=exp/tri1/graph/disambig_tid.int --transition-scale=1.0 data/lang/tmp/ilabels_3_1 exp/tri1/tre
e exp/tri1/final.mdl
fsttablecompose exp/tri1/graph/Ha.fst data/lang/tmp/CLG_3_1.fst
fstdeterminizestar --use-log=true
fstrmepslocal
fstrmsymbols exp/tri1/graph/disambig_tid.int
fstminimizeencoded
fstisstochastic exp/tri1/graph/HCLGa.fst
0.602189 -0.122112
HCLGa is not stochastic
add-self-loops --self-loop-scale=0.1 --reorder=true exp/tri1/final.mdl
steps/decode.sh --config conf/decode.config --nj 3 --cmd run.pl exp/tri1/graph data/test exp/tri1/decode
decode.sh: feature type is delta
steps/diagnostic/analyze_lats.sh --cmd run.pl exp/tri1/graph exp/tri1/decode
steps/diagnostic/analyze_lats.sh: see stats in exp/tri1/decode/log/analyze_alignments.log
Overall, lattice depth (10,50,90-percentile)=(1,2,10) and mean=4.4
steps/diagnostic/analyze_lats.sh: see stats in exp/tri1/decode/log/analyze_lattice_depth_stats.log
exp/tri1/decode/wer_19
%WER 65.88 [ 9664 / 14669, 3992 ins, 132 del, 5540 sub ]
%SER 96.17 [ 1859 / 1933 ]

===== run.sh script is finished =====

root@0cbb1df73518:/usr/local/src/kaldi/egs/paldaruo_welsh# exit

```
