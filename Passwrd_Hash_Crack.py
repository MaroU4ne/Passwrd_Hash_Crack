import hashlib

flag = False
hash = input("\n *Enter a SHA256 hash: ")
file = input("\n ***Enter a Passord listFile: ")

try:
    readFile = open(file, 'r')
    readFile.read()
except:
    print ("\n\t [!] No such File !")

for password in readFile:
    enc_wrd = password.encode("utf-8")
    digest = hashlib.sha256(enc_wrd.strip()).hexdigest()

    print(digest)
    print(hash)
    print(password)

    if digest == hash:
        print("\n\t [+] Password Found >>>", password)
        flag = True
        break
if not flag:
    print("\n\t [!] Password Not Found !!!")
    break
