from tkinter import *
import tkinter as tk

def add_task(task_enter, listbox, task_list):
    task= task_enter.get()
    task_enter.delete(0,END)

    if task:
        with open ("tasklist.txt","a")as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task)

def delete_task(listbox, task_list):
    task = str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt", "w") as taskfile:
            for task in task_list:
                taskfile.write(task + "\n")
        listbox.delete(ANCHOR)

      
def view_task(listbox, task_list):
    try:
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()
        for task in tasks:
            if task.strip():  
                task_list.append(task.strip())  
                listbox.insert(END, task.strip())  
    except FileNotFoundError:
        pass





def main():
    root=Tk()
    root.title("TO-DO LIST")
    root.geometry("500x600")

    this_is_icon=PhotoImage(file="images/icon.png")
    root.iconphoto(False,this_is_icon)

    attop=PhotoImage(file="images/topbar.png")
    Label(root,image=attop).pack()

    top_image=PhotoImage(file="images/toplogo.png")
    Label(root,image=top_image,bg="#febb55").place(x=1,y=1.5)
    task_list=[]

    heading=Label(root,text="TaskTracker",font="arial 26 bold",fg="#545454",bg="#febb55")
    heading.place(x=200,y=50)

    frame=Frame(root,width=480,height=50,bg="#545454")
    frame.place(x=10,y=150)

    task=StringVar()
    global task_enter
    task_enter=Entry(frame,width=25,font="arial 20",fg="#545454",bd=0)
    task_enter.place(x=15,y=5)
    task_enter.focus()

    add_button=Button(frame,text="ADD",font="arial 15 bold",width=4,bg="#febb55",fg="white",bd=0,command=lambda: add_task(task_enter, listbox, task_list))
    add_button.place(x=400,y=6)


    to_do_frame=Frame(root,width=1000,height=150,bg="#545454")
    to_do_frame.place(x=0,y=210)
     
     
    listbox=Listbox(to_do_frame,font=('arial',15),width=80,height=16,bg="#545454",fg="white",cursor="hand2")
    listbox.pack(side="left",fill=BOTH,padx=2)
    view_task(listbox,task_list)

    
    delete_icon=PhotoImage(file="images/deleteicon.png")
    Button(root,image=delete_icon,bd=0,command=lambda: delete_task(listbox, task_list)).pack(side=BOTTOM)
    
    
  




    root.mainloop()   

if __name__=="__main__":
    main()