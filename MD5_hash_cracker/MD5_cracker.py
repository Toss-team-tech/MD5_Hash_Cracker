import hashlib

pass_hash = input('Enter MD5 hash ')
wordlist = input("Enter the file name: ")

try:
    pass_file = open(wordlist, "r")
except:
    print("No file found")
    quit()

for word in pass_file:
     
     enc_wrd = word.encode('utf-8')
     digest = hashlib.md5(enc_wrd.strip()).hexdigest()

     if digest == pass_hash:
         print("Password has been found")
         print("password is " + word)
         flag = 1
         break

if flag == 0:
    print("password/passphrase is not in the list")