# Import Auxiliary Tools
import tqdm as tqdm

# Import Text
coating_2500 = "An ultra-low DFT advanced coating system targeted for refinery crude unit and FCC slurry fouling by enhancing tube lubricity and reducing surface tension. Curran 2500 is designed for high temperature DCU, VDU and FCCU crude services, and can be applied to tube exchangers, P&F exchangers and distillation tower components. In independent lab testing this coating has exhibited excellent anti-fouling and anti-coking performance, and is resistant to thermal cycling. Designed to withstand extreme temperatures up to 1200°F. May be applied to heat exchanger tubes, plate & frame exchangers, tube sheets, channels, exchanger components and crude heaters. Can be applied in-situ."
coating_1500 = "Curran 1500 is an advanced two part (100% solids) epoxy coating designed specifically for high temperature immersion service in water, hydrocarbons, and process streams (up to 365 F, 185 C). This coating is an organic/inorganic hybrid, is suitable for immersion services subjected to “cold wall” exposure, and is machinable when fully cured. Can withstand multiple cycling and steam out events subjected to process equipment."

import spacy
nlp = spacy.load('en_core_web_sm')

doc_2500 = nlp(coating_2500)
doc_1500 = nlp(coating_1500)

for i in doc_2500.sents:
    print(i)

for i in doc_2500.sents:
    for tok in nlp(str(i)):
        if tok.dep_.find("subj") == True:
            print("SUBJ:", tok.dep_.text)

def get_entities(sent):
    # Defining empty varibales
    ent1 = ""
    ent2 = ""

    # Defining empty varibales that will hold the
    # dependency tag fo the previous word in the sentence.
    prv_tok_dep = "" 
    prv_tok_text = "" # previous token in sentence

    # These will hold the text that is associated with the 
    # subject or object
    prefix = "" 
    modifier = ""

    for tok in nlp(sent):
        # -- This part we are building the prefix/modifier
        # that will go into a node -- 
        # if token is a punctuation mark then move on
        if tok.dep_ != "punct":
            # check: token is a compound or not
            if tok.dep_ == "compound":
                prefix = tok.text
                # if the previous word was also a 'compound'
                # then add the current word to it.
                if prv_tok_dep == "compound":
                    prefix = prv_tok_text + " " + tok.text
            # check: token is a modifier or not
            if tok.dep_.endswith("mod") == True:
                modifier = tok.text
                # if the previous word was also a 'compound'
                # then add the current word to it
                if prv_tok_dep == "compound":
                    modifier = prv_tok_text + " " + tok.text

            # 3
            # check: token is subject of sentence
            if tok.dep_.find("subj") == True:
                # build entitiy with prefixes and modifiers
                ent1 = modifier + " " + prefix + " " + tok.text
                # free up new empty prefixes and modifiers
                prefix = ""
                modifier = ""
                prv_tok_dep = ""
                prv_tok_text = ""
            
            # check if tok is DO, if it is then it will be related
            # to the other entity
            if tok.dep_.find("obj") == True:
                # build entity
                ent2 = modifier + " " + prefix + " " + tok.text

            # 5
            # update variables
            prv_tok_dep = tok.dep_
            prv_tok_text = tok.text

    return [ent1.strip(), ent2.strip()]

entity_pairs = []

for i in doc_2500.sents:
    entity_pairs.append(get_entities(str(i)))

print(entity_pairs)