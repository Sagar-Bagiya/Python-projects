import spacy
nlp = spacy.load('en_core_web_sm')

Interrogative_Sent_keyword = ["what", "why", "when", "where", "whom", "whose", "which","how",
                            "am","is","are",
                            "name", "do", "does", 
                            "could", "would","should",
                            "has", "have", "don't"]


def Query_analysis(query):

    tokens = nlp(query)
    
    poss = [token.pos_ for token in tokens]
    tags = [token.tag_ for token in tokens]
    result = []
    verb = []
    noun = []
    sent_type = ""

    for token, pos, tag in zip(tokens,poss,tags):
        if pos == 'VERB' or pos == 'ADJ':
            verb.append(token)
        elif pos == 'NOUN' or pos == 'PROPN' :
            noun.append(token)
        # print(token,pos,tag)

    if (poss[0] == "AUX") or any(x in tokens[0].text for x in Interrogative_Sent_keyword) or (tokens[-1].text == "?"):
        sent_type = "Interrogative"
        # print("This is a question!")

    elif poss[0] == "VERB" or poss[0] == "PROPN" or poss[0] == "ADJ":
        sent_type = "command"

    elif poss[0] == "INTJ" :
        sent_type = "udagar"

    else : return "no idea"

    result.append(verb)
    result.append(noun)
    result.append(sent_type)
    
    return result


# print(Query_analysis('open notepad'))


# Types of Sentences

# Declarative Sentence
# Imperative Sentence
# Interrogative Sentence
# Exclamatory Sentence

#1) Interrogative Sentence
# Common linking verbs are is, are, am, and any form of the verb “to be.” Often, these verbs will begin the question