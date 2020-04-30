#!/usr/bin/python3
import os
import random
import time
import sys

print("""\33[92mBing Awards Searcher
Version 2.6
by Oliver Chen, GVH 8, 2019
Programmed 12.28.2019\33[0m""")

if os.name != "posix":
    print("\33[5m\33[1m\33[91mNOTE: THIS PROGRAM MAY NOT PROPERLY RUN ON WINDOWS!!!\nPlease use linux for optimal results.\33[0m")

try:
    try:
        settingsfile = open("BingAwardsSearchCompromiser-v2-settings.txt", 'r')
        for line in settingsfile.readlines():
            exec(line)
    except FileNotFoundError:
        if input("\33[93mA program settings file was not found! Would you like to generate a new one or quit? (leave blank for generate) [Default: ] \33[0m") == '':
            print("Okay, we will now ask you some one-time questions.\nIn the case that you would like to change any of these settings, delete the settings file and re-run the program.\nBy the way, no configuration file will be generated until the end.")
            browserexec = input("\nPlease give us the location of your web browser executable.\nIt will be run with the following syntax: [executable] [URL]. [Default: /opt/google/chrome/chrome] ")
            if browserexec == "":
                browserexec = "/opt/google/chrome/chrome"
            print("\33[93mOkay, to launch the URLs, we will use the following OS.system() command: %s [URL]\nIf you've made a mistake, restart the program now.\33[0m\n" % browserexec)
            englishDictionaryFileName = input("\nPlease give us the location of your english word list (ie. dictionary). [Default: ./english-words.txt] ")
            if englishDictionaryFileName == "":
                englishDictionaryFileName = "./english-words.txt"
            print("\33[93mOkay, to create the URLs, we will use the following dictionary: %s\nIf you've made a mistake, restart the program now.\33[0m\n" % englishDictionaryFileName)
            errortext = "\33[1m\33[43mNo configuration file has been created.\33[0m"
            input("\33[1m\33[5mPlease confirm the creation of the config file!!! KeyboardInterrupt to cancel. \33[0m")
            del errortext
            print('\n', end='')
            settingsfile = open("BingAwardsSearchCompromiser-v2-settings.txt", 'w')
            settingsfile.write("browserexec = '%s'\n" % browserexec)
            settingsfile.write("englishDictionaryFileName = '%s'\n" % englishDictionaryFileName)
        else:
            sys.exit()

    try:
        numberToGenerate = input("\33[93mHow many searches would you like to use? [Default: 30] \33[0m")
        if numberToGenerate == '':
            numberToGenerate = 30
        else:
            numberToGenerate = int(numberToGenerate)
    except ValueError:
        print("\33[91mSorry, that is not a valid number.\33[0m")
        sys.exit()

    try:
        msToWait = input("\33[93mApproximately how much time (ms) would you like to allocate to webpage-loading? [Default: 500] \33[0m")
        if msToWait == '':
            msToWait = 500
        else:
            msToWait = int(msToWait)
    except ValueError:
        print("\33[91mSorry, that is not a valid time.\33[0m")
        sys.exit()

    print("Reading the english dictionary...")
    englishDictionary = open(englishDictionaryFileName).readlines()
    print("Generating wordlist...")
    URLList = []
    print("Generating URLs...")
    for i in range(1, (numberToGenerate + 1)):
        URL = ("https://www.bing.com/search?q=define+%s&PC=U316&FORM=CHROMN" % englishDictionary[random.randint(0, (len(englishDictionary)))].strip())
        print("URL #%i: \33[4m%s\33[0m" % (i, URL))
        URLList.append(URL)
    errortext = "\33[0m"
    print("\33[90m")
    for URL in URLList:
        os.system((browserexec + " %s") % URL)
        thisMsToWait = random.randint(round(msToWait*0.75), round(msToWait*1.25))
        print("\33[35mNow waiting %ims before next request.\33[90m" % thisMsToWait)
        time.sleep(thisMsToWait/1000)
    print("\33[0m", end="")
    del errortext
except KeyboardInterrupt:
    print("\33[91m\nKeyboardInterrupt\33[0m")
    try:
        print(errortext)
    except NameError:
        pass
finally:
    print("\33[92mThank you for using Bing Awards Search Compromiser by Oliver Chen, GVH 8, 2019\33[0m")
