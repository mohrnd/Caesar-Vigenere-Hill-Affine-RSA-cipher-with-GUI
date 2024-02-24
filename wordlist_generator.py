from itertools import product
from string import ascii_uppercase
#https://stackoverflow.com/questions/23686398/iterate-a-to-zzz-in-python
with open("wordlist.txt", "w") as file:
    file.write("word_list = [\n")
    

    for x in range(1, 5):
        for combo in product(ascii_uppercase, repeat=x):
            word = ''.join(combo)
            file.write(f"    '{word}',\n")

    file.write("]\n")
