from tkinter import *
from video_file import video
from BicepApplication import bicepwindow
class window:
    def __init__(self,root):
        self.window = root
        self.window.title("Welcome to trAIner application")

        self.window.geometry("1280x800+0+0")
        self.window.config(bg="cyan")

        self.frame3 = Frame(self.window, bg="white")
        self.frame3.place(x=140,y=150,width=1000,height=450)

        self.video_button = Button(self.frame3,text="Click for Video",command=self.video_func,font=("times new roman",25, "bold"),bd=0,cursor="hand2",bg="blue",fg="white").place(x=250,y=100,width=500)
        self.video_button = Button(self.frame3,text="Click for Bicep Exercise",command=self.curl_func,font=("times new roman",25, "bold"),bd=0,cursor="hand2",bg="blue",fg="white").place(x=250,y=250,width=500)
    def video_func(self):
        self.window.destroy()

        root=Tk()
        obj=video(root)
        root.mainloop()
    
    def curl_func(self):
        self.window.destroy()
        root=Tk()
        obj=bicepwindow(root)
        root.mainloop()

if __name__ == "__main__":
    root = Tk()
    obj = window(root)
    root.mainloop()