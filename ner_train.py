"""
Code to train ner model

! python3 -m spacy init config config.cfg --lang en
--pipeline ner --optimize efficiency
! python3 -m spacy train config.cfg --output ./ --paths.train
./training_data.spacy --paths.dev ./training_data.spacy
"""
import json
import spacy
from spacy.tokens import DocBin
from tqdm import tqdm

nlp = spacy.blank("en")  # load a new spacy model
db = DocBin()  # create a DocBin object

with open('final.json', 'r', encoding='utf-8') as f:
    TRAIN_DATA = json.load(f)

for text, annot in tqdm(TRAIN_DATA['annotations']):
    doc = nlp.make_doc(text.strip())
    ents = []
    for start, end, label in annot["entities"]:
        span = doc.char_span(start, end, label=label,
                             alignment_mode="contract")
        if span is None:
            print("Skipping entity")
        else:
            ents.append(span)
    doc.ents = ents
    db.add(doc)
db.to_disk("./training_data.spacy")  # save the docbin object
