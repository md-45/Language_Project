import pandas as pd
import random
import webbrowser

mega_lang_df = pd.read_csv("D:/Languages_Project/Languages_Project/mega_lang_list.csv")

#Test incoroporating opening a random link
random_num = random.randrange(len(mega_lang_df))
random_link = mega_lang_df.iloc[random_num]["link"]
webbrowser.open(random_link)

#Filter links to just music
mega_lang_df.head(5)