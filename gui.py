import tkinter as tk
import os
from tkinter import *

root = tk.Tk()

root.configure(background='#1b1b1b')
root.geometry("600x300")

#this is the part u should look at niscal
def Performanceboost():
    os.system("git clone https://github.com/W4RH4WK/Debloat-Windows-10.git")
    #the rest of the script will be written in performance
    os.system("./Performance")
def Update():
    os.system("git clone https://github.com/p978/rip-off.git")
    os.system("cd rip-off")
def Taskmanager():
    os.system("taskmgr")
def logout():
    os.system("logoff")
def restart():
    os.system("reboot /s")
def Shutdown():
    os.system("shutdown /s")
def restartexplorer():
    os.system("taskkill /f /im explorer.exe")
    os.system("start explorer.exe")
explorer = tk.Button(root, 
            width=20,
            text ="Restart explorer",
            bg ="#263D42",
            command=restartexplorer)
explorer.pack()

Shutdown = tk.Button(root,
                width=20,
                text ="Shutdown",
                bg ="#263D42",
                command=Shutdown)
Shutdown.pack()

OpenTaskManager = tk.Button(root,
                         width=20,
                         text="Open Task Manager",
                         bg="#263D42",
                         command=Taskmanager)
OpenTaskManager.place(x=1, y=100)

Update = tk.Button(root, 
                width=10,
                text="Update",
                bg="#263d42",
                command=Update)
Update.place(x=510, y=100)




root.mainloop()
