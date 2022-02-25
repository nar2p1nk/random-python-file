import hashlib
import random
### basic hashing(shuffle) ###
def shuffleword(word):

    Lword= list(word)

    random.shuffle(Lword)

    password= ''.join(Lword)

    print(password)

### hashing ###

def hashed(word):
    password = word.encode()

    print(password)

    print('password before hashing')

    time.sleep(4)

    print(hashlib.blake2b(password).hexdigest())

    print('password after hashing')
