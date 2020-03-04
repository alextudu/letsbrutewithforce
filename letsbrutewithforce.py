#!/usr/bin/python3.5
#Shoutout to Rohan Chavan for helping me create this script. Great explaination. Do visit, https://www.secjuice.com/bruteforcing-with-python/
# The script is a just 25 line python code

#request package to get resquests from the url and sys package to send arugments from commandline
import requests
import sys
import time

#The script takes 3 inputs which are url of the target, path of wordlist and extension of the file
url_target = sys.argv[1]
word_book = sys.argv[2]
exte = sys.argv[3]

#In roder to read wordlist, the following commands helps to open the wordlist and reads the data
letsopen = open(word_book, "r+")

def write(wordperline):
    f1 = open("newlist.txt", "a")
    f1.write(wordperline + "\n")

"""
The following loop code is the soul of the program,
1) Starts index at 0 till given range to calculate worlist's lines as per range.
2)Each index will input word at each line and store in a variable.
3)Concatinate with the URL.
4)Set response code to 200.
"""

for i in range(2000):
    wordperline = letsopen.read(10).strip()
    new_url = url_target+wordperline+exte
    response = requests.get(new_url)
    if (response.status_code == 200):
        print("[+] found Code 200 :-", new_url)
        write(wordperline)
    if (response.status_code == 404):
        print("[+] found Code 404 :-", new_url)
        write(wordperline)

    else:
        print("[-] Not found : - ", new_url)
        pass

