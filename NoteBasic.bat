@echo off

set name=%1

mkdir Notes
cd Notes
echo # %name% >> %name%.txt
%name%.txt
cd ..
