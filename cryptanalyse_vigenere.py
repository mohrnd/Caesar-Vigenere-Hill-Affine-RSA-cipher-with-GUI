import tkinter as tk

alphdict = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
    'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18,
    'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
}

def Get_key(string, CipheredString):
    key = ''
    string_length = len(string)
    for i in range(string_length):
        key_index = (alphdict[CipheredString[i]] - alphdict[string[i]]) % 26
        for letter, index in alphdict.items():
            if index == key_index:
                key += letter
                break
    return key


def Get_key_string():
    string = Original_string.get().upper()
    CipheredString = Ciphered_string.get().upper()

    Key = Get_key(string, CipheredString)
    text_deciphered_thingy.insert(tk.END, f" The Key: " +''.join(Key) + f" Ciphered String: {CipheredString}\n" + f" Original String: {string}\n")

root = tk.Tk()
root.title("Vigenere Cipher")

frame_decipher = tk.Frame(root)
frame_decipher.pack(padx=10, pady=10)

label_ciphered_text = tk.Label(frame_decipher, text="Enter the original string:", font='Cairo')
label_ciphered_text.grid(row=0, column=0, sticky="w")

Original_string = tk.Entry(frame_decipher)
Original_string.grid(row=0, column=1, padx=5, pady=5)

label_CipheredString_decipher = tk.Label(frame_decipher, text="Enter the ciphered string:", font='Cairo')
label_CipheredString_decipher.grid(row=1, column=0, sticky="w")

Ciphered_string = tk.Entry(frame_decipher)
Ciphered_string.grid(row=1, column=1, padx=5, pady=5)

button_decipher = tk.Button(frame_decipher, text="Find the CipheredString", command=Get_key_string, font='Cairo')
button_decipher.grid(row=2, columnspan=2, pady=10)

scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_deciphered_thingy = tk.Text(root, wrap=tk.WORD, yscrollcommand=scrollbar.set)
text_deciphered_thingy.pack(expand=True, fill=tk.BOTH)

scrollbar.config(command=text_deciphered_thingy.yview)

root.mainloop()
