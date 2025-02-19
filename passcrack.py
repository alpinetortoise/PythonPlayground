import hashlib

target = "7f67005387f2c0db5c219d935fc425c0"
wordlist = open("./words.txt", "rb")

for word in wordlist:
    word = word.rstrip()
    hashed = hashlib.md5(word).hexdigest()

    if(hashed == target):
        word_string = word.decode()
        print("Password Found: ", word_string)
