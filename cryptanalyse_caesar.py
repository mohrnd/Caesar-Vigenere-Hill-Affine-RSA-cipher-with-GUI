import tkinter as tk
import enchant

alphdict = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
    'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18,
    'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
}

def decipher_string(key):
    global string
    string = entry_ciphered.get().upper()
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
    text_deciphered_thingy.insert(tk.END, ''.join(str_deciphered) + f" Key: {key}\n")
    
    # # this will only detect single ciphered words (you can uncomment the following to use it)
    # d = enchant.Dict("en_US")
    # lang_check = d.check(''.join(str_deciphered))
    # if lang_check == True:
    #     text_deciphered_thingy.insert(tk.END, ''.join(str_deciphered) + f" Key: {key}\n")
    # else: 
    #     pass

def brute_force():
    for number in range(0, 26):
        decipher_string(number)

root = tk.Tk()
root.title("caesar brute force Decipher")

# Decipher 
frame_decipher = tk.Frame(root)
frame_decipher.pack(padx=10, pady=10)

label_ciphered_text = tk.Label(frame_decipher, text="Enter the ciphered string:", font='Cairo')
label_ciphered_text.grid(row=0, column=0, sticky="w")

entry_ciphered = tk.Entry(frame_decipher)
entry_ciphered.grid(row=0, column=1, padx=5, pady=5)

button_decipher = tk.Button(frame_decipher, text="Decipher", command=brute_force, font='Cairo')
button_decipher.grid(row=2, columnspan=2, pady=10)

# Scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

text_deciphered_thingy = tk.Text(root, wrap=tk.WORD, yscrollcommand=scrollbar.set)
text_deciphered_thingy.pack(expand=True, fill=tk.BOTH)

scrollbar.config(command=text_deciphered_thingy.yview)

root.mainloop()
