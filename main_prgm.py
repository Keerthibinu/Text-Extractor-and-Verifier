"""
Main program text extracter and verifier
"""

import re
import webbrowser
from paddleocr import PaddleOCR
import spacy

# Step 3: Initialize PaddleOCR
ocr = PaddleOCR()

# Step 4: Load your trained NER model using SpaCy
nlp_ner = spacy.load("./model-best")
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


PATH = "img.jpeg"
TEXT = extract_text_from_image(PATH)
Processed_doc = process_text_with_ner(TEXT)
print(Processed_doc)

dic = {}
college = ["fisat", "federal institute of science and technology"]
FIRST_NAME = False
for ent in Processed_doc.ents:
    if ent.label_ == "NAME":
        if not FIRST_NAME:
            dic[ent.label_] = ent.text
            FIRST_NAME = True
    elif ent.label_ == "INSTITUTE":
        if ent.text.lower() in college:
            dic[ent.label_] = "FISAT"
        else:
            dic["HOST"] = ent.text
            dic.pop("INSTITUTE", 0)
    else:
        if ent.label_ not in dic:
            dic[ent.label_] = ent.text
print(dic)


def display_in_browser(dictionary):
    """
    Display output in the browser
    """
    formatted_dict = str(dictionary).replace('{', '').replace('}', '')
    formatted_dict = re.sub(r"',\s*'", "',\n'", formatted_dict)
    html_content = f"<html><body><pre><span style='font-size: 20px;'>{formatted_dict}</span></pre></body></html>"
    with open("dictionary.html", "w", encoding="utf-8") as file_f:
        file_f.write(html_content)
    webbrowser.open_new_tab("dictionary.html")


display_in_browser(dic)
