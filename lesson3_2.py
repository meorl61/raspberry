import tkinter as tk #module or package

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('這是第一個視窗')  #在java 用this
        self.geometry('400x200')
        self.resizable(False,False)        

if __name__ == "__main__":
    #window = tkinter.Tk()
    #window = tk.Tk()
    window = Window()

    #window.title('GUI')
    #window.geometry('380x400')
    #window.resizable(False,False)
    window.mainloop()