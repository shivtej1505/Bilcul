from Tkinter import *
from tkMessageBox import *
import subprocess as viewbill
billgenerator=__import__("bill")
root=Tk()
root.title("Bill Calculator & Generator")
root.geometry('600x400+200+200')
root.resizable(width=FALSE,height=FALSE)

top=Frame(root,borderwidth=1,relief=RAISED)
top.pack(side=TOP,fill=BOTH,ipady=5,padx=100)
note=StringVar(root)

def set_notify(text):
    note.set(text)

set_notify("Notification will be Shown here.")
notify=Label(top,textvariable=note).pack()

def kill(p):
    p.destroy()

def area_select():
    if region.get()=='Urban':
        kill(area_o)
        kill(bo)
        area_s=OptionMenu(f2,area,'U1','U2','U3')
        area_s.pack(side=LEFT)
        Button(f2,text="OK",command=select_type).pack(side=LEFT)
    elif region.get()=='Rural':
        kill(area_o)
        kill(bo)
        area_s=OptionMenu(f2,area,'R1','R2','R3')
        area_s.pack(side=LEFT)
        Button(f2,text="OK",command=select_type).pack(side=LEFT)
    else:
        set_notify("Please select region.")

def testing():
    print "button"

def Genbill(name):
    billgenerator.make_pdf(name,unit.get(),area.get(),region.get(),Type.get(),unit.get())
    showinfo('Positive',"Bill generated for %s" %name)
    viewbill.call(["evince","bill.pdf"])

def select_type():
    if area.get()=="Select Area":
        set_notify("Please select area.")

def calculate(unit):
    if area.get()=="Select Area" or (region.get()!="Urban" and region.get()!="Rural") or Type.get()=="Select Type":
        set_notify("Please select area/region/type.")
        return
    msg='Amount calculated is '+str(unit.get())+".\nArea="+Type.get()+".\n"
    if(B):
        f5=Frame(root)
        name=StringVar(f5)
        Label(f5,text="Consumer's name:").pack(side=LEFT)
        Entry(f5,textvariable=name).pack(side=LEFT)
        Button(f5,text="Get Bill",command=lambda:Genbill(name.get())).pack(side=LEFT)
        f5.pack(side=TOP,padx=10,pady=10)
    showinfo('Positive',msg)

f1=Frame(root)
l1=Label(f1,text='Region : ').pack(side=LEFT)
region=StringVar(f1)
region.set("Select Region")
option=OptionMenu(f1,region,'Urban','Rural')
option.pack(side=LEFT)
Button(f1,text="OK",command=area_select).pack(side=LEFT)
f1.pack(pady=10,padx=10,side=TOP)

f2=Frame(root)
l2=Label(f2,text='Area').pack(side=LEFT)
area=StringVar(f2)
area.set("Select Area")
area_o=OptionMenu(f2,area,'')
area_o.pack(side=LEFT)
bo=Button(f2,text="OK",command=select_type)
bo.pack(side=LEFT)
f2.pack(pady=10,padx=10,side=TOP)

f3=Frame(root)
Label(f3,text="Select Type").pack(side=LEFT)
Type=StringVar()
Type.set("Select type.")
types=OptionMenu(f3,Type,'Industry','Agriculture','Domestic','Commertial','Railway','Other')
types.pack(side=LEFT)
f3.pack(pady=10,padx=10,side=TOP)

f4=Frame(root)
unit=DoubleVar(f4)
Elabel=Label(f4,text="No. of Units").pack(side=LEFT)
E=Entry(f4,textvariable=unit).pack(side=LEFT)
Button(f4,text="Submit",command=lambda:calculate(unit)).pack(side=LEFT)
B=IntVar()
bill=Checkbutton(f4,text="Generate Bill",variable=B).pack()
f4.pack(pady=10,padx=10,side=TOP)

last=Frame(root,borderwidth=1,relief=RAISED)
last.pack(side=BOTTOM,fill=BOTH,ipady=4)
Button(last,text='Exit',command=root.quit).pack(side=BOTTOM)

root.mainloop()
