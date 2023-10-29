import hashlib
import binascii
import random

#Part 1 Code
'''
words = [line.strip().lower() for line in open('words.txt')]

wordHash = dict()
for word in words:
    hasher = hashlib.sha256(word.encode('utf-8'))
    digest_as_hex_string = binascii.hexlify(hasher.digest()).decode('utf-8')
    wordHash[digest_as_hex_string] = word

passwordHash = [line.strip().split(':',2) for line in open('passwords1.txt')]

with open('cracked1.txt','w') as writer:
    for userpass in passwordHash:
        writer.writelines(userpass[0] + ':' + wordHash[userpass[1]] + '\n')
'''
        
#Part 2 Code
'''
words = [line.strip().lower() for line in open('words.txt')]

passwordHash = [line.strip().split(':',2) for line in open('passwords2.txt')]

hashcount = 0

while not words == [] and not passwordHash == []:
    with open('cracked2.txt','a') as writer:
        currentWord = random.choice(words)

        wordHash = dict()
        for otherWord in words:
            hasher1 = hashlib.sha256((currentWord + otherWord).encode('utf-8'))
            hasher2 = hashlib.sha256((otherWord + currentWord).encode('utf-8'))
            hashcount += 2
            digest_as_hex_string1 = binascii.hexlify(hasher1.digest()).decode('utf-8')
            digest_as_hex_string2 = binascii.hexlify(hasher2.digest()).decode('utf-8')
            wordHash[digest_as_hex_string1] = (currentWord + otherWord)
            wordHash[digest_as_hex_string2] = (otherWord + currentWord)

        for userpass in passwordHash:
            if userpass[1] in wordHash.keys():
                writer.writelines(userpass[0] + ':' + wordHash[userpass[1]] + '\n')
                passwordHash.remove(userpass)
        
        words.remove(currentWord)
        print(hashcount)
'''

#Part 3 Code
words = [line.strip().lower() for line in open('words.txt')]

passwordHash = [line.strip().split(':',2) for line in open('passwords3.txt')]

hashcount = 0

for userpass in passwordHash:
    salt = userpass[1].split('$',3)[2]
    saltpwdhash = userpass[1].split('$',3)[3]
    wordHash = dict()
    for word in words:
            hasher = hashlib.sha256((salt + word).encode('utf-8'))
            hashcount += 1
            digest_as_hex_string = binascii.hexlify(hasher.digest()).decode('utf-8')
            wordHash[digest_as_hex_string] = word

    with open('cracked3.txt','a') as writer:
        writer.writelines(userpass[0] + ':' + wordHash[saltpwdhash] + '\n')
    print(hashcount)