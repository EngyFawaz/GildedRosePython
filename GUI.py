from tkinter import *
from gilded_rose import Item, GildedRose
import threading

items = []
Status_label = None
label_4 = None

def CreateItems ():
    global label_4
    Name =  str(entry_1.get())
    Sell_in = int(entry_2.get())
    Quality =  int(entry_3.get())
    
    if (Sell_in < 0 or Quality < 0):
        label_4.configure(text="invalid values")
        return
        
    new_item = Item(Name, Sell_in , Quality)
    items.append(new_item)
    print(items)

def set_interval(func, sec):
   def func_wrapper():
       set_interval(func, sec) 
       func()  
   t = threading.Timer(sec, func_wrapper)
   t.start()
   return t



def CreateWindow ():
    global Status_label
    root = Tk()
    root.geometry('400x400')
    root.title("Items List")
    text = StringVar()
    Status_label = Label(root, text = "Waiting for the update of the items", width=100 ,font=("bold", 10))
    
    
    set_interval(showStatus,10)

    Status_label.pack()
    root.mainloop()
    
 
def showStatus ():
    global Status_label
    if Status_label == None:
        return

    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    text_items = map(lambda item : "Name: "+str(item.name) + " ,Sell_in: "+ str(item.sell_in)+ " ,Quality: "+str(item.quality)  , items)
    Status_label.configure(text='\n'.join(text_items))
    
        
        
    
root = Tk()
root.geometry('500x500')
root.title("Item List")

label_0 = Label(root, text="Item List",width=20,font=("bold", 20))
label_0.place(x=90,y=53)

label_1 = Label(root, text="Name",width=20,font=("bold", 10))
label_1.place(x=68,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Sell-in",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root)
entry_2.place(x=240,y=180)


label_3 = Label(root, text="Quality",width=20,font=("bold", 10))
label_3.place(x=70,y=220)

entry_3 = Entry(root)
entry_3.place(x=240,y=220)



Button(root, text='Submit',width=20,bg='brown',fg='white' , command = CreateItems).place(x=180,y=280)
Button(root, text='Check Status',width=20,bg='brown',fg='white', command = CreateWindow ).place(x=180,y=320)


label_4 = Label(root, text= "" ,width=20,font=("bold", 10))
label_4.place(x=70,y=470)



root.mainloop()


    


