"#AutoNotes" 
import os
import sys
from datetime import date

name = str(sys.argv[1])
date = str(date.today())
type = "txt"
_dir = "C:\Users\Johannes\progs\AutoNotes\Notes"

commands = [f'echo "# {name} - {date}" >> {name}.{type}',
          f'{name}.{type}']

os.chdir(_dir)

for c in commands:
     os.system(c)
