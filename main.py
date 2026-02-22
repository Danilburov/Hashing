# from hashlib import md5

# input_ = input('Enter something: ')
# print(md5(input_.encode('utf-8')).hexdigest())

from collections import Counter

length_counter = Counter()

with open("rockyou.txt", "rb") as f:
    for line in f:
        password = line.strip()
        if password:
            length_counter[len(password)] += 1

for length in sorted(length_counter):
    print(length, length_counter[length])

