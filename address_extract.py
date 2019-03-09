import pandas as pd
import usaddress
from pandas import DataFrame

data = [''] #unclean address goes here

tagged_addresses = [usaddress.parse(line) for line in data]

address_df = pd.DataFrame(tagged_addresses)

address_df.to_csv('moooutput.csv') #filename