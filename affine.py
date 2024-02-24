import tkinter as tk

alphdict = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
    'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18,
    'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
}

def euclidian(m, b):
    A1, A2, A3 = 1, 0, m
    B1, B2, B3 = 0, 1, b
    while True:
        if B3 == 0:
            A3 = PGCD(m,b)
            print("pas divisible")
            return A1, A2, A3 
        elif B3 == 1:
            B3 = PGCD(m,b)
            return  B2   
        Q = A3 // B3
        T1, T2, T3 = (A1 - Q * B1), (A2 - Q * B2), (A3 - Q * B3)
        A1, A2, A3 = B1, B2, B3
        B1, B2, B3 = T1, T2, T3

def PGCD(a, b):
    while b:
        a, b = b, a % b
    return a

def encrypt(string, a , b):
    string_len = len(string)
    encrypted_string_num = []
    
    for num_letter in range(0, string_len):
        letter = string[num_letter]
        letter_num_in_dict = alphdict[letter]
        encrypted_letter = (a * letter_num_in_dict + b) % 26
        encrypted_string_num.append(encrypted_letter)
    
    encrypted_string = ''.join([list(alphdict.keys())[list(alphdict.values()).index(num)] for num in encrypted_string_num])
    return encrypted_string

def decrypt(string, a, b):
    string_len = len(string)
    decrypted_string_num = []
    
    for num_letter in range(0, string_len):
        letter = string[num_letter]
        letter_num_in_dict = alphdict[letter]
        NUM = euclidian(26, a)
        decrypted_letter = (NUM * (letter_num_in_dict - b)) % 26
        decrypted_string_num.append(decrypted_letter)
    
    decrypted_string = ''.join([list(alphdict.keys())[list(alphdict.values()).index(num)] for num in decrypted_string_num])
    return decrypted_string

def encrypt_string():
    string = entry_string.get().upper()
    a = int(entry_a.get())
    b = int(entry_b.get())

    encrypted_string = encrypt(string, a , b)
    label_ciphered.config(text="Ciphered string: " + encrypted_string)

def decrypt_string():
    string = entry_ciphered.get().upper()
    a = int(entry_a_decipher.get())
    b = int(entry_b_decipher.get())

    decrypted_string = decrypt(string, a , b)
    label_deciphered.config(text="Deciphered string: " + decrypted_string)

root = tk.Tk()
root.title("Affine Cipher")

# Encryption
frame_cipher = tk.Frame(root)
frame_cipher.pack(padx=10, pady=10)

label_string = tk.Label(frame_cipher, text="Enter the string you want to cipher:" , font='Cairo')
label_string.grid(row=0, column=0, sticky="w")

entry_string = tk.Entry(frame_cipher)
entry_string.grid(row=0, column=1, padx=5, pady=5)

label_a = tk.Label(frame_cipher, text="Enter the value of a:" , font='Cairo')
label_a.grid(row=1, column=0, sticky="w")

entry_a = tk.Entry(frame_cipher)
entry_a.grid(row=1, column=1, padx=5, pady=5)

label_b = tk.Label(frame_cipher, text="Enter the value of b:" , font='Cairo')
label_b.grid(row=2, column=0, sticky="w")

entry_b = tk.Entry(frame_cipher)
entry_b.grid(row=2, column=1, padx=5, pady=5)

button_cipher = tk.Button(frame_cipher, text="Cipher", command=encrypt_string, font='Cairo')
button_cipher.grid(row=3, columnspan=2, pady=10)

label_ciphered = tk.Label(frame_cipher, text="")
label_ciphered.grid(row=4, columnspan=2)

# Decryption
frame_decipher = tk.Frame(root)
frame_decipher.pack(padx=10, pady=10)

label_ciphered_text = tk.Label(frame_decipher, text="Enter the ciphered string:", font='Cairo')
label_ciphered_text.grid(row=0, column=0, sticky="w")

entry_ciphered = tk.Entry(frame_decipher)
entry_ciphered.grid(row=0, column=1, padx=5, pady=5)

label_a_decipher = tk.Label(frame_decipher, text="Enter the value of a:", font='Cairo')
label_a_decipher.grid(row=1, column=0, sticky="w")

entry_a_decipher = tk.Entry(frame_decipher)
entry_a_decipher.grid(row=1, column=1, padx=5, pady=5)


label_b_decipher = tk.Label(frame_decipher, text="Enter the value of b:", font='Cairo')
label_b_decipher.grid(row=2, column=0, sticky="w")

entry_b_decipher = tk.Entry(frame_decipher)
entry_b_decipher.grid(row=2, column=1, padx=5, pady=5)

button_decipher = tk.Button(frame_decipher, text="Decipher", command=decrypt_string , font='Cairo')
button_decipher.grid(row=3, columnspan=2, pady=10)

label_deciphered = tk.Label(frame_decipher, text="")
label_deciphered.grid(row=4, columnspan=2)

root.mainloop()
