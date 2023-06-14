"""
Main program text extracter and verifier
"""

import webbrowser
from paddleocr import PaddleOCR
import spacy

# Step 3: Initialize PaddleOCR
ocr = PaddleOCR()

# Step 4: Load your trained NER model using SpaCy
nlp_ner = spacy.load("/home/keerthi/NEW/model-best")
list1 = []


def extract_text_from_image(path):
    """
    Extract text from image
    """
    result = ocr.ocr(path)
    for i in range(len(result[0])):
        line = result[0][i][1][0]
        word = line.split(" ")
        list1.extend(word)
    str1 = " ".join(map(str, list1))
    return str1


def process_text_with_ner(text):
    """
    Process text with ner
    """
    doc = nlp_ner(text)
    return doc


PATH = "/home/keerthi/NEW/images2/3.jpg"
TEXT = extract_text_from_image(PATH)
Processed_doc = process_text_with_ner(TEXT)
print(Processed_doc)

dic = {}
FIRST_NAME = False
for ent in Processed_doc.ents:
    if ent.label_ == "NAME":
        if not FIRST_NAME:
            dic[ent.label_] = ent.text
            FIRST_NAME = True
    else:
        if ent.label_ not in dic:
            dic[ent.label_] = ent.text

print(dic)


def display_in_browser(dictionary):
    """
        To display output in browser
    """
    html_content = f"<html><body><pre>{dictionary}</pre></body></html>"
    with open("dictionary.html", "w", encoding="utf-8") as file_f:
        file_f.write(html_content)
    webbrowser.open_new_tab("dictionary.html")


display_in_browser(dic)
