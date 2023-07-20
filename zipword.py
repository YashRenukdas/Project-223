import zipfile
import time

folderpath = input('Path to the file: ')
zipf = zipfile.ZipFile(folderpath)

global result
result = 0

global tried
tried = 0
c = 0

if not zipf:
    print('The zipped file/folder is not password protected, you can successfully open it!')

else:

    startTime = time.time()
    wordListFile = open('wordlist.txt', 'r', errors= 'ignore')

    body = wordListFile.read().lower()
    words = body.split('\n')

    for i in range(len(words)):

        word = words[i]
        password = body.encode('utf8').strip()
        c=c+1

        print("Trying to decode password by: {}".format(word))

        try:

            with zipfile.ZipFile(folderpath, 'r') as zf:

                zf.extractall(pwd = password)
                print("Success! The password is: "+word)

                endTime = time.time()
                result = 1

            break
        except:
            pass

duration = endTime - startTime

if(result == 0):
    print("Sorry, password not found. A total of "+str(c)+"+ possible combinations tried in "+str(duration)+". Password is not of 4 characters.")

else:
    print("Congratulations! Password is found after trying "+str(c)+" combinations in "+str(duration)+" seconds.")