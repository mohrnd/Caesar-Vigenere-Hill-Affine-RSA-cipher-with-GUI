import subprocess
import tkinter as tk

def main():
    title.config(text='Please select your preferred cipher method')
    Button1.config(text='Cesar', command=cesar, padx=10, pady=10)
    Button12.config(text='Cesar cryptanalyse', command=cryptanalyse, padx=10, pady=10)
    Button2.config(text='Vigenere', command=vigenere, padx=10, pady=10)
    Button3.config(text='Hill', command=hill, padx=10, pady=10)
    Button4.config(text='Affine', command=affine, padx=10, pady=10)
    Button5.config(text='RSA', command=RSA, padx=10, pady=10)
def cesar():
    script_path = 'cesar.py'
    subprocess.Popen(['python', script_path], shell=True)
    #call(["python3", "cesar.py"]) if you're on linux uncomment the this line and comment the line above

def vigenere():
    script_path = 'vigenere.py'
    subprocess.Popen(['python', script_path], shell=True)
    #call(["python3", "vigenere.py"])
def hill():
    script_path = 'hill.py'
    subprocess.Popen(['python', script_path], shell=True)
    #call (["python3", "hill.py"])
def affine():
    script_path = 'affine.py'
    subprocess.Popen(['python', script_path], shell=True)
    #call (["python3", "affine.py"])
def RSA():
    script_path = 'RSA.py'
    subprocess.Popen(['python', script_path], shell=True)
    #call (["python3", "RSA.py"])
def cryptanalyse():
    script_path = 'cryptanalyse_caesar.py'
    subprocess.Popen(['python', script_path], shell=True)
    #call (["python3", "cryptanalyse_caesar.py"])

window = tk.Tk()
window.title('Cryptography')


title = tk.Label(master=window, text='', font='Cairo')
title.pack()

Button1 = tk.Button(master=window, text='', width=20, height=1, font='Cairo')
Button1.pack(pady=5)
Button12 = tk.Button(master=window, text='', width=20, height=1, font='Cairo')
Button12.pack(pady=5)
Button2 = tk.Button(master=window, text='', width=20, height=1, font='Cairo')
Button2.pack(pady=5)
Button3 = tk.Button(master=window, text='', width=20, height=1, font='Cairo')
Button3.pack(pady=5)
Button4 = tk.Button(master=window, text='', width=20, height=1, font='Cairo')
Button4.pack(pady=5)
Button5 = tk.Button(master=window, text='', width=20, height=1, font='Cairo')
Button5.pack(pady=5)

main()
window.mainloop()
