# -*-  coding: utf-8 -*-
import urllib

def main(f):
    lines = f.readlines()
    i = 0
    for line in lines:
        print " downloading  "+ "第"+str(i)+"张"
        urllib.urlretrieve(line,'%s.jpg'%i)
        i =  i + 1

if __name__ == "__main__":
    f = open('menu.txt','r')
    main(f)
    f.close()



