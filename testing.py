import os
import time


filename = 'testing.txt'
angka = 0
while True:
    time.sleep(3) 
    angka += 1
    with open (filename,'a') as file:
        output = "halo{}\n".format(angka)
        file.write(output)
    os.system("git add {}".format(filename))
    os.system("git commit -m 'change ke - {}'".format(angka))