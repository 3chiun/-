import tkinter as tk

win_0 = tk.Tk()

#set
win_0.title("EN TEST")
win_0.geometry("640x640+300+50")#+:定位初始位置 == win.geometry("長*寬+x+y")
win_0.config(bg="#323232")

#setup
img = tk.PhotoImage(file="D:/im_project/資料/廢圖/真好吃.PNG")
def changeLB():
    txt = en_1.get()
    lb_1.config(text=txt)




#Label
lb_1 = tk.Label(bg="#323232", text="label 1 ", fg="white")
lb_1.pack()

#entry
en_1 = tk.Entry()  
en_1.pack()

#button
# btn_1 = tk.Button(text="btn", bg="skyblue", width=10, height=5, )
btn_2 = tk.Button(image=img, command=changeLB)
    #非像素設定，是以當前視窗的網格
# btn_1.pack()
btn_2.pack()

tk.mainloop()
