import os
import time
import random


angka = 'test 123'
filename = 'testing.txt'
check_changes = os.popen("git diff {}".format(filename)).read()
# check - is check changes return null value or empty return?
# emptty return means no changes from git diff output
if check_changes == '':
    print('no changes')
else:
    print('changes detected')
    print('prosess commit')
    stagging_git = os.system("git add {}".format(filename))
    commit_git = os.system("git commit -m 'change ke - {}'".format(angka))



filename = 'testing.txt'
angka = 0
while True:
    time.sleep(3) 
    angka += 1
    with open (filename,'w') as file:
        output = "this is {}".format(random.random())
        file.write(output)
    # add file to stagging git
    os.system("git add {}".format(filename))
    # commit that with comments
    os.system("git commit -m 'change ke - {}'".format(angka))