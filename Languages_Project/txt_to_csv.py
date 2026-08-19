import pandas as pd

country_codes = 'CountryCodes.tab.txt'
lang_codes = 'LanguageCodes.tab.txt'
lang_index = 'LanguageIndex.tab.txt'

csv_cc = 'CountryCodes.csv'
csv_lc = 'LanguageCodes.csv'
csv_li = 'LanguageIndex.csv'

delimiter = '\t'

cc_df = pd.read_csv(country_codes, sep=delimiter)
lc_df = pd.read_csv(lang_codes, sep=delimiter)
li_df = pd.read_csv(lang_index, sep=delimiter)

cc_df.to_csv(csv_cc, index=False)
lc_df.to_csv(csv_lc, index=False)
li_df.to_csv(csv_li, index=False)

