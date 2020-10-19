from tkinter import*
from PIL import*
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
frame4=Frame(root,width=(w),height=500,relief="raise")
frame4.pack(side=RIGHT,fill=BOTH)
#===================frame1-label================================
frame1_label=Label(frame1,text=" Bus Ticket Booking System\t\t\t",font=('Arial',40,'bold'),bg='green',fg='white').pack()
#===============frame2-buttons===============
frame2_button1=Button(frame2,text='Dashboard',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=0)
frame2_button2=Button(frame2,text='Add Bus',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=1)
frame2_button3=Button(frame2,text='Add Route',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=2)
frame2_button4=Button(frame2,text='View Route',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=3)
frame2_button5=Button(frame2,text='Bus Report',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=4)
frame2_button6=Button(frame2,text='Logout',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=5)

admin_bus_iamge=PhotoImage(file='volkswagen-158463_640.png')
admin_bus_iamge_label=Label(frame4,image=admin_bus_iamge).pack()
#===========das board==============
das_button=Button(frame3,text='Dashboard',font=('Arial',16,'bold'),bg='black',fg='white',width=30,bd=1).pack()
addbus_button=Button(frame3,text='Add Bus',font=('Arial',16,'bold'),bg='black',fg='white',width=30,bd=1).pack()
addroute_button=Button(frame3,text='Add Route',font=('Arial',16,'bold'),bg='black',fg='white',width=30,bd=1).pack()
viewr_button=Button(frame3,text='View Route',font=('Arial',16,'bold'),bg='black',fg='white',width=30,bd=1).pack()
areports_button=Button(frame3,text='Bus Report',font=('Arial',16,'bold'),bg='black',fg='white',width=30,bd=1).pack()
logout_button=Button(frame3,text='Logout',font=('Arial',16,'bold'),bg='black',fg='white',width=30,bd=1).pack()

root.mainloop()