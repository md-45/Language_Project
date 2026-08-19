import random
import math
import pandas as pd
import numpy as np

langs = pd.read_csv('Lang_List.csv', delimiter=';')
langs_list = langs.values.tolist()
new_langs_list = []
for x in np.arange(len(langs_list)):
    if len(langs_list) >= 0:
        print(len(langs_list))
        choose = random.randrange(len(langs_list))
        new_value = str(langs_list[choose])
        clean_value = new_value.strip("['']")
        new_langs_list = new_langs_list + [clean_value]
        langs_list.pop(choose)