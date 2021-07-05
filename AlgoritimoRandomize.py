#Criado para randomizar uma lsita de 20mil Colaboradores retornando apenas 1000 colaboradores vários cargos distintos.
import pandas as pd

import random

base = pd.read_excel("usuarios - energisa.xlsx", encoding="ISO-8859-1",error_bad_lines=False)

sort1 = base.sample(15000)

sort2 = sort1.sample(10000)

sort3 = sort2.sample(7500)

sort4 = sort3.sample(5000)

sort5 = sort4.sample(2500)

sorteado = sort5.sample(1000)

sorteado.to_excel("Lista Randomizada.xlsx")
