import timeit

SETUP_CODE = """
from horspool import naive_search, search, shift
roman_file = open("le_meilleur_des_mondes.txt","r",encoding='utf8')
roman = roman_file.read()
data = roman.replace('\\n', ' ')
pattern = "En trois autres points, leur physiologie différait étrangement de la nôtre. Leurs organismes ne dormaient jamais, pas plus que ne dort le cœur de l’homme. Puisqu’ils n’avaient aucun vaste mécanisme musculaire à récupérer, ils ignoraient le périodique retour du sommeil. Ils ne devaient ressentir, semble-t-il, que peu ou pas de fatigue. Sur la terre, ils ne purent jamais se mouvoir sans de grands efforts et cependant ils conservèrent jusqu’au bout leur activité. En vingt-quatre heures, ils fournissaient vingt-quatre heures de travail, comme c’est peut-être le cas ici-bas avec les fourmis."
"""

TEST_NAIVE_CODE = """
naive_search(data, pattern, case_sensitive=False)"""

TEST_HORSPOOL_CODE = """
search(data, pattern, case_sensitive=False)"""

number = 10
naive_delay = timeit.timeit(setup=SETUP_CODE,
                          stmt=TEST_NAIVE_CODE,
                          number=number)


horspool_delay = timeit.timeit(setup=SETUP_CODE,
                          stmt=TEST_HORSPOOL_CODE,
                          number=number)

print(f'Naive search time: {naive_delay}')
print(f'Horspool search time: {horspool_delay}')
