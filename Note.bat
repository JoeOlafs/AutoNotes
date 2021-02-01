@echo off

set name=%1
set type=%2

cd progs
cd AutoNotes
python main.py %name% %type%

cd ..
cd ..
