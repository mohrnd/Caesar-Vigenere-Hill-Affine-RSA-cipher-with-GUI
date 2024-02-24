alphdict = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
    'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18,
    'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
}

dictt = {}

string = input("String: ")
key = input("Key: ")

keytab = []


for num_letter in range(len(key)):
    letter = key[num_letter]
    key_letter_num_in_dict = alphdict[letter]
    dictt[key_letter_num_in_dict] = []
    keytab.append(key_letter_num_in_dict)
    keytab = sorted(keytab)

for letter_num in range(len(string)):
    letter = string[letter_num]
    index = letter_num % len(key)
    key_letter = key[index]
    key_letter_num = alphdict[key_letter]
    dictt[key_letter_num].append(letter)

    
print(dictt) 
#SORTING THE DICT
sorted_dict = dict(sorted(dictt.items()))
print(sorted_dict)


#PRINTING THE CIPHERED MESSAGE

max_length = max(len(column) for column in dictt.values())
for i in range(max_length):
    for key in keytab:
        if i < len(dictt[key]):
            print(dictt[key][i], end='')




