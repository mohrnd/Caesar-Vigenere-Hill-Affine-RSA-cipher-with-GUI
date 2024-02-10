import tkinter as tk

################################
#P and Q: Prime numbers
#N: Product
#T: Totient
#E: Public Key:
#             -must be a prime number
#             -must be less than T
#             -must not be a factor of T (T mod D != 0)
#D: Private Key:
#             -D * E mod T MUST be equal to 1
################################

alphdict = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
    'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18,
    'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
}

def is_prime(number):
    if number == 0 or number == 1:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

def encrypt(string, E, N):
    string = string.upper() 
    string_len = len(string)
    encrypted_string_num = []
    
    for num_letter in range(0, string_len):
        letter = string[num_letter]
        if letter in alphdict:
            letter_num_in_dict_enc = alphdict[letter]
            encrypted_letter = letter_num_in_dict_enc ** E % 26
            encrypted_string_num.append(encrypted_letter) 
    
    encrypted_string = ''.join([list(alphdict.keys())[list(alphdict.values()).index(num)] for num in encrypted_string_num])
    return encrypted_string

def decrypt(cipher, D, N):
    cipher = cipher.upper()  
    cipher_len = len(cipher)
    decrypted_cipher_num = []
    
    for num_letter in range(0, cipher_len):
        letter = cipher[num_letter]
        if letter in alphdict:
            letter_num_in_dict_dec = alphdict[letter]
            decrypted_letter = letter_num_in_dict_dec ** D % 26
            decrypted_cipher_num.append(decrypted_letter) 
    
    decrypted_cipher = ''.join([list(alphdict.keys())[list(alphdict.values()).index(num)] for num in decrypted_cipher_num])
    return decrypted_cipher

def Public_Key_gen(P, Q):
    N = P * Q
    T = (P - 1) * (Q - 1)
    E = 0
    for number in range(2, T):  
        if is_prime(number) and T % number != 0 and number < T:
            E = number
            break
    return E
    print('E', E)

def Private_Key_gen(E, P, Q):
    D = None 
    T = (P - 1) * (Q - 1)
    for number in range(T):
        if number * E % T == 1:
            D = number
            break
    return D
    print('D', D)
root = tk.Tk()
root.title("RSA Encryption and Decryption")

# Generate Public and Private Keys
frame_keys = tk.Frame(root)
frame_keys.pack(padx=10, pady=10)

label_p = tk.Label(frame_keys, text="Enter prime number P:", font='Cairo')
label_p.grid(row=0, column=0, sticky="w")

entry_p = tk.Entry(frame_keys)
entry_p.grid(row=0, column=1, padx=5, pady=5)

label_q = tk.Label(frame_keys, text="Enter prime number Q:", font='Cairo')
label_q.grid(row=1, column=0, sticky="w")

entry_q = tk.Entry(frame_keys)
entry_q.grid(row=1, column=1, padx=5, pady=5)

label_public_key = tk.Label(frame_keys, text="Public Key (E):", font='Cairo')
label_public_key.grid(row=2, column=0, sticky="w")

label_private_key = tk.Label(frame_keys, text="Private Key (D):", font='Cairo')
label_private_key.grid(row=3, column=0, sticky="w")

def generate_keys():
    p = int(entry_p.get())
    q = int(entry_q.get())
    
    E = Public_Key_gen(p, q)
    D = Private_Key_gen(E, p, q)
    print(p, q, E, D)
    label_public_key.config(text="Public Key (E): " + str(E))
    label_private_key.config(text="Private Key (D): " + str(D))

button_generate_keys = tk.Button(frame_keys, text="Generate Keys", command=generate_keys, font='Cairo')
button_generate_keys.grid(row=2, column=1, rowspan=2, padx=5, pady=5)

# Encryption
frame_encrypt = tk.Frame(root)
frame_encrypt.pack(padx=10, pady=10)

label_message_encrypt = tk.Label(frame_encrypt, text="Enter the message you want to encrypt:", font='Cairo')
label_message_encrypt.grid(row=0, column=0, sticky="w")

entry_message_encrypt = tk.Entry(frame_encrypt)
entry_message_encrypt.grid(row=0, column=1, padx=5, pady=5)

label_public_key_encrypt = tk.Label(frame_encrypt, text="Enter the public key (E):", font='Cairo')
label_public_key_encrypt.grid(row=1, column=0, sticky="w")

entry_public_key_encrypt = tk.Entry(frame_encrypt)
entry_public_key_encrypt.grid(row=1, column=1, padx=5, pady=5)

label_encrypted_message = tk.Label(frame_encrypt, text="Encrypted Message:", font='Cairo')
label_encrypted_message.grid(row=2, columnspan=2)

def encrypt_message():
    message = entry_message_encrypt.get()
    E = int(entry_public_key_encrypt.get())
    N = int(entry_p.get()) * int(entry_q.get())
    print('N: ',N)
    print('E: ',E)
    
    encrypted_message = encrypt(message, E, N)
    
    label_encrypted_message.config(text="Encrypted Message: " + encrypted_message)

button_encrypt = tk.Button(frame_encrypt, text="Encrypt", command=encrypt_message, font='Cairo')
button_encrypt.grid(row=3, columnspan=2, pady=10)

# Decryption
frame_decrypt = tk.Frame(root)
frame_decrypt.pack(padx=10, pady=10)

label_message_decrypt = tk.Label(frame_decrypt, text="Enter the message you want to decrypt:", font='Cairo')
label_message_decrypt.grid(row=0, column=0, sticky="w")

entry_message_decrypt = tk.Entry(frame_decrypt)
entry_message_decrypt.grid(row=0, column=1, padx=5, pady=5)

label_private_key_decrypt = tk.Label(frame_decrypt, text="Enter the private key (D):", font='Cairo')
label_private_key_decrypt.grid(row=1, column=0, sticky="w")

entry_private_key_decrypt = tk.Entry(frame_decrypt)
entry_private_key_decrypt.grid(row=1, column=1, padx=5, pady=5)

label_decrypted_message = tk.Label(frame_decrypt, text="Decrypted Message:", font='Cairo')
label_decrypted_message.grid(row=2, columnspan=2)

def decrypt_message():
    message = entry_message_decrypt.get()
    D = int(entry_private_key_decrypt.get())
    N = int(entry_p.get()) * int(entry_q.get())
    
    decrypted_message = decrypt(message, D, N)
    
    label_decrypted_message.config(text="Decrypted Message: " + decrypted_message)

button_decrypt = tk.Button(frame_decrypt, text="Decrypt", command=decrypt_message, font='Cairo')
button_decrypt.grid(row=3, columnspan=2, pady=10)

root.mainloop()
