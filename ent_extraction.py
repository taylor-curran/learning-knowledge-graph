import spacy
nlp = spacy.load('en_core_web_sm')

doc = nlp("The 22-year-old recently won ATP Challenger.")

for tok in doc:
    print(tok.text, "...", tok.dep_)