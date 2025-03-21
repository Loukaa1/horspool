from horspool import naive_search, shift, search

#   +---------------------------------------------------+
#   |                     TESTS                         |
#   +---------------------------------------------------+

DATAS_SEARCH = (
    # TEXT          PATTERN         CASE_SENSITIVE  EXPECTED
    ("text",        "texto",        True,           []),
    ("text",        "text",         True,           [0]),
    ("Text",        "text",         True,           []),
    ("le text",     "text",         True,           [3]),
    ("xt text text","text",         True,           [3,8]),
    ("text text te","text",         True,           [0,5]),
    ("TexT tEXt te","tExt",         False,          [0,5]),
)

#   ------NAIVE_SEARCH-------------
for text, pattern, case_sensitive, expected in DATAS_SEARCH:
    result = naive_search(text, pattern, case_sensitive=case_sensitive)
    assert expected==result, f"La recherche naïve de '{pattern}' dans '{text}', (case_sensitive = {case_sensitive}) aurait du être {expected} mais c'est {result}."

#   ------SHIFT----------------------
PATTERN = "aBcdCba"
DATAS_SHIFT = (
    # PATTERN         CASE_SENSITIVE  EXPECTED
    (PATTERN,         True,           {'a': 6, 'B': 5, 'c': 4, 'd': 3, 'C': 2, 'b': 1}),
    (PATTERN.lower(), True,           {'a': 6, 'b': 1, 'c': 2, 'd': 3}),
    (PATTERN.title(), True,           {'A': 6, 'b': 1, 'c': 2, 'd': 3}),
    (PATTERN,         False,          {'A': 6, 'B': 1, 'C': 2, 'D': 3}),
)
for pattern, case_sensitive, expected in DATAS_SHIFT: 
    result = shift(pattern, case_sensitive=case_sensitive)
    assert expected==result, f"Le motif '{pattern}' (case_sensitive={case_sensitive}) devrait donner {expected}"
    
    
#   --------SEARCH-------------
for text, pattern, case_sensitive, expected in DATAS_SEARCH:
    result = search(text, pattern, case_sensitive=case_sensitive)
    assert expected==result, f"La recherche de '{pattern}' dans '{text}', (case_sensitive = {case_sensitive}) aurait du être {expected} mais c'est {result}."
    
    
roman_file = open("le_meilleur_des_mondes.txt","r",encoding='utf8')
roman = roman_file.read()
data = roman.replace('\n', ' ')
motif = 'marsien'
results = naive_search(roman, motif, case_sensitive=False)
print(len(results))
for result in results :
    print(data[result-10:result+len(motif)+10])

    