import tkinter as tk

class Window(tk.Tk):
    def __init__(self):  #self 可省略
        super().__init__()
        self.title("Hello 蝦米碗")

        label = tk.Label(self, text="嘿嘿~~Hello World!")
        label.pack(fill=tk.BOTH, expand=1, padx=100, pady=50)


if __name__ == "__main__":
    window = Window()
    window.mainloop() #視窗不會關閉