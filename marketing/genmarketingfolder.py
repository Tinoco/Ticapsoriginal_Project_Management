import os
import sys


with open("Ticapsoriginal_Marketing.txt", 'rU') as j:
    for line in j:
        line = line.strip().split()
        filename = " ".join([i for i in line])
        full_path = "marketingarquitecturefolders" + "/" + filename
        os.mkdir(full_path) 
