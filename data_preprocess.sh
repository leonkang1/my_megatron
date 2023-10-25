python tools/preprocess_data.py \
       --input datasets/fake_dataset.txt \
       --output-prefix my-gpt2 \
       --vocab-file gpt_nlp_files/vocab.json \
       --tokenizer-type GPT2BPETokenizer \
       --merge-file gpt_nlp_files/merges.txt \
       --append-eod \
       --workers 4