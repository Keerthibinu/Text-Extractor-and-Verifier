import spacy
import cv2
from paddleocr import PaddleOCR
from fuzzywuzzy import fuzz

# Load the "en_core_web_lg" model
nlp_lg = spacy.load('./output/model-best')

dictionary = {'Federal Institute Of Science And Technology': '1',
              'Keerthi Binu': '2',
              'FISAT': '3'}

img = cv2.imread('/home/keerthi/img.png')
ocr = PaddleOCR()
result = ocr.ocr(img)

# Process the OCR result
matched_phrases = set()
matched_entities = set()

for i in range(len(result[0])):
    s = result[0][i][1][0]
    l = s.split(" ")
    for word in l:
        for key in dictionary.keys():
            if fuzz.token_set_ratio(word, key) == 100:  # to check similarity ratio
                matched_phrases.add(key)

    doc_lg = nlp_lg(s)
    for ent in doc_lg.ents:
        if ent.text in matched_phrases:
            matched_entities.add((ent.text,ent.label_))

# Print the matched phrases and entities
for phrase in matched_phrases:
    print(f"{phrase} is present")  

for entity,label in matched_entities:
    print(f"{entity} is found with label {label}")
