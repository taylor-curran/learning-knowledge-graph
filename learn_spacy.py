coating_2500 = "An ultra-low DFT advanced coating system targeted for refinery crude unit and FCC slurry fouling by enhancing tube lubricity and reducing surface tension. Curran 2500 is designed for high temperature DCU, VDU and FCCU crude services, and can be applied to tube exchangers, P&F exchangers and distillation tower components. In independent lab testing this coating has exhibited excellent anti-fouling and anti-coking performance, and is resistant to thermal cycling. Designed to withstand extreme temperatures up to 1200°F. May be applied to heat exchanger tubes, plate & frame exchangers, tube sheets, channels, exchanger components and crude heaters. Can be applied in-situ."
coating_1500 = "Curran 1500 is an advanced two part (100% solids) epoxy coating designed specifically for high temperature immersion service in water, hydrocarbons, and process streams (up to 365 F, 185 C). This coating is an organic/inorganic hybrid, is suitable for immersion services subjected to “cold wall” exposure, and is machinable when fully cured. Can withstand multiple cycling and steam out events subjected to process equipment."

# Import English Language Class
from spacy.lang.en import English

# Create NLP Object
nlp = English()

# Process a string of text with the nlp object
doc_2500 = nlp(coating_2500)
doc_1500 = nlp(coating_1500)

# Iterate over tokens in a Doc
# for token in doc_1500:
#     print(token.text)

span = doc_2500[:56]
print(span)

# print([token.like_num for token in doc_2500])

import spacy

# Load English Model
nlp = spacy.load("en_core_web_sm")

doc = nlp(str(span))

for token in doc:
    # Print the text and the predicted part-of speech tag
    print(token.text, token.pos_, token.dep_, token.head.text)