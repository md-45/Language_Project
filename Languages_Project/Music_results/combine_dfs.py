import pandas as pd
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
import matplotlib.pyplot as plt

#Where I add country, region, lang_code, and status to each language

country_codes = 'CountryCodes.tab.txt'
lang_codes = 'LanguageCodes.tab.txt'

csv_cc = 'CountryCodes.csv'
csv_lc = 'LanguageCodes.csv'

delimiter = '\t'

cc_df = pd.read_csv(country_codes, sep=delimiter)
lc_df = pd.read_csv(lang_codes, sep=delimiter)

cc_df.to_csv(csv_cc, index=False)
lc_df.to_csv(csv_lc, index=False)

langs = pd.read_csv('Lang_List.csv', delimiter=';')

all_langs = pd.merge(langs, lc_df, on='Name', how='left')
all_langs_cleaned = all_langs.drop(columns=['Unnamed: 2', 'Unnamed: 3'])

final = all_langs_cleaned.merge(cc_df, on='CountryID', how='left')
final = final.rename(columns={"Name_x": "Language", "Name_y": "Country"})

csv_final = 'All_Lang_Info.csv'
final.to_csv(csv_final, index=False)

data = pd.get_dummies(final)

#Maybe need to conduct feature selection first
#Only need area, family, country
#Transform into principal components
#Consider regression

#Plot the hierarchical clustering as a dendrogram
Z = linkage(data, method='ward')
dendrogram(Z, orientation='left', truncate_mode = 'level', p=5)
plt.show()
labels = fcluster(Z, t=5, criterion='distance')
data['Name'] = labels
print(data)

#Track run time