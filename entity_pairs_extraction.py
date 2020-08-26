import spacy

nlp = spacy.load('en_core_web_sm')

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
                if prev_tok_dep == "compound":
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

print(get_entities("The film had 200 patents."))

