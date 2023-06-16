"""
Main program text extracter and verifier
"""

import webbrowser
import glob
from paddleocr import PaddleOCR
import spacy

# Step 3: Initialize PaddleOCR
ocr = PaddleOCR()

# Step 4: Load your trained NER model using SpaCy
nlp_ner = spacy.load("./model-best")


def extract_text_from_images(paths):
    """
    Extract text from images
    """
    list1 = []
    for i in paths:
        result = ocr.ocr(i)
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


def display_in_browser(result):
    """
    To display output in browser
    """
    html_content = "<html><body>"
    for i, dictionary in enumerate(result):
        html_content += f"<h2>Image {i+1}</h2>"
        html_content += f"<pre>{dictionary}</pre>"
    html_content += "</body></html>"

    with open("dictionary.html", "w", encoding="utf-8") as file_f:
        file_f.write(html_content)
    webbrowser.open_new_tab("dictionary.html")


PATH = "./trained_img/"
image_paths = glob.glob(PATH + "*.png") + glob.glob(PATH + "*.jpeg")
image_paths += glob.glob(PATH + "*.jpg")

results = []
for path in image_paths:
    TEXT = extract_text_from_images([path])
    Processed_doc = process_text_with_ner(TEXT)
    dic = {}
    FIRST_NAME = False
    for ent in Processed_doc.ents:
        if ent.label_ == "NAME":
            if not FIRST_NAME:
                dic[ent.label_] = ent.text
                FIRST_NAME = True
        else:
            dic[ent.label_] = ent.text
    results.append(dic)

display_in_browser(results)
