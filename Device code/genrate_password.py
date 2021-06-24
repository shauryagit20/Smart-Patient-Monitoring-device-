import random

def genrate_password():
    rand_length =  random.randint(8,12)
    passwd= ""
    for _ in range(rand_length):
        rand_ascii = random.randint(65,122)
        character_to_add =  chr(rand_ascii)
        print(character_to_add)
        passwd = passwd + str(character_to_add)
    return passwd