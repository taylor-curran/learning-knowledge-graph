import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_sm')

doc = nlp("The 22-year-old recently won ATP Challenger.")

for tok in doc:
    print(tok.text, "...", tok.dep_)

# Extract the subject/object along with its modifiers, 
# compound words and also extract the punctuation marks between them.

# We will use dependency parsing to extract entities.

# displacy.serve(doc, style="dep")

doc = nlp("Nagal won the first set.")

for tok in doc:
  print(tok.text, "...", tok.dep_)