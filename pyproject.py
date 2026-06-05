import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
root = tk.Tk()
root.config(bg="#BDCAEB",relief='groove')
root.title('The Simple Painting Demo')
frame1 = tk.Frame(root,height=100,bg='white',background='#BDCAEB')
frame1.grid(row=0,column=0)
frame2 = tk.Frame(root,height=500,background='#BDCAEB')
frame2.grid(row=1,column=0)
frame3 = tk.Frame(root,height=100,background='#BDCAEB')
frame3.grid(row=1,column=1,sticky='n')

colour_name_label = ttk.Label(frame1,text="Enter colour name : ",background='#BDCAEB',font=('Corier',8,'bold'))
size_label =ttk.Label(frame1,text="Enter size of brush : ",background='#BDCAEB',font=('Corier',8,'bold'))
coulur_sheet_label = ttk.Label(frame1,text="Enter sheet colour : ",background='#BDCAEB',font=('Corier',8,'bold'))
colour_name_label.grid(row=0,column=0,padx=10,pady=10)
size_label.grid(row=0,column=2,padx=10,pady=10)
coulur_sheet_label.grid(row=0,column=4,padx=10,pady=10)

brush_size = tk.ttk.Combobox(frame1,values=[x for x in range(10,101,2)],state='readonly',width=5)
brush_size.set(26)
brush_size.grid(row=0,column=3,padx=10,pady=10)

brush_colour = tk.ttk.Entry(frame1,width=15)
brush_colour.grid(row=0,column=1,padx=10,pady=10)
brush_colour.insert(0,"black")

sheet_colour = ttk.Entry(frame1,width=15)
sheet_colour.grid(row=0,column=5,padx=10,pady=10)
sheet_colour.insert(0,'white')

canvas = tk.Canvas(frame2,width=1000,height=1000,cursor='hand2',highlightbackground='black',bg='white')
canvas.grid(row=0,column=0,sticky='e',padx=20)

def draw(event):
    try:
        a,b = event.x,event.y
        cs = int(brush_size.get())
        global clr
        clr = brush_colour.get()
        canvas.create_text(a,b,text='•',font=("Arial",cs),fill=clr)
    except:
        messagebox.showerror('Error','color is not found')

def reset():
    canvas.create_rectangle(0,0,1001,1001,fill=sheet_colour.get(),width=0) 
    brush_colour.delete(0,tk.END)
    brush_colour.insert(0,clr)
    
def set_sheet():
    try:
        sheetcrl = sheet_colour.get()
        canvas.create_rectangle(0,0,1001,1001,fill=sheetcrl,width=0)
    except:
        messagebox.showerror('Error','color is not found')

def er():
    global co
    if co == 1:
        brush_colour.delete(0,tk.END)
        brush_colour.insert(0,sheet_colour.get())
        co = 0
    elif co == 0:
        brush_colour.delete(0,tk.END)
        brush_colour.insert(0,clr)
        co = 1

Opt = ttk.Label(frame3,text="Options",font=('Corier',12,'bold','underline'),background="#BDCAEB")
Opt.grid(row=0,column=0,columnspan=2)

reset = ttk.Button(frame3,text="reset",command=reset)
reset.grid(row=1,column=0,pady = 40)
co = 1
eraser = ttk.Button(frame3,text="Eraser",command=er)
eraser.grid(row=1,column=1)

enterb = ttk.Button(frame1,text="Enter",command=set_sheet)
enterb.grid(row=0,column=6)

can = tk.Canvas(frame3,height=800,width=800,background='#BDCAEB',highlightbackground='#BDCAEB')
can.grid(row=2,column=0,columnspan=10)
can.create_text(400,200,text='Simple',font=('Times New Roman',32,"bold italic"),fill="#3A0A61")
can.create_text(400,300,font=('Times New Roman',36,'bold italic'),text='Painting',fill="#3A0A61")
can.create_text(400,400,fill='#3A0A61',font=('Times New Roman',32,'bold italic'),text='Application')
canvas.bind('<B1-Motion>',draw)
root.mainloop()