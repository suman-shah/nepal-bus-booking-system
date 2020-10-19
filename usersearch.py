from tkinter import*
from tkinter.ttk import Combobox
from tkcalendar import*
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
userdasboard_frame=Frame(frame3,width=500,height=300)
userdasboard_frame.pack(side=LEFT,fill=BOTH)
userdaspic_frame=Frame(frame3,width=500,height=300,bd=10)
userdaspic_frame.pack(side=RIGHT)
#===================frame1-label================================
frame1_label=Label(frame1,text=" Bus Ticket Booking System\t\t\t",font=('Arial',40,'bold'),bg='green',fg='white').pack()
#===============frame2-buttons===============
frame2_button1=Button(frame2,text='Dasboard',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=0)
frame2_button2=Button(frame2,text='Search Bus',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=1)
frame2_button3=Button(frame2,text='My Booking',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=2)
frame2_button4=Button(frame2,text='Logout',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=3)
frame2_button5=Button(frame2,text='Contact',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=4)

#=============search bus============
search_city_label=Label(userdasboard_frame,text='Search Bus',font=('Arial',20,'bold')).grid(row=0,column=0)
from_city_label=Label(userdasboard_frame,text='From city',font=('Arial',15,'bold')).grid(row=1,column=0,sticky=W)
to_city_label=Label(userdasboard_frame,text='To city',font=('Arial',15,'bold')).grid(row=2,column=0,sticky=W)
travel_city_datelabel=Label(userdasboard_frame,text='Travel Date',font=('Arial',15,'bold')).grid(row=3,column=0,sticky=W)
fbusdestination_cobobox=Combobox(userdasboard_frame,width=20,state='readonly',font=('arial',11,'bold'))
fbusdestination_cobobox['value']=('Birgunj','Kathmandu','Pokhara','Butwal','Kalaiya')
fbusdestination_cobobox.grid(row=1,column=1)
fbusdestination_cobobox.current(0)
tbusdestination_cobobox=Combobox(userdasboard_frame,width=20,state='readonly',font=('arial',11,'bold'))
tbusdestination_cobobox['value']=('Birgunj','Kathmandu','Pokhara','Butwal','Kalaiya')
tbusdestination_cobobox.grid(row=2,column=1)
tbusdestination_cobobox.current(1)

user_image=PhotoImage(file='avatar-3637561_640.png')
user_img_label=Label(userdaspic_frame,image=user_image).pack()

#==============calander============

def grab_date():
    my_label.config(text=cal.get_date())
my_button=Button(userdasboard_frame,text='Conform',padx=10,pady=5,font=("arial",10,"bold"),command=grab_date)
my_button.grid(row=4)
my_label=Label(userdasboard_frame,text="")
my_label.grid(row=5)
cal=Calendar(userdasboard_frame,selectmode='day',year=2020,month=6,command=grab_date)
cal.grid(row=3,column=1,sticky=W)


root.mainloop()
