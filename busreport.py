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
frame3=Frame(root,width=(w),height=500,bd=10,relief="raise")
frame3.pack(side=TOP,fill=BOTH)
#===================frame1-label================================
frame1_label=Label(frame1,text=" Bus Ticket Booking System\t\t\t",font=('Arial',40,'bold'),bg='green',fg='white').pack()
#===============frame2-buttons===============
frame2_button1=Button(frame2,text='Home',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=0)
frame2_button2=Button(frame2,text='About Project',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=1)
frame2_button3=Button(frame2,text='Login',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=2)
frame2_button4=Button(frame2,text='Register',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=3)
frame2_button5=Button(frame2,text='Contact',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=4)


root.mainloop()