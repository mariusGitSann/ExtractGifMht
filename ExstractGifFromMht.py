import base64
import os
from tkinter import filedialog


append = False
filnavn = ""

binfil=""

def createfile(loade,name):
    img_fil = str.encode(loade)
    img_decode = base64.decodebytes(img_fil)
    img_result = open(name+'.gif', 'wb')  # create a writable Image
    img_result.write(img_decode)
    img_result.close()


file = filedialog.askopenfilename(title = "Select .mht",filetypes=[('Report Tool','*.mht'), ('All files','*.*')])
#file = 'Recording_20180904_1717.mht'


dir_path = os.path.dirname(os.path.realpath(file))

os.chdir(dir_path)

with open (file, 'rt') as in_file:  # Open file lorem.txt for reading of text data.
    for line in in_file: # Store each line in a string variable "line"
        #print(line) # prints that line'
        a = line

        if append:
            if "--=" in line:
                append = False
                #print (binfil)
                createfile(binfil,filnavn)
                binfil = ""

        if len(line) > 5 and append:
            #print("Fil : {}  txt : {}".format(filnavn,line.strip()))
            binfil+=line.strip()
        #if "Content-Location" in a.lower() and ".JPEG" in a:
        if "content-location" in a.lower() and ".jpeg" in a.lower():
            start = a.find(':') + 1
            stop = a.lower().find('.jpeg')
            filnavn = a[start:stop].strip()
            print("File Name : {}".format(filnavn))
            append = True


