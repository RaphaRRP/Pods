import pandas as pd
import os

def converter():
    folder = "converter"
    output_folder = "convertido"
    for count, filename in enumerate(os.listdir(folder)):
        read_file = pd.read_excel(os.path.join(folder,filename))
        read_file.to_csv(os.path.join(output_folder,str('dados') + str('.csv')), index = None, header=True)

    print('convertido para csv')