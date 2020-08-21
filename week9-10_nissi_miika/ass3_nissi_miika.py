# Morse code translator Python3 program
# 
# Assignment 3, Week 9 and 10, Miika Nissi

import tkinter

class MorseCoder:
    def __init__(self, root):
        self.MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
        root.title("Morse coder")
        root.geometry()
        root.configure(bg="#2a2a2a")

        self.string_encrypt = tkinter.StringVar()
        self.string_decrypt = tkinter.StringVar()

        self.label1 = tkinter.Label(root, text="Encrypt:", bg="#2a2a2a", fg="white")
        self.label2 = tkinter.Label(root, text="Decrypt:", bg="#2a2a2a", fg="white")

        self.entry_encrypt = tkinter.Entry(root, textvariable=self.string_encrypt, bg="black", fg="white", width=30)
        self.entry_decrypt = tkinter.Entry(root, textvariable=self.string_decrypt, bg="black", fg="white", width=30)

        self.label1.grid(row=0, column=0, pady=6, padx=6)
        self.label2.grid(row=1, column=0, pady=6, padx=6)
        self.entry_encrypt.grid(row=0, column=1, pady=6, padx=6)
        self.entry_decrypt.grid(row=1, column=1, pady=6, padx=6)

        self.update_in_progress = False

        self.string_encrypt.trace("w", self.callback_encrypt)
        self.string_decrypt.trace("w", self.callback_decrypt)
        
    def callback_encrypt(self, *args):
        if self.update_in_progress:
            return
        new_string_decrypt = self.encrypt(self.string_encrypt.get().upper())
        self.update_in_progress = True
        self.string_decrypt.set(new_string_decrypt)
        self.update_in_progress = False

    def callback_decrypt(self, *args):
        if self.update_in_progress:
            return
        new_string_encrypt = self.decrypt(self.string_decrypt.get())
        self.update_in_progress = True
        self.string_encrypt.set(new_string_encrypt)
        self.update_in_progress = False
        
    def encrypt(self, s):
        morse = ""
        try:
            for letter in s:
                if (letter != " "):
                    morse += self.MORSE_CODE_DICT[letter] + " "
                else:
                    morse += " "
            return morse
        except:
            return morse
    
    def decrypt(self, s):
        s += " "
        message = ""
        word = ""
        for letter in s:
            try:
                if (letter != " "):
                    i = 0
                    word += letter
                else:
                    i += 1
                    if (i==2):
                        message += " "
                    else:
                        message += list(self.MORSE_CODE_DICT.keys())[list(self.MORSE_CODE_DICT.values()).index(word)]
                        word = ""
            except:
                return message

        return message
        
    
root = tkinter.Tk()
morse = MorseCoder(root)
root.mainloop()
