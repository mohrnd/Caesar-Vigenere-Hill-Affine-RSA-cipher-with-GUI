import tkinter as tk

alphdict = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
    'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18,
    'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
}

def decrypt(string, a, b):
    string_len = len(string)
    decrypted_string_num = []
    
    for num_letter in range(0, string_len):
        letter = string[num_letter]
        letter_num_in_dict = alphdict[letter]
        decrypted_letter = pow(a, -1 , 26) * (letter_num_in_dict - b) % 26
        decrypted_string_num.append(decrypted_letter)
    
    decrypted_string = ''.join([list(alphdict.keys())[list(alphdict.values()).index(num)] for num in decrypted_string_num])
    return decrypted_string

def decrypt_string():
    string = entry_ciphered.get().upper()
    for A in range(1, 12, 2):  
        for B in range(0, 25):
            decrypted_string = decrypt(string, A, B)
            text_deciphered_thingy.insert(tk.END, f" A: {A} B: {B} {decrypted_string}\n")




root = tk.Tk()
root.title("Affine Cipher")


# Decryption
frame_decipher = tk.Frame(root)
frame_decipher.pack(padx=10, pady=10)

label_ciphered_text = tk.Label(frame_decipher, text="Enter the ciphered string:", font='Cairo')
label_ciphered_text.grid(row=0, column=0, sticky="w")

entry_ciphered = tk.Entry(frame_decipher)
entry_ciphered.grid(row=0, column=1, padx=5, pady=5)

button_decipher = tk.Button(frame_decipher, text="Decipher", command=decrypt_string , font='Cairo')
button_decipher.grid(row=3, columnspan=2, pady=10)

label_deciphered = tk.Label(frame_decipher, text="")
label_deciphered.grid(row=4, columnspan=2)

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_deciphered_thingy = tk.Text(root, wrap=tk.WORD, yscrollcommand=scrollbar.set)
text_deciphered_thingy.pack(expand=True, fill=tk.BOTH)

scrollbar.config(command=text_deciphered_thingy.yview)

root.mainloop()
