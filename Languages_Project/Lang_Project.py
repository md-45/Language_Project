import pandas as pd
import numpy as np
import random

#DF approach

langs = pd.read_csv('Lang_List.csv', delimiter=';')
num_langs = langs.shape[0]
print(num_langs)

langs = langs.drop(["Unnamed: 2", "Unnamed: 3"], axis=1)

choose = random.randint(1, num_langs)
chosen_lang = langs.iloc[choose]

print(langs["Name"])

'''
Recursive approach
def lang_selector(lst):
    #num_langs = len(lst)
    new_lst = []
    #print(num_langs)
    if not lst:
        return []
    else:
        choose = random.randrange(len(lst))
        #print(lst[choose])
        new_lst = new_lst.append(lst[choose])
        lst.pop(choose)
        #num_langs = len(lst)
        #print(num_langs)
        return lang_selector(lst)


langs = pd.read_csv('Lang_List.csv', delimiter=';')
langs_list = langs.values.tolist()

lang_selector(langs_list)
print(new_lst)
'''

'''
For loop
langs = pd.read_csv('Lang_List.csv', delimiter=';')
langs_list = langs.values.tolist()
new_langs_list = []
for x in np.arange(len(langs_list)):
    if len(langs_list) >= 0:
        choose = random.randrange(len(langs_list))
        new_value = str(langs_list[choose])
        clean_value = new_value.strip("['']")
        new_langs_list = new_langs_list + [clean_value]
        langs_list.pop(choose)
'''

'''
List Comprehension
langs = pd.read_csv('Languages_Project\Lang_List.csv', delimiter=';')
langs_list = langs.values.tolist()
new_langs_list = [str(langs_list.pop(random.randrange(len(langs_list)))).strip("['']") for _ in range(len(langs_list))]
print(new_langs_list)
'''

#Dendrogram

#References
#https://www.ethnologue.com/browse/names/
