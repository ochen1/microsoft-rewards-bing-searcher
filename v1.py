#!/usr/bin/python3
import os
import random
import time

print("""\33[92mBing Rewards Searcher
Version 1.1
by Oliver Chen, GVH 8, 2019
Last modified 12.28.2019\33[0m""")

if os.name != "posix":
    print("\33[5m\33[1m\33[91mNOTE: THIS PROGRAM MAY NOT PROPERLY RUN ON WINDOWS!!!\nPlease use linux for optimal results.\33[0m")

try:
    try:
        numberToGenerate = input("\33[93mHow many searches would you like to use? [Default: 30] \33[0m")
        if numberToGenerate == '':
            numberToGenerate = 30
        else:
            numberToGenerate = int(numberToGenerate)
    except ValueError:
        print("\33[91mSorry, that is not a valid number.\33[0m")
        exit()

    try:
        msToWait = input("\33[93mHow much time (ms) would you like to allocate to webpage-loading? [Default: 250] \33[0m")
        if msToWait == '':
            msToWait = 250
        else:
            msToWait = int(msToWait)
        msToWait = msToWait / 1000
    except ValueError:
        print("\33[91mSorry, that is not a valid time.\33[0m")
        exit()

    print("Reading the english dictionary...")
    englishDictionary = open("english-words.txt").readlines()
    print("Generating wordlist...")
    URLList = []
    print("Generating URLs...")
    for i in range(1, (numberToGenerate + 1)):
        URL = ("https://www.bing.com/search?q=define+%s&PC=U316&FORM=CHROMN" % englishDictionary[random.randint(0, (len(englishDictionary)))].strip())
        print("URL #%i: \33[4m%s\33[0m" % (i, URL))
        URLList.append(URL)
    for URL in URLList:
        os.system("/opt/google/chrome/chrome %s" % URL)
        time.sleep(msToWait)
except KeyboardInterrupt:
    print("\33[91m\nKeyboardInterrupt\33[0m")
finally:
    print("\33[92mThank you for using Bing Awards Search Compromiser by Oliver Chen, GVH 8, 2019\33[0m")
