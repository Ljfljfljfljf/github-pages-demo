# 李俊飞
'''
tk.Frame。Frame是一个独立的容器，可以包含多个其它的Tkinter组件
Frame的常见属性与方法：
bd：边框宽度，默认是2像素。
bg或background：背景颜色。
relief：边框样式，常用的取值有flat（平的）、groove（凸起）、raised（凸出）等。
pack()：将Frame添加到父容器中，并根据需要进行缩放和布局。同时，也可以使用side参数指定在父容器中的位置。
grid()：使用网格布局方式将Frame添加到父容器中。

Menu常用的方法和属性：
add_command()：向菜单中添加一个普通菜单项。
add_checkbutton()：向菜单中添加一个复选框菜单项。
add_radiobutton()：向菜单中添加一个单选按钮菜单项。
add_cascade()：向菜单中添加子菜单。
entryconfig()：获取或设置菜单项的属性，例如名称、状态、快捷键等。
'''
#---------导入库----
import webbrowser
import tkinter as tk
from tkinter import messagebox
#-------------函数----
def mybutton():
    messagebox.showinfo('Message','ljf')
def mymenu():
    messagebox.showinfo('Message','ljf')
def get_selected_value():
    selected_value = my_invar.get()
    print("选中的值是:", selected_value)
def get_entry_text():
    selected_value = my_stringvar.get()
    print("输入的是:", selected_value)
#创建窗口
my_window=tk.Tk(className='ljf')
#Flame空间
my_flame1=tk.Frame(my_window)
my_flame2=tk.Frame(my_window)
#可变的整数对象
my_invar=tk.IntVar()
#可变的字符串对象
my_stringvar=tk.StringVar()
#标签
my_lable1=tk.Label(my_flame1,text='请输入:',padx=100,pady=100)
my_lable2=tk.Label(my_flame1,text='请输入:',pady=100)
my_button=tk.Button(my_flame1,text='ljf',font=('楷体',12),fg='red',command=get_entry_text,width=3,height=1)
#创建单选按钮
my_radiobutton1=tk.Radiobutton(my_flame1,text='ljf',variable=my_invar,value=10,width=10,height=1)
my_radiobutton2=tk.Radiobutton(my_flame1,text='ljf',variable=my_invar,value=4,width=10,height=1)
#创建文本输入框
my_entry=tk.Entry(my_flame1,textvariable=my_stringvar,highlightcolor='Fuchsia',highlightthickness=1,width=35)
#创建菜单条
my_menu_bar=tk.Menu(my_window)
#创建菜单
my_menu=tk.Menu(my_menu_bar,tearoff=0)
#绑定
my_menu_bar.add_cascade(label='菜单条',menu=my_menu)
#添加菜单项
my_menu.add_command(label='菜单项',command=mymenu)
my_menu.add_command(label='菜单项',command=mymenu)
my_menu.add_command(label='菜单项',command=mymenu)
my_menu.add_command(label='菜单项',command=mymenu)
my_menu.add_command(label='菜单项',command=mymenu)
my_menu.add_command(label='腾讯视频',command=lambda:webbrowser.open('http://v.qq.com/'))
my_menu.add_command(label='搜狐视频',command=lambda:webbrowser.open('http://tv.sohu.com/'))
my_menu.add_command(label='芒果TV',command=lambda:webbrowser.open('http://www.mqtv.com/'))
my_menu.add_command(label='爱奇艺',command=lambda:webbrowser.open('http://www.iqiyi.com/'))
my_menu.add_command(label='优酷',command=lambda:webbrowser.open('http://www.youku.com/'))
my_menu.add_command(label='乐视',command=lambda:webbrowser.open('http://www.le.com/'))
my_menu.add_command(label='土豆',command=lambda:webbrowser.open('http://www.tudou.com/'))
my_menu.add_command(label='A站',command=lambda:webbrowser.open('http://www.acfun.com/'))
my_menu.add_command(label='B站',command=lambda:webbrowser.open('http://www.bilibili.com/'))
#-------添加---
my_lable1.grid(row=0,column=0)
my_lable2.grid(row=0,column=1)
my_button.grid(row=1,column=0)
my_radiobutton1.grid(row=1,column=1)
my_radiobutton2.grid(row=2,column=1)
my_entry.grid(row=2,column=0)
my_flame1.pack()
#将菜单条设置成窗口的菜单条
my_window.configure(menu=my_menu_bar)
my_window.mainloop()
