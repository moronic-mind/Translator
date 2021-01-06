import encryption as cipher
import decryption as decipher   

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

import gui_support

def vp_start_gui():
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    gui_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    gui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'  
        _fgcolor = '#000000'
        _compcolor = '#d9d9d9'
        _ana1color = '#d9d9d9'
        _ana2color = '#ececec'

        top.geometry("902x600+385+154")
        top.minsize(100, 1)
        top.maxsize(1924, 1030)
        top.resizable(1, 1)
        top.title("Translator")
        top.configure(background="black")

        self.text1 = tk.Entry(top)
        self.text1.place(relx=0.089, rely=0.333,height=174, relwidth=0.304)
        self.text1.configure(background="white")
        self.text1.configure(font="TkFixedFont")
        self.text1.configure(foreground="#000000")
        self.text1.configure(insertbackground="black")

        self.text1_1 = tk.Message(top)
        self.text1_1.place(relx=0.621, rely=0.333,height=174, relwidth=0.304)
        self.text1_1.configure(background="white")
        self.text1_1.configure(font="TkFixedFont")
        self.text1_1.configure(foreground="#000000")
        self.text1_1.configure(highlightbackground="#d9d9d9")
        self.text1_1.configure(highlightcolor="black")
        self.text1_1.configure(width=100)
        
        def call():
            plain_text =self.text1.get().upper()
            ans=cipher.encryptor(plain_text)
            #print(ans)
            self.text1_1.configure(text=ans)

        def get():
            encrypted_text =self.text1.get()
            x=decipher.decryptor(encrypted_text)
            self.text1_1.configure(text=x)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.443, rely=0.383, height=33, width=106)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="green")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Encryption''',command=call)

        self.Button1_2 = tk.Button(top)
        self.Button1_2.place(relx=0.443, rely=0.5, height=33, width=106)
        self.Button1_2.configure(activebackground="#ececec")
        self.Button1_2.configure(activeforeground="#000000")
        self.Button1_2.configure(background="#d9d9d9")
        self.Button1_2.configure(disabledforeground="#a3a3a3")
        self.Button1_2.configure(foreground="#000000")
        self.Button1_2.configure(highlightbackground="green")
        self.Button1_2.configure(highlightcolor="black")
        self.Button1_2.configure(pady="0")
        self.Button1_2.configure(text='''Decryption''',command=get)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.356, rely=0.067, height=30, width=242)
        self.Label1.configure(background="black")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="white")
        self.Label1.configure(text='''Translator''',font=("arial",30))

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.1, rely=0.283, height=26, width=252)
        self.Label2.configure(background="black")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="white")
        self.Label2.configure(text='''Input''',font=("arial",15))

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.632, rely=0.283, height=26, width=252)
        self.Label3.configure(background="black")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="white")
        self.Label3.configure(text='''Output''',font=("arial",15))

if __name__ == '__main__':
    vp_start_gui()