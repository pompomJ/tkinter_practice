#coding:utf-8
import tkinter as tk

root = tk.Tk() # ウインドウ作成
root.title(u"tkinter")
root.geometry("400x300") # xの前後にはスペースを入れないこと！

# ラベル
Static1 = tk.Label(text=u'practice', font = ('MS Gothic', 20), foreground = '#FF00FF', background = 'cyan')
Static1.pack()

root.mainloop() # ウインドウ表示
