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
avaiable_frame=Frame(frame3,width=500,height=300)
avaiable_frame.pack(side=LEFT,fill=BOTH)
apict_frame=Frame(frame3,width=500,height=300,bd=10)
apict_frame.pack(side=RIGHT)
#===================frame1-label================================
frame1_label=Label(frame1,text=" Bus Ticket Booking System\t\t\t",font=('Arial',40,'bold'),bg='green',fg='white').pack()
#===============frame2-buttons===============
frame2_button1=Button(frame2,text='Dasboard',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=0)
frame2_button2=Button(frame2,text='Search Bus',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=1)
frame2_button3=Button(frame2,text='My Booking',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=2)
frame2_button4=Button(frame2,text='Logout',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=3)
frame2_button5=Button(frame2,text='Contact',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=4)
#================label=======================
to_lab=Label(avaiable_frame,text='All Avaibale Bus\n',font=('arial',20,'bold')).grid(row=0,column=1)
bus_name_label=Label(avaiable_frame,text='Bus name:',font=('arial',15,'bold')).grid(row=1,column=0,sticky=W)
bus_number_label=Label(avaiable_frame,text='Bus number:',font=('arial',15,'bold')).grid(row=2,column=0,sticky=W)
from_city_label=Label(avaiable_frame,text='Bus city:',font=('arial',15,'bold')).grid(row=3,column=0,sticky=W)
bus_fare_label=Label(avaiable_frame,text='Bus fare:',font=('arial',15,'bold')).grid(row=4,column=0,sticky=W)

#=========book now button================
book_button=Button(avaiable_frame,text='Book Now',bg='green',fg='white',font=('arial',20,'bold')).grid(row=5,column=1)

#======choosen number====================
book_image=PhotoImage(file='greyhound_bus_18582.png')
book_image_label=Label(apict_frame,image=book_image).pack()



root.mainloop()