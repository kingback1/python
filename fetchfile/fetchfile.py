#coding:utf-8

import os
import time
import shutil

def getnamelist():
    file = open('name.txt', 'r')
    names = file.readlines()
    name_list = []

    for name in name_list:
        name = name.strip()
        name_list.append(name)

    file.close()
    return name_list

def readfolder():
    fl = os.listdir(".")
    return fl

def classfile(files, names, filepath):
    logf = open('log.txt', "a")
    localtime = time.asctime(time.localtime(time.time()))
    logf.write(localtime)
    logf.write('\r\n')

    for f in files:
        for n in names:
            if not -1 == f.find(n):
                info = "find %s, copy %s to %s \r\n" % (n, f, filepath)
                print info
                logf.write(info)
                shutil.copy(f, filepaht)
    logf.close()

if __name__=='__main__':

    if not os.path.exists("result"):
        os.makedirs("result")
        filepath = "./result"
    else:
        print "error! result folder is already exists"
        sys.exit()

    names = getnamelist()
    fs = readfolder()
    exitlist = ['names.txt', 'fetchfile.py', 'log.txt', 'result']
    files = list(set(fs) - set(exitlist))

    classfile(files, names, filepath)







    