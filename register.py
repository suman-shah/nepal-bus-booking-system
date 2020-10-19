from tkinter import*
from PIL import*
root=Tk()
root.title('Bus Ticket Booking System V 2.0.7.7.0.3')
w=root.winfo_screenwidth()
h=root.winfo_screenwidth()
root.geometry("%dx%d+0+0"%(w,h))
#==============variable================
g=IntVar()
g.set(1)
fname=StringVar()
fname.set("nobi")
lname=StringVar()
lname.set('rsi')
uname=StringVar()
uname.set('nobirsi')
password=StringVar()
password.set('123nepal')
email=StringVar()
email.set('nobi@hotmail.com')
dob=StringVar()
dob.set('2056-06-12')
fullad=StringVar()
fullad.set('Japan')

#=====================top 3 common frames=====================

frame1=Frame(root,width=(w),height=100,bd=10,relief="raise")
frame1.pack(side=TOP,fill=BOTH)
frame2=Frame(root,width=(w),height=50,bd=5,relief="raise")
frame2.pack(side=TOP,fill=BOTH)
frame3=Frame(root,width=(w),height=500,bd=10,relief="raise")
frame3.pack(side=TOP,fill=BOTH)
registration_frame=Frame(frame3,width=500,height=300)
registration_frame.pack(side=LEFT,fill=BOTH)
rpict_frame=Frame(frame3,width=500,height=300,bd=10)
rpict_frame.pack(side=RIGHT)
#===================frame1-label================================
frame1_label=Label(frame1,text=" Bus Ticket Booking System\t\t\t",font=('Arial',40,'bold'),bg='green',fg='white').pack()
#===============frame2-buttons===============
frame2_button1=Button(frame2,text='Home',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=0)
frame2_button2=Button(frame2,text='About Project',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=1)
frame2_button3=Button(frame2,text='Login',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=2)
frame2_button4=Button(frame2,text='Register',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=3)
frame2_button5=Button(frame2,text='Contact',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=4)
#=================================Registration labels=====================
ra=Label(registration_frame,text='Register your account',font=('Arial',20,'bold')).grid(row=0,column=0)
fname_register_label=Label(registration_frame,text='First name:\n',font=('arial',10,'bold')).grid(row=1,column=0,sticky=W)
lname_register_label=Label(registration_frame,text='Last name:\n',font=('arial',10,'bold')).grid(row=3,column=0,sticky=W)
uname_register_label=Label(registration_frame,text='User name:\n',font=('arial',10,'bold')).grid(row=5,column=0,sticky=W)
password_register_label=Label(registration_frame,text='Password:',font=('arial',10,'bold')).grid(row=7,column=0,sticky=W)
gender_label=Label(registration_frame,text='Gender',font=('arial',10,'bold')).grid(row=9,column=0,sticky=W)
gender_entry=Radiobutton(registration_frame,text='Male',bd=5,value=1,variable=g).grid(row=9,column=1,sticky=W)
genders_entry=Radiobutton(registration_frame,text='Female',bd=5,value=2,variable=g).grid(row=9,column=2,sticky=W)
email_register_label=Label(registration_frame,text='Email',font=('arial',10,'bold')).grid(row=13,column=0,sticky=W)
dob_register_label=Label(registration_frame,text='Date of Birth',font=('arial',10,'bold')).grid(row=15,column=0,sticky=W)
fulladdress_register_label=Label(registration_frame,text='Full Address',font=('arial',10,'bold')).grid(row=17,column=0,sticky=W)
#=============Entry box===================

first_name_entry=Entry(registration_frame,textvariable=fname,width=80,bd=6).grid(row=2,column=0)
last_name_entry=Entry(registration_frame,textvariable=lname,width=80,bd=6).grid(row=4,column=0)
user_name_entry=Entry(registration_frame,textvariable=uname,width=80,bd=6).grid(row=6,column=0)
password_name_entry=Entry(registration_frame,textvariable=password,width=80,bd=6).grid(row=8,column=0)
email_name_entry=Entry(registration_frame,textvariable=email,width=80,bd=6).grid(row=14,column=0)
dob_name_entry=Entry(registration_frame,textvariable=dob,width=80,bd=6).grid(row=16,column=0)
fulladdress_name_entry=Entry(registration_frame,textvariable=fullad,width=80,bd=6).grid(row=18,column=0)

#===========register button========
register_button=Button(registration_frame,text='Register',font=('arial',20,'bold'),fg='White',bg='Green',padx=8,pady=9).grid(row=20,column=0)

#==============image==========
reg_image=PhotoImage(file='businessregistration_signpen_negocio_inscripcio_2358.png')
reg_lab=Label(rpict_frame,image=reg_image).pack()
root.mainloop()