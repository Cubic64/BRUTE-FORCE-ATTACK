import zipfile
import time

folderpath = input("folder path..")
zipf = zipfile.ZipFile(folderpath)
global result
result = 0
global tried
tried = 0
c = 0

if not zipf:
    print('Could not open the file as a zip archive')
else:
    starttime = time.time()
    wordlistFile = open('wordlist.txt', 'r', errors = 'ignore')
    body = wordlistFile.read().lower()
    words = body.split('\n')

for i in range(len(words)):
    word = words[i]
    password = word.encode('utf8').strip()
    c = c+1
    print('Trying to decode password by: {}'.format(word))
    try:
        with zipfile.ZipFile(folderpath,'r') as zf:
            zf.extractall(pwd=password)
            print("Success! The password is: "+ word)
            endtime = time.time()
            result = 1
        break
    except:
        pass