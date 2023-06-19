import tkinter as tk #module or package
from tkinter import ttk #module or package
from gpiozero import LED
import datasource  #檔案名



class LEDButton(ttk.Button):
    def __init__(self,master,led,**kwargs):
        super().__init__(master,**kwargs)
        self.led=led
        self.state=False
        self.configure(command=self.user_click)
        s=ttk.Style()
        s.theme_use('clam')
        s.configure('LEDClose.TButton',
                    foreground='red',
                    font=('Arial','20'),borderwidth=5,
                    padding=(10,20),)
        s.configure('LEDOpen.TButton',
                    foreground='red',
                    background='yellow',
                    font=('Arial','20'),
                    borderwidth=5,
                    padding=(10,20),)
    
    def user_click(self):
        self.state = not self.state  #否定運算子        
        if self.state:
            self.configure(text='LED 開')
            self.configure(style='LEDOpen.TButton')
            self.led.on()
            datasource.insert_data(1)
        else:
            self.configure(text='LED 關')
            self.configure(style='LEDClose.TButton')
            self.led.off()
            datasource.insert_data(0)
       

class Window(tk.Tk):
    def __init__(self,redLed,**kwargs):
        ''' 多行文字說明
        @parmater redLed, 是gpiozero.LED 的實體
        '''
        super().__init__(**kwargs)
        #self.redLed=redLed        
        self.title('這是第一個視窗')  #在java 用this
        #self.geometry('400x200')   //設定視窗大小
        self.resizable(False,False)        
        s=ttk.Style()
        s.theme_use('clam')
        #s.configure('TLabel',foreground='red',background='yellow')        
        s.configure('Title.TLabel',foreground='blue',background='lavender',font=('Arial','20'))
        #s.configure('Led.TButton',foreground='red',background='yellow',font=('Arial','20'),borderwidth=5,padding=(10,20))
        
        #print(s.layout('Led.TButton'))
        #title_label = tk.Label(self,bg='yellow',text="LED控制",font=('Helvetica','16') )
        #title_label.pack(pady=25,padx=100)
        title_label = ttk.Label(self,text="LED控制器",style='Title.TLabel')
        title_label.pack(pady=25,padx=100)

        ##self ,傳給 master
        self.led_btn = LEDButton(self,led=redLed,text="LED 開",
                                 style='LEDClose.TButton',                                
                             )
        self.led_btn.pack(pady=(10,50))   


if __name__ == "__main__":
    datasource.sayHellow()

    #conn = datasource.create_connection('iot.db')
    #datasource.create_table(conn)
    #datasource.insert_data(conn,1)
    datasource.insert_data(1)
    led=LED(23)
    led.off()
    #window = tkinter.Tk()
    #window = tk.Tk()
    window = Window(led)
    #window.title('GUI')
    #window.geometry('380x400')
    #window.resizable(False,False)
    
    window.mainloop()


    