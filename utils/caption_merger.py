import re

def replace_placeholder(original_caption, replacement):
    return re.sub(r"\b(a|A) (soccer player|man|bald man)\b", replacement, original_caption)
