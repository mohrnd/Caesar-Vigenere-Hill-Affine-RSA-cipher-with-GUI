import tkinter as tk
import numpy as np

alphdict = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
    'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18,
    'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
}

def encrypt():
    intstr = []
    matrix = []

    # Prepare matrix
    for _ in range(n):
        matrix.append([0] * n)

    for A in range(n):
        for B in range(n):
            number = int(entry_keys[A][B].get())
            matrix[A][B] = number

    string = entry_plain_text.get().upper()
    string_len = len(string)

    if string_len % n != 0:
        string += 'X' * (n - string_len % n)
        string_len = len(string)

    for letter in string:
        number = alphdict[letter]
        intstr.append(number)

    result = []
    for number in range(0, string_len, n):
        temp_table = []
        for R in range(0, n):
            temp_table.append(intstr[number + R])
        coded_chunk = np.dot(matrix, temp_table) % 26
        result.extend(coded_chunk.flatten())

    ciphered_text = ''.join([list(alphdict.keys())[list(alphdict.values()).index(num)] for num in result])
    label_ciphered_text.config(text="Encrypted string: " + ciphered_text)

def decrypt():
    intstr = []
    matrix = []

    for _ in range(n):
        matrix.append([0] * n)

    for A in range(n):
        for B in range(n):
            number = int(entry_keys_decrypt[A][B].get())
            matrix[A][B] = number

    determinant = np.linalg.det(matrix)
    adjoint = np.linalg.inv(matrix) * determinant
    K_inv = 1 / determinant * adjoint
    int_str_ciphered = []

    ciphered_str = entry_ciphered_text.get().upper()
    ciphered_str_len = len(ciphered_str)

    if ciphered_str_len % n != 0:
        ciphered_str += 'X' * (n - ciphered_str_len % n)
        ciphered_str_len = len(ciphered_str)

    for letter in ciphered_str:
        number = alphdict[letter]
        int_str_ciphered.append(number)

    result = []
    for number in range(0, ciphered_str_len, n):
        temp_table = []
        for R in range(0, n):
            temp_table.append(int_str_ciphered[number + R])
        coded_chunk = np.dot(K_inv, temp_table) % 26
        result.extend(coded_chunk.flatten())

    decrypted_text = ''.join([list(alphdict.keys())[list(alphdict.values()).index(num)] for num in result])
    label_deciphered_text.config(text="Decrypted string: " + decrypted_text)

# Create GUI
root = tk.Tk()
root.title("Matrix Encryption")

# Encryption Frame
frame_encrypt = tk.Frame(root)
frame_encrypt.pack(padx=10, pady=10)

label_plain_text = tk.Label(frame_encrypt, text="Enter the plain text:", font='Cairo')
label_plain_text.grid(row=0, column=0, sticky="w")

entry_plain_text = tk.Entry(frame_encrypt)
entry_plain_text.grid(row=0, column=1, padx=5, pady=5)

label_key = tk.Label(frame_encrypt, text="Enter your matrix (space-separated integers):", font='Cairo')
label_key.grid(row=1, column=0, sticky="w")



n = 2




entry_keys = [[None]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        entry_keys[i][j] = tk.Entry(frame_encrypt)
        entry_keys[i][j].grid(row=i+1, column=j+1, padx=5, pady=5)

button_encrypt = tk.Button(frame_encrypt, text="Encrypt", command=encrypt, font='Cairo')
button_encrypt.grid(row=n+1, columnspan=n+1, pady=10)

label_ciphered_text = tk.Label(frame_encrypt, text="")
label_ciphered_text.grid(row=n+2, columnspan=n+1)

# Decryption Frame
frame_decrypt = tk.Frame(root)
frame_decrypt.pack(padx=10, pady=10)

label_ciphered_text2 = tk.Label(frame_decrypt, text="Enter the ciphered text:", font='Cairo')
label_ciphered_text2.grid(row=0, column=0, sticky="w")

entry_ciphered_text = tk.Entry(frame_decrypt)
entry_ciphered_text.grid(row=0, column=1, padx=5, pady=5)

label_key_decrypt = tk.Label(frame_decrypt, text="Enter the matrix (space-separated integers):", font='Cairo')
label_key_decrypt.grid(row=1, column=0, sticky="w")

entry_keys_decrypt = [[None]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        entry_keys_decrypt[i][j] = tk.Entry(frame_decrypt)
        entry_keys_decrypt[i][j].grid(row=i+1, column=j+1, padx=5, pady=5)

button_decrypt = tk.Button(frame_decrypt, text="Decrypt", command=decrypt, font='Cairo')
button_decrypt.grid(row=n+1, columnspan=n+1, pady=10)

label_deciphered_text = tk.Label(frame_decrypt, text="")
label_deciphered_text.grid(row=n+2, columnspan=n+1)

root.mainloop()
