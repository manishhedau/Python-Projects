import random
import string

def generator():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.punctuation
    s4 = string.digits
    s1 = list(map(str,s1))
    s2 = list(map(str,s2))
    s3 = list(map(str,s3))
    s4 = list(map(str,s4))
 
    s = []
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)
    # print(s)
    posslen = int(input('Enter the number of lenth of your Password : '))

    random.shuffle(s)
    Password = ''.join(s[0:posslen])
    print(Password)
generator()