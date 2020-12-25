import subprocess
import os.path
import tkinter as tk
from tkinter import *
#ip = input('Ingresa la ip a escanear')   #Reemplazar por path con txt de ip's
#passwd = input('Ingresa password de administrador: ')
#subprocess.run('sudo su', shell=True)
#subprocess.run(str(passwd), shell=True)

#list_path = input('set .txt file route: ')


root = tk.Tk()
root.title("IP locator")

path_ = StringVar()
list_path = Entry(root, width=40, text='Set .txt directory', textvariable=path_)
list_path.grid(column=3, row=1)


true_path = True

lbl = Label(root, text="Set. TXT file route", font=("Arial Bold", 0))
lbl.grid(column=2,row=1)
root.geometry('450x300')

def locator():
    if true_path == True:
        ls = open(path_.get(), 'r')
        lines = ls.read().splitlines()       
        for ip in lines:
            ip_to_scan = 'ipinfo.io/'+ str(ip)
            scan = subprocess.check_output(['curl', str(ip_to_scan)])
            str(scan).strip('}{')
            list(scan)
            new_list = open('mod_list.txt', 'a', encoding="utf-8")
            new_list.write('%s\n%s'  %(str(ip), scan.decode("utf-8")))
        
    else:
        print('Wrong path...')


start_bttn = Button(root, text='Start scan', command=locator)
start_bttn.grid(column=3, row=2)

root.mainloop()

# C:\Users\giuli\Documents\GitHub\IP_locator\ip_list.txt