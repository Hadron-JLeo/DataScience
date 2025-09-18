from random import randint
import pandas as pd

#ID,Zeit,EmailGegeben,NutzerMerkmal (IP),Land,Email

NAME = ['Tom', 'Dagobert', 'John', 'Leo']

ID =     []
Zeit =   []
EmailG = []
IP =     []
Land =   []
Email =  []


num_rows = range(0,100)


for i in num_rows:
  my_time = f'{randint(1,30)}/{randint(1,12)}/2025'
  ID.append(i)
  Zeit.append(my_time)


print(Zeit)

df = pd.DataFrame({ 'ID':ID,
                     'Datum': Zeit })

df
