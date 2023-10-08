"""
.trans creator by EgorV4x
"""

import glob
import json
from os import path

jsonfile = open("hiragana.json", encoding='UTF-8', errors='ignore')
pDict = json.load(jsonfile)
jsonfile.close

wav_path = input("Enter wav directory: ")
wav_path = wav_path + "\\"
wav_files = glob.glob(f'{wav_path}*.wav')

creating_ask = input("Do you want to create automatic transcriptions? (write Yes or No) ")
auto_creating = False
if creating_ask.lower() == "yes":
    auto_creating = True

for filepath in wav_files:

    name = path.basename(filepath)
    name = path.splitext(name)[0]

    filepath = filepath.replace(".wav", ".trans")
    trans_file = open(filepath, "w+")
    if auto_creating == True:
        nameLen = len(name)
        phoneme = "Sil "
        findCheck = False
        for i in range(0, nameLen):
            findCheck = False
            if i + 1 < nameLen:
                for obj in pDict:
                    if obj['kana'] == (name[i] + name[i+1]):
                        phoneme += obj['phoneme'] + " "
                        findCheck = True
                        break
                if findCheck == False:
                    for obj in pDict:
                        if obj['kana'] == (name[i]):
                            phoneme += obj['phoneme'] + " "
                            break
            else:
                for obj in pDict:
                    if obj['kana'] == (name[i]):
                        phoneme += obj['phoneme'] + " "
                        break
        
        phoneme += "Sil"
        
        trans_file.write(phoneme)
        phonlist = phoneme.split()
        phonLen = len(phonlist)
        for i in range(0, phonLen):
            if i < phonLen - 1:
                trans_file.write("\n[" + phonlist[i] + " " + phonlist[i + 1] + "]")
            else:
                break

    
    trans_file.close()

print("Process Completed!")