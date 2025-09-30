import sys
import os
import string
import tkinter as tk
from tkinter import messagebox

file_counter = 0

def decryptFolder(folder):
    global file_counter

    folderPath = os.path.join(gamePath, 'www', folder)

    for file in os.listdir(folderPath):
        file_counter += 1

        with open(os.path.join(folderPath, file), 'rb') as rf:
            data = rf.read()

        if True:
            extension = ''
            topFolder = folder.split('/')[0]

            if topFolder == 'data':
                extension = '.json'
            elif topFolder == 'audio':
                extension = '.ogg'
            elif topFolder == 'img':
                extension = '.png'
            else:
                messagebox.showerror("Error", "Unknown top folder: " + topFolder)
                sys.exit()

            data = decrypt(data, folder + '/' + file)

            newFile = os.path.basename(file) + extension

            os.makedirs(os.path.join(outPath, folder), exist_ok=True)

            with open(os.path.join(outPath, folder, newFile), 'wb') as wf:
                wf.write(data)


def decrypt(raw_bytes, idFilePath):
    encrypted_data = raw_bytes[len(signature) + 1:]

    encrypt_offset = raw_bytes[len(signature)]
    if encrypt_offset == 0:
        encrypt_offset = len(encrypted_data)

    mask = (getMask(idFilePath) + 1) % 256
    decrypted_data = bytearray(encrypted_data)

    for i in range(encrypt_offset):
        original_byte = encrypted_data[i]
        decrypted_data[i] = original_byte ^ mask
        mask = ((mask << 1) ^ original_byte) & 255

    return bytes(decrypted_data)

def getMask(filename):
    mask = 0
    filename = filename.split('/')[-1].upper()

    for char in filename:
        mask = mask << 1 ^ ord(char)

    return mask

def getSignature(gamePath):
    return b'TCOAAL'

def find_game_folder():
    drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
    for drive in drives:
        steam_path = os.path.join(drive, "\\", "SteamLibrary", "steamapps", "common", "The Coffin of Andy and Leyley")
        if os.path.exists(steam_path):
            return steam_path
    return os.getcwd()

if sys.version_info[0] < 3 or sys.version_info[1] < 2:
    messagebox.showerror("Error", "Python 3.2+ is required")
    sys.exit()

root = tk.Tk()
root.withdraw()

gamePath = find_game_folder()
outPath = os.path.join(os.getcwd(), "decrypted TCOAAL assets")

if not os.path.exists(os.path.join(gamePath, 'www/img/system/e5230bf37c4fabb0')):
    messagebox.showerror("Place .exe file in the game's dir", "The game folder was not found.\Place this .exe file in the game's root directory and try again.\n\nUsually it's in C:\\Program Files (x86)\\Steam\\steamapps\\common\\The Coffin of Andy and Leyley")
    sys.exit()

os.makedirs(outPath, exist_ok=True)
signature = getSignature(gamePath)

decryptFolder('data')
decryptFolder('audio/bgm')
decryptFolder('audio/bgs')
decryptFolder('audio/me')
decryptFolder('audio/se')
decryptFolder('img/characters')
decryptFolder('img/faces')
decryptFolder('img/parallaxes')
decryptFolder('img/pictures')
decryptFolder('img/system')
decryptFolder('img/tilesets')
decryptFolder('img/titles1')

messagebox.showinfo("Decryption successful!", f"{file_counter} files processed.\n\nThank you Basil & Phoni for your work on tools for TCOAAL. For the OG tool visit: https://codeberg.org/basil/grimoire.\nMade by AlternativeOne with love. https://github.com/AlternativeOne/tcoaal_decryptor\nPacked into .exe by @GreatFireDragon without Love.")
