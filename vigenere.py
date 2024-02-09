import tkinter as tk

alphdict = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
    'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18,
    'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
}

def encrypt(string, key):
    key_len = len(key)
    string_len = len(string)
    coded_string = []
    FINAL = []

    for num_letter in range(0, string_len):
        letter = string[num_letter]
        letter_num_in_dict = alphdict[letter]
        key_letter_pos_relative_to_string = num_letter % key_len
        key_letter = key[key_letter_pos_relative_to_string]
        key_letter_number = alphdict[key_letter]
        sum_key_str = key_letter_number + letter_num_in_dict
        coded_string.append((sum_key_str % 26))

    for num in coded_string:
        for letter, value in alphdict.items():
            if value == num:
                FINAL.append(letter)
                break

    return ''.join(FINAL)

def decrypt(string, key):
    key_len = len(key)
    string_len = len(string)
    decoded_string = []
    FINAL = []

    for num_letter in range(0, string_len):
        letter = string[num_letter]
        letter_num_in_dict = alphdict[letter]
        key_letter_pos_relative_to_string = num_letter % key_len
        key_letter = key[key_letter_pos_relative_to_string]
        key_letter_number = alphdict[key_letter]
        sub_key_str = letter_num_in_dict - key_letter_number
        decoded_string.append((sub_key_str % 26))

    for num in decoded_string:
        for letter, value in alphdict.items():
            if value == num:
                FINAL.append(letter)
                break

    return ''.join(FINAL)

def encrypt_string():
    string = entry_string.get().upper()
    key = entry_key.get().upper()

    encrypted_string = encrypt(string, key)
    label_ciphered.config(text="Ciphered string: " + encrypted_string)

def decrypt_string():
    string = entry_ciphered.get().upper()
    key = entry_key_decipher.get().upper()

    decrypted_string = decrypt(string, key)
    label_deciphered.config(text="Deciphered string: " + decrypted_string)

root = tk.Tk()
root.title("Vegnere Cipher")

# Encryption
frame_cipher = tk.Frame(root)
frame_cipher.pack(padx=10, pady=10)

label_string = tk.Label(frame_cipher, text="Enter the string you want to cipher:" , font='Cairo')
label_string.grid(row=0, column=0, sticky="w")

entry_string = tk.Entry(frame_cipher)
entry_string.grid(row=0, column=1, padx=5, pady=5)

label_key = tk.Label(frame_cipher, text="Enter your key (a string):" , font='Cairo')
label_key.grid(row=1, column=0, sticky="w")

entry_key = tk.Entry(frame_cipher)
entry_key.grid(row=1, column=1, padx=5, pady=5)

button_cipher = tk.Button(frame_cipher, text="Cipher", command=encrypt_string, font='Cairo')
button_cipher.grid(row=2, columnspan=2, pady=10)

label_ciphered = tk.Label(frame_cipher, text="")
label_ciphered.grid(row=3, columnspan=2)

# Decryption
frame_decipher = tk.Frame(root)
frame_decipher.pack(padx=10, pady=10)

label_ciphered_text = tk.Label(frame_decipher, text="Enter the ciphered string:", font='Cairo')
label_ciphered_text.grid(row=0, column=0, sticky="w")

entry_ciphered = tk.Entry(frame_decipher)
entry_ciphered.grid(row=0, column=1, padx=5, pady=5)

label_key_decipher = tk.Label(frame_decipher, text="Enter the key (a string):", font='Cairo')
label_key_decipher.grid(row=1, column=0, sticky="w")

entry_key_decipher = tk.Entry(frame_decipher)
entry_key_decipher.grid(row=1, column=1, padx=5, pady=5)

button_decipher = tk.Button(frame_decipher, text="Decipher", command=decrypt_string , font='Cairo')
button_decipher.grid(row=2, columnspan=2, pady=10)

label_deciphered = tk.Label(frame_decipher, text="")
label_deciphered.grid(row=3, columnspan=2)

root.mainloop()
