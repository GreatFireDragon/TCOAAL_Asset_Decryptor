import sys
import os

file_counter=0

def decryptFolder(folder):
  global file_counter

  folderPath = os.path.join(gamePath, 'www', folder)
  
  for file in os.listdir(folderPath):
    file_counter+=1
  
    with open(os.path.join(folderPath, file), 'rb') as rf:
      data=rf.read()

    if True:
      extension=''
      topFolder = folder.split('/')[0]
      
      if topFolder=='data':
        extension = '.json'
      elif topFolder=='audio':
        extension = '.ogg'
      elif topFolder=='img':
        extension = '.png'
      else:
        print('Unknown top folder')
        quit()

      data=decrypt(data, folder + '/' + file)
      
      newFile = os.path.basename(file) + extension
      
      os.makedirs(os.path.join(outPath, folder), exist_ok=True)
      
      with open(os.path.join(outPath, folder, newFile), 'wb') as wf:
        wf.write(data)

    if file_counter%50==0:
      print(str(file_counter)+' files processed')

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
  return 'TCOAAL'

if sys.version_info[0] < 3 or sys.version_info[1] < 2:
  print('Python 3.2+ is required')
  quit()

gamePath=str(sys.argv[1])
outPath=str(sys.argv[2])

print('\nThank you Basil & Phoni for your work on tools for TCOAAL. For the OG tool visit: https://codeberg.org/basil/grimoire.\nMade by AlternativeOne with love.\n')

if not os.path.exists(os.path.join(gamePath, 'www/img/system/e5230bf37c4fabb0')):
  print('Game is not of 3.0.0+ version')
  quit()

signature=getSignature(gamePath)

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

if file_counter%50!=0:
  print(str(file_counter)+' files processed')
print('Success')



