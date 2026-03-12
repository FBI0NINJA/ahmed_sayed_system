import requests
import tkinter as tk
from tkinter import messagebox
import webbrowser
import subprocess


def activate():
    key = entry.get()

    try:
        url = "http://localhost/license_server/verify.php"
        response = requests.post(url, data={"license": key})
        data = response.json()

        if data["status"] == "valid":
            messagebox.showinfo("تم الدخول","الكود مفعل")
            subprocess.Popen(["python","snake_game.py"])
            
        else:
            messagebox.showerror("خطأ","الكود غير مفعل")

    except:
        messagebox.showerror("Server Error","Cannot connect to server")
def open_facebook():
    webbrowser.open("https://www.facebook.com/ninjafbi1")

def open_github():
    webbrowser.open("https://github.com/FBI0NINJA")

root = tk.Tk()
root.title("Ahmed Sayed Software Activation")
root.geometry("500x400")
root.config(background='red')

label = tk.Label(root,text="coding Ahmed Sayed" ,bg='red' ,fg='white' ,font='15')
label.pack(pady=15)
label.place(x=10,y=200)

label = tk.Label(root,text="Enter License Key" ,bg='black' ,fg='white')
label.pack(pady=15)

entry = tk.Entry(root,width=50)
entry.pack()

btn = tk.Button(root,text="Activate",command=activate ,bg='blue' ,fg='white')
btn.pack(pady=20)

btn = tk.Button(root,text="Facebook",command=open_facebook,bg="red",fg="white")
btn.place(x=190,y=200)

btn = tk.Button(root,text="GitHub",command=open_github,bg="red",fg="white")
btn.place(x=260,y=200)


root.mainloop()
