@echo off 
set "offsets=20x0 14x14 0x20 -14x14 -20x0 -14x-14 0x-20 14x-14"
::for %%i in (%offsets%) do call mouse moveBy %%i
set "offsets=0x-20 0x-20 15x15 15x-15 0x20 0x20 0x-20 0x-20 -15x15 -15x-15 0x20 0x20"
rundll32 user32.dll,SetCursorPos
call mouse moveBy -50x-50
for %%i in (%offsets%) do call mouse moveBy %%i
for %%i in (%offsets%) do call mouse moveBy %%i
for %%i in (%offsets%) do call mouse moveBy %%i

