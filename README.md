# alaa
Dataset link: https://huggingface.co/datasets/iradukunda-dev/offences_and_penalties_in_general_2018_dataset

Model link: https://huggingface.co/iradukunda-dev/law-finetuned-DeepSeek-R1-Distill-Qwen-7B


# How to build dataset
- Download the official gazette and add it to the `~/data/raw`
- Activate venv and install requirements txt.
- The execute:
```:bash
python utils/data_cleanup.py
```
