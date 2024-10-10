import re
from os import walk

for root, dirs, files in walk('data/news/'):
    if len(dirs) == 0:
        for filename in files:
            fp = f'{root}/{filename}'
            with open(fp, 'r') as file:
                file_content = u' '.join(file.readlines())
                stripped_file = re.sub(r'[^\u0900-\u097F ">;:\.\',!\?\-\(\)\{\}\[\]%&\+\*]+', '', file_content)
            with open(fp, 'w') as file:
                file.write(stripped_file)
            
