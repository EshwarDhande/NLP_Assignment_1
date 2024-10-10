import pandas as pd
from os import walk

list_of_data = []

count = 0

for root, dirs, files in walk('data/'):
    if len(dirs) == 0:
        for filename in files:
            fp = f'{root}/{filename}'
            with open(fp, 'r') as file:
                file_content = u' '.join(file.readlines())
                list_of_data.append([root.split('/')[-1], filename, file_content])
                count += 1
            print(count)

df = pd.DataFrame(list_of_data, columns=['source', 'filename', 'contents'])
df.to_csv('mukul_data.csv')
            
