import numpy as np
import pandas as pd
import openpyxl

def test():
    df = pd.read_excel('datenrandom.xlsx')

    print(df)
    my_array = np.array([[0, 2, 4], [1, 3, 5]])
    np.save('my_array_temp.npy', my_array)
    arbeit=np.load('my_array_temp.npy')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   test()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
