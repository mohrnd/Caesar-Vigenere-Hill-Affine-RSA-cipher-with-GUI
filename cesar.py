import tkinter as tk

alphdict = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
    'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18,
    'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
}

def cipher_string():
    string = entry_string.get().upper()
    key = int(entry_key.get())

    numstr = []
    numciphered = []
    strciphered = []

    for letter in string:
        num = alphdict.get(letter, None)
        if num is not None:
            numstr.append(num)

    for num in numstr:
        R = (key + num) % 26
        numciphered.append(R)

    for num in numciphered:
        for letter, value in alphdict.items():
            if value == num:
                strciphered.append(letter)
                break

    label_ciphered.config(text="Ciphered string: " + ''.join(strciphered) , font='Cairo')

def decipher_string():
    string = entry_ciphered.get().upper()
    key = int(entry_key_decipher.get())

    numciphered = []
    num_deciphered = []
    str_deciphered = []

    for letter in string:
        num = alphdict.get(letter, None)
        if num is not None:
            numciphered.append(num)

    for num in numciphered:
        R = (num - key) % 26
        num_deciphered.append(R)

    for num in num_deciphered:
        for letter, value in alphdict.items():
            if value == num:
                str_deciphered.append(letter)
                break

    label_deciphered.config(text="Deciphered string: " + ''.join(str_deciphered) , font='Cairo')


root = tk.Tk()
root.title("Caesar Cipher")


frame_cipher = tk.Frame(root)
frame_cipher.pack(padx=10, pady=10)

label_string = tk.Label(frame_cipher, text="Enter the string you want to cipher:" , font='Cairo')
label_string.grid(row=0, column=0, sticky="w")

entry_string = tk.Entry(frame_cipher)
entry_string.grid(row=0, column=1, padx=5, pady=5)

label_key = tk.Label(frame_cipher, text="Enter your key (an integer):" , font='Cairo')
label_key.grid(row=1, column=0, sticky="w")

entry_key = tk.Entry(frame_cipher)
entry_key.grid(row=1, column=1, padx=5, pady=5)

button_cipher = tk.Button(frame_cipher, text="Cipher", command=cipher_string, font='Cairo')
button_cipher.grid(row=2, columnspan=2, pady=10)

label_ciphered = tk.Label(frame_cipher, text="")
label_ciphered.grid(row=3, columnspan=2)

# Decipher 
frame_decipher = tk.Frame(root)
frame_decipher.pack(padx=10, pady=10)

label_ciphered_text = tk.Label(frame_decipher, text="Enter the ciphered string:", font='Cairo')
label_ciphered_text.grid(row=0, column=0, sticky="w")

entry_ciphered = tk.Entry(frame_decipher)
entry_ciphered.grid(row=0, column=1, padx=5, pady=5)

label_key_decipher = tk.Label(frame_decipher, text="Enter the key (an integer):", font='Cairo')
label_key_decipher.grid(row=1, column=0, sticky="w")

entry_key_decipher = tk.Entry(frame_decipher)
entry_key_decipher.grid(row=1, column=1, padx=5, pady=5)

button_decipher = tk.Button(frame_decipher, text="Decipher", command=decipher_string , font='Cairo')
button_decipher.grid(row=2, columnspan=2, pady=10)

label_deciphered = tk.Label(frame_decipher, text="")
label_deciphered.grid(row=3, columnspan=2)

root.mainloop()
