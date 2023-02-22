from tkinter import *
from curl_counter import curlcount
from rightbicep import rightcurlcount
from bb import bbcurlcount
from squat import squatcount
from pushup import pushupcount
class bicepwindow:
    def __init__(self,root):
        self.window = root
        self.window.title("Welcome to trAIner application")
        self.window.geometry("1280x800+0+0")
        self.window.config(bg="cyan")

        self.frame3 = Frame(self.window, bg="white")
        self.frame3.place(x=140,y=100,width=1000,height=550)

        self.video_button = Button(self.frame3,text="Left Bicep Exercise",command=self.left_func,font=("times new roman",25, "bold"),bd=0,cursor="hand2",bg="blue",fg="white").place(x=250,y=50,width=500)
        self.video_button = Button(self.frame3,text="Right Bicep Exercise",command=self.right_func,font=("times new roman",25, "bold"),bd=0,cursor="hand2",bg="blue",fg="white").place(x=250,y=150,width=500)
        self.video_button = Button(self.frame3,text="Barbell Curl Exercise",command=self.bb_func,font=("times new roman",25, "bold"),bd=0,cursor="hand2",bg="blue",fg="white").place(x=250,y=250,width=500)
        self.video_button = Button(self.frame3,text="Squat Exercise",command=self.squat_func,font=("times new roman",25, "bold"),bd=0,cursor="hand2",bg="blue",fg="white").place(x=250,y=350,width=500)
        self.video_button = Button(self.frame3,text="Pushup Exercise",command=self.pushup_func,font=("times new roman",25, "bold"),bd=0,cursor="hand2",bg="blue",fg="white").place(x=250,y=450,width=500)

    def left_func(self):
        self.window.destroy()

        root=Tk()
        obj=curlcount(root)
        root.mainloop()
    
    def right_func(self):
        self.window.destroy()

        root=Tk()
        obj=rightcurlcount(root)
        root.mainloop()
    
    def bb_func(self):
        self.window.destroy()

        root=Tk()
        obj=bbcurlcount(root)
        root.mainloop()

    def squat_func(self):
        self.window.destroy()

        root=Tk()
        obj=squatcount(root)
        root.mainloop()
    def pushup_func(self):
        self.window.destroy()

        root=Tk()
        obj=pushupcount(root)
        root.mainloop()
if __name__ == "__main__":
    root = Tk()
    obj = bicepwindow(root)
    root.mainloop()