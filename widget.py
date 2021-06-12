import transfer
import os
# 这里我们提供必要的引用。基本控件位于pyqt5.qtwidgets模块中。
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image,ImageTk
class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.styleSelect = ttk.Combobox()
        self.styleSelect['state'] = 'readonly'
        self.transferBtn = tk.Button(self, text="转换")
        self.contentSelectBtn = tk.Button(self,text="选择图片",command=self.selectContent)
        self.contentImage = tk.Label()
        self.transferedImage =tk.Label()
        self.label1 = tk.Label(text='迁移前')
        self.label2 = tk.Label(text='迁移后')
        self.initUi()
        self.setCommand()
        self.loadStyle()

    def initUi(self):
        self.geometry("1200x600")
        self.styleSelect.grid(columnspan=3)
        self.transferBtn.grid(column=4,row=0)
        self.contentSelectBtn.grid(column=3,row=0,)
        self.contentImage.grid(row=2,rowspan=2,column=1,columnspan=3)
        self.transferedImage.grid(row=2,rowspan=2,column=4,columnspan=3)
        self.label1.grid(row=1,column=3)
        self.label2.grid(row=1,column=8)

    def setCommand(self):
        self.transferBtn.bind("<Button-1>",self.transfer)
        self.contentSelectBtn.bind("<Button-1>",self.selectContent)

    def loadStyle(self):
        styles = os.listdir("samples_styles")
        self.styleSelect.config(value=styles)
        self.styleSelect.current(0)

    # 选择内容图片
    def selectContent(self,event):
        default_path = os.getcwd()+"/content"
        fileName = filedialog.askopenfilename(title=u'选择文件',initialdir=default_path)
        if fileName != "":
            image1 = Image.open(fileName)
            # 调整大小
            windowWidth = self.winfo_width()
            windowHeight = self.winfo_height()*0.8
            width = int(windowWidth/2)
            height = int(windowHeight)
            image2 = ImageTk.PhotoImage(image1.resize((width, height), Image.ANTIALIAS))
            self.contentImage.config(image=image2)
            self.contentImage.image = image2
            self.contentImage.config(text=fileName)

    def transfer(self,event):
        style = self.styleSelect.get()
        if style=="":
            print("请选择风格")
            return
        contentImagePath = self.contentImage.cget("text")
        if contentImagePath == "":
            print("请选择图片")
            return
        content = contentImagePath.split("/")[-1]
        transferedImagePath = transfer.transfer(style,content)
        image = Image.open(transferedImagePath)
        windowWidth = self.winfo_width()
        windowHeight = self.winfo_height() * 0.8
        width = int(windowWidth / 2)
        height = int(windowHeight)
        outcomeImg = ImageTk.PhotoImage(image.resize((width,height),Image.ANTIALIAS))
        self.transferedImage.config(image=outcomeImg)
        self.transferedImage.image = outcomeImg

# content_image='scnu.jpg'
# style_name = '卡通1'

if __name__ == '__main__':
    win = MainWindow()
    win.mainloop()
