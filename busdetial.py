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
frame3=Frame(root,width=(w),height=200,bd=10,relief="raise")
frame3.pack(side=LEFT,fill=BOTH)
frame4=Frame(root,width=(w),height=200,bd=10,relief="raise")
frame4.pack(side=RIGHT,fill=BOTH)
busdetial_frame=Frame(frame4,width=w,height=300,bd=10,relief="raise")
busdetial_frame.pack(side=TOP,fill=BOTH)
database_frame=Frame(frame4,width=w,height=300,bd=10,relief="raise")
database_frame.pack(side=TOP,fill=BOTH)
#===================frame1-label================================
frame1_label=Label(frame1,text=" Bus Ticket Booking System\t\t\t",font=('Arial',40,'bold'),bg='green',fg='white').pack()

#===============frame2-buttons===============
frame2_button1=Button(frame2,text='Dasboard',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=0)
frame2_button2=Button(frame2,text='Search Bus',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=1)
frame2_button3=Button(frame2,text='My Booking',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=2)
frame2_button4=Button(frame2,text='Logout',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=3)
frame2_button5=Button(frame2,text='Contact',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=4)

#=============bus detial image==============
bus_detial_image=PhotoImage(file='greyhound_bus_18582222.png')
logo_set=Label(frame3,image=bus_detial_image).grid(row=0,column=0,sticky=W)

#============bus detial labels==============
to_lab=Label(frame3,text='Bus Detial\n',font=('arial',15,'bold')).grid(row=1,column=0,sticky=W)
bus_name_label=Label(frame3,text='Bus name:',font=('arial',10,'bold')).grid(row=2,column=0,sticky=W)
bus_number_label=Label(frame3,text='Bus number:',font=('arial',10,'bold')).grid(row=3,column=0,sticky=W)
from_city_label=Label(frame3,text='Bus city:',font=('arial',10,'bold')).grid(row=4,column=0,sticky=W)
bus_fare_label=Label(frame3,text='Bus fare:',font=('arial',10,'bold')).grid(row=5,column=0,sticky=W)

#=============passanger detil label==============
passanger_name_detial=Label(busdetial_frame,text='Name\t\t',font=('arial',14,'bold'),bg='green',fg='white').grid(row=0,column=0,sticky=W)
passanger_address_detial=Label(busdetial_frame,text='Address\t\t',font=('arial',14,'bold'),bg='green',fg='white').grid(row=0,column=1,sticky=W)
passanger_gender_detial=Label(busdetial_frame,text='Gender\t\t',font=('arial',14,'bold'),bg='green',fg='white').grid(row=0,column=2,sticky=W)
#====================passanger detil entry=============
passanger_name_detial_entry=Entry(busdetial_frame,bd=5).grid(row=1,column=0)
passanger_address_detial_entry=Entry(busdetial_frame,bd=5).grid(row=1,column=1)
passanger_gender_detial_entry=Entry(busdetial_frame,bd=5).grid(row=1,column=2)

#===================add button & total book==========
bnank=Label(busdetial_frame).grid(row=2)#bnak space
add_button=Button(busdetial_frame,text='Add',font=('arial',15,'bold'),fg='white',bg='green').grid(row=3,column=0,sticky=W)
bnank=Label(busdetial_frame).grid(row=4)
all_added=Label(busdetial_frame,text='All Added Passanger',font=('arial',13,'bold')).grid(row=5)
total_cost_label=Label(frame3,text='Total= 0$',font=('arial',12,'bold'),bd=5,padx=5,pady=4,fg='white',bg='green').grid(row=6,sticky=W)
l=Label(frame3).grid(row=7)
book_now_butt=Button(frame3,text='Book Now',font=('arial',15,'bold'),width=15,bd=5,padx=5,pady=6,fg='white',bg='green').grid(row=8)
#============================database===================
sn_label=Label(database_frame,text='S.no\t',font=('arial',10,'bold')).grid(row=0,column=0,sticky=W)
name_label=Label(database_frame,text='Name\t',font=('arial',10,'bold')).grid(row=0,column=1,sticky=W)
busname_label=Label(database_frame,text='Bus Name\t',font=('arial',10,'bold')).grid(row=0,column=2,sticky=W)
sn_label=Label(database_frame,text='Bus No\t',font=('arial',10,'bold')).grid(row=0,column=3,sticky=W)
sn_label=Label(database_frame,text='Age\t',font=('arial',10,'bold')).grid(row=0,column=4,sticky=W)
sn_label=Label(database_frame,text='Gender\t',font=('arial',10,'bold')).grid(row=0,column=5,sticky=W)
sn_label=Label(database_frame,text='Date\t',font=('arial',10,'bold')).grid(row=0,column=6,sticky=W)
sn_label=Label(database_frame,text='Fare\t',font=('arial',10,'bold')).grid(row=0,column=7,sticky=W)
sn_label=Label(database_frame,text='Action\t',font=('arial',10,'bold')).grid(row=0,column=8,sticky=W)













root.mainloop()
