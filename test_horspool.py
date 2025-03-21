from horspool import naive_search

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
    assert expected==result, f"La recherche naïve de '{pattern}' dans '{text}' aurait du être {expected} mais c'est {result}."
