from tkinter import *
import random 
root=Tk()
root.title("Picnic bag list")
root.geometry("800x500")

item_list=Label(root)
rand_no=Label(root)
list1=["Mat","Food","Water","Drinks"]
item_list["text"]= "Listed Items : " + str(list1)

def r_item():
    rand_item=random.randint(0,4)
    rand_no["text"] = "Put Item No. " + str(rand_item) + " In Bag"

item_list.place(relx = 0.5, rely = 0.4, anchor = CENTER)    
btn = Button(root, text = "Which Item To Put In Bag ?", command = r_item)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)
rand_no.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()