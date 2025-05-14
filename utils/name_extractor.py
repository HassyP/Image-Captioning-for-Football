import re
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_entity_name(caption: str):
    doc = nlp(caption.strip())
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text

    fallback = re.findall(r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)?\b', caption)
    blacklist = {"With", "At", "For", "From", "In", "On", "And"}
    for name in fallback:
        if not any(word in blacklist for word in name.split()):
            return name

    return "the player"
