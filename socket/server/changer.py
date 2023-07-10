import time
import shutil

a=1
while True:
    a=a^1
    if a==1:
        shutil.copy('server-file1.png', 'server-file.png')
    else:
        shutil.copy('server-file2.png', 'server-file.png')
    #print(a)
    time.sleep(0.1)
