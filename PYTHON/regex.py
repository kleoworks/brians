import re

def get_matching_words(regex):

    words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

    return [word for word in words if re.search(regex, word)]



v = get_matching_words(r'[v]')
ss = get_matching_words(r'(ss)')
end_e = get_matching_words(r'\w+e$')
b_any_b = get_matching_words(r'\w*[b]\w*[b][\w]*')
b_one_b = get_matching_words(r'\w*[b]\w+[b][\w]*')
aeiou = get_matching_words(r'[^aeiou ]*[a][^iou ]*[e][^aeou ]*[i][^aeiu ]*[o][^aeio ]*[u]\w*')
regex = get_matching_words(r'\b[regulaxpsion]+\b')
doubles = get_matching_words(r'\w*([a-z])\1\w*')
print doubles
