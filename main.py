"#AutoNotes" 
import os
import sys
from datetime import date, datetime

name = str(sys.argv[1])
date = str(date.today())
month = datetime.now().strftime('%b')
type = str(sys.argv[2])
path = os.environ.get('Notes')          #Add path to notes to ENV
#_dir = path + '/' + month

commands = [f'echo # {name} - {date} >> {name}.{type}',
          f'{name}.{type}']

#os.mkdir(_dir)
os.chdir(path)

for c in commands:
     os.system(c)
