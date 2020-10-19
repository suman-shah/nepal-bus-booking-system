from tkinter import*
from PIL import*
from tkinter.ttk import Combobox
root=Tk()
root.title('Bus Ticket Booking System V 2.0.7.7.0.3')
w=root.winfo_screenwidth()
h=root.winfo_screenwidth()
root.geometry("%dx%d+0+0"%(w,h))
#=====================top 3 common frames=====================

frame1=Frame(root,width=(w),height=100,bd=10,relief="raise")
frame1.pack(side=TOP,fill=BOTH)
frame2=Frame(root,width=(w),height=50,bd=5,relief="raise")
frame2.pack(side=TOP,fill=BOTH)
frame3=Frame(root,width=(w),height=500,relief="raise")
frame3.pack(side=LEFT,fill=BOTH)
listofbuss=[1,2,3,4]
#===================frame1-label================================
frame1_label=Label(frame1,text=" Bus Ticket Booking System\t\t\t",font=('Arial',40,'bold'),bg='green',fg='white').pack()
#===============frame2-buttons===============
frame2_button1=Button(frame2,text='Dashboard',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=0)
frame2_button2=Button(frame2,text='Add Bus',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=1)
frame2_button3=Button(frame2,text='Add Route',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=2)
frame2_button4=Button(frame2,text='View Route',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=3)
frame2_button5=Button(frame2,text='Bus Report',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=4)
frame2_button6=Button(frame2,text='Logout',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=5)
#================frame 3-add bus labels and entry wizrad=======================
Label(frame3,text='ADD NEW ROUTE',font=('Arial',20,'bold')).grid(row=0)
Label(frame3,text='Select Bus',font=('Arial',15,'bold')).grid(row=1,column=0,sticky=W)
fbusdestination_cobobox=Combobox(frame3,width=36,state='readonly',font=('arial',11,'bold'))
fbusdestination_cobobox['value']=listofbuss
fbusdestination_cobobox.grid(row=1,column=1)
fbusdestination_cobobox.current(0)

Label(frame3,text='Route:',font=('Arial',15,'bold')).grid(row=2,column=0,sticky=W)
Entry(frame3,width=50,bd=5).grid(row=2,column=1)

Label(frame3,text='Distance:',font=('Arial',15,'bold')).grid(row=3,column=0,sticky=W)
Entry(frame3,width=50,bd=5).grid(row=3,column=1)

Label(frame3,text='Fare:',font=('Arial',15,'bold')).grid(row=4,column=0,sticky=W)
Entry(frame3,width=50,bd=5).grid(row=4,column=1)


#==================Add bus button============
Button(frame3,text='Add Route',font=('Arial',25,'bold'),bg='black',fg='white').grid(row=9,column=1)


root.mainloop()
