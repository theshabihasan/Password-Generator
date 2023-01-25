import string
import random
if __name__ == '__main__':
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation
    plen = int(input("Enter the length of password:\n"))
    s = []
    s.extend(s1)
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)
    random.shuffle(s)
    print("Your password is: ")
    print("".join(s[0:plen]))
