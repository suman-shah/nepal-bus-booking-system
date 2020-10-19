from tkinter import*
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import*
root=Tk()
root.title('Bus Ticket System')
#root.geometry('800x600+250+80')
Tops=LabelFrame(root,width=1350,text='Yatra Tour and Travels',height=100,bd=14,relief="raise")
Tops.pack(side=TOP)

f1=Frame(root,width=900,height=650,bd=8,relief="raise")
f1.pack(side=LEFT)

f2=LabelFrame(root,width=440,height=650,bd=8,relief="raise")
f2.pack(side=RIGHT)

f1a=Frame(f1,width=900,height=330,bd=8,relief="raise")
f1a.pack(side=TOP)

f2a=LabelFrame(f1,width=900,height=320,bd=6,relief="raise")
f2a.pack(side=BOTTOM)

ft2=LabelFrame(f2,width=440,text='Ticket Conforation',height=650,bd=12,relief="raise")
ft2.pack(side=TOP)
fb2=Frame(f2,width=440,height=50,bd=16,relief="raise")
fb2.pack(side=BOTTOM)


f1aa=LabelFrame(f1a,width=400,text='Passanger Details',height=330,bd=16,relief="raise")
f1aa.pack(side=LEFT)
f1ab=LabelFrame(f1a,width=400,text='Choose Seat',height=330,bd=16,relief="raise")
f1ab.pack(side=RIGHT)

f2aa=Frame(f2a,width=450,height=330,bd=14,relief="raise")
f2aa.pack(side=LEFT)
f2aa=Frame(f2a,width=450,height=330,bd=14,relief="raise")
f2aa.pack(side=RIGHT)

def utton():
    conform=messagebox.askyesno("Seat Conformation","Do you want to conform for Mr."+name.get())
    if conform>0:
        ASit1.config(state=DISABLED)
    
    print(name.get())
    return
def unreserve(event):
    conform=messagebox.askyesno("Seat Unreservation","Do you want to Free This seat")
    if conform>0:
        ASit1.config(state=NORMAL)
    
    return
def cost_check():
    time_bus=Label(f1aa,text='7:15 \n Kalanki').grid(row=1,column=2,sticky=W)
    if destination.get()=='Birgunj':
        destination_fare_cost=Label(f1aa,text='700').grid(row=6,column=1)
    if destination.get()=='Kathmandu':
        destination_fare_cost=Label(f1aa,text='1000').grid(row=6,column=1)
    if destination.get()=='Pokhara':
        destination_fare_cost=Label(f1aa,text='800').grid(row=6,column=1)
    if destination.get()=='Butwal':
        destination_fare_cost=Label(f1aa,text='650').grid(row=6,column=1)
    if destination.get()=='Kalaiya':
        destination_fare_cost=Label(f1aa,text='300').grid(row=6,column=1)
     
f1.configure(background='sea green')
f2.configure(background='sea green')
#==================================top frame========
bus_logo=PhotoImage(file="Ap.png")
logo=Label(Tops,image=bus_logo)
logo.grid(row=0,column=0,sticky=W)
title_lel=Label(Tops,text='Nepal Yatayat Pvt.Ltd kathmandu').grid(row=1,column=0,sticky=W)
sys=Label(Tops,text='BUS TICKET BOOKING SYSTEM',font=('arial',48,'bold'),fg='dark khaki').grid(row=0,column=1)
cont_lael=Label(Tops,text='Contact: +977 987654321\nAddress: 44600, Kathmandu').grid(row=1,column=2,sticky=W)

#================passangerdetial------------
name=StringVar()
name_lael=Label(f1aa,font=('arial',15,'bold'),text='Name: ',fg='black').grid(row=0,column=0,sticky=W)
name_entry=Entry(f1aa,bd=5,textvariable=name).grid(row=0,column=1,sticky=W)
Age_lael=Label(f1aa,font=('arial',15,'bold'),text='Age  : ',fg='black').grid(row=1,column=0,sticky=W)
Age_entry=Entry(f1aa,bd=5).grid(row=1,column=1,sticky=W)
phone_lael=Label(f1aa,font=('arial',15,'bold'),text='Phone: ',fg='black').grid(row=2,column=0,sticky=W)
phone_entry=Entry(f1aa,bd=5).grid(row=2,column=1,sticky=W)
address_lael=Label(f1aa,font=('arial',15,'bold'),text='Address: ',fg='black').grid(row=3,column=0,sticky=W)
address_entry=Entry(f1aa,bd=5).grid(row=3,column=1,sticky=W)
gender_lael=Label(f1aa,font=('arial',15,'bold'),text='Gender: ',fg='black').grid(row=4,column=0,sticky=W)
g=IntVar()
g.set(1)
gender_entry=Radiobutton(f1aa,text='Male',bd=5,value=1,variable=g).grid(row=4,column=1,sticky=W)
genders_entry=Radiobutton(f1aa,text='Female',bd=5,value=2,variable=g).grid(row=4,column=2,sticky=W)
des_lael=Label(f1aa,font=('arial',15,'bold'),text='Destination: ',fg='black').grid(row=5,column=0,sticky=W)
destination=StringVar()
destination_cobobox=Combobox(f1aa,width=20,textvariable=destination,state='readonly',font=('arial',11,'bold'))
destination_cobobox['value']=('Birgunj','Kathmandu','Pokhara','Butwal','Kalaiya')
cost_ch=Button(f1aa,text='Cost',command=cost_check).grid(row=5,column=2,sticky=W)
destination_fare=Label(f1aa,text='BUS FARE:',font=('arial',15,'bold'),fg='green').grid(row=6,column=0,sticky=W)
bus_timeing=Label(f1aa,text='Departure Time ',font=('arial',15,'bold')).grid(row=0,column=2,sticky=W)

    
destination_cobobox.current(0)
destination_cobobox.grid(row=5,column=1,sticky=W)
#=============================Destination Section============
#ASECTION=Label(f1ab,text='A section',font=('arial',15,'bold')).grid(row=0,column=1)
A1=PhotoImage(file='A1.png')
A2=PhotoImage(file='A2.png')
A3=PhotoImage(file='A3.png')
A4=PhotoImage(file='A4.png')
A5=PhotoImage(file='A5.png')
A6=PhotoImage(file='A6.png')
A7=PhotoImage(file='A7.png')
A8=PhotoImage(file='A8.png')
A9=PhotoImage(file='A9.png')
A10=PhotoImage(file='A10.png')
A11=PhotoImage(file='A11.png')
A12=PhotoImage(file='A12.png')

B1=PhotoImage(file='B1.png')
B2=PhotoImage(file='B2.png')
B3=PhotoImage(file='B3.png')
B4=PhotoImage(file='B4.png')
B5=PhotoImage(file='B5.png')
B6=PhotoImage(file='B6.png')
B7=PhotoImage(file='B7.png')
B8=PhotoImage(file='B8.png')
B9=PhotoImage(file='B9.png')
B10=PhotoImage(file='B10.png')
B11=PhotoImage(file='B11.png')
B12=PhotoImage(file='B12.png')
#FOR A SECTION


ASit1=Button(f1ab,image=A1,command=utton)
ASit1.bind("<Button-3>",unreserve)
ASit1.grid(row=1,column=0)

ASit2=Button(f1ab,image=A2)
ASit2.bind("<Button-3>",unreserve)
ASit2.grid(row=1,column=1)

ASit3=Button(f1ab,image=A3)
ASit3.bind("<Button-3>",unreserve)
ASit3.grid(row=2,column=0)

ASit4=Button(f1ab,image=A4)
ASit4.bind("<Button-3>",unreserve)
ASit4.grid(row=2,column=1)

ASit5=Button(f1ab,image=A5)
ASit5.bind("<Button-3>",unreserve)
ASit5.grid(row=3,column=0)

ASit6=Button(f1ab,image=A6)
ASit6.bind("<Button-3>",unreserve)
ASit6.grid(row=3,column=1)

ASit7=Button(f1ab,image=A7)
ASit7.bind("<Button-3>",unreserve)
ASit7.grid(row=4,column=0)

ASit8=Button(f1ab,image=A8)
ASit8.bind("<Button-3>",unreserve)
ASit8.grid(row=4,column=1)

ASit9=Button(f1ab,image=A9)
ASit9.bind("<Button-3>",unreserve)
ASit9.grid(row=5,column=0)

ASit10=Button(f1ab,image=A10)
ASit10.bind("<Button-3>",unreserve)
ASit10.grid(row=5,column=1)

ASit11=Button(f1ab,image=A11)
ASit11.bind("<Button-3>",unreserve)
ASit11.grid(row=6,column=0)

ASit12=Button(f1ab,image=A12)
ASit12.bind("<Button-3>",unreserve)
ASit12.grid(row=6,column=1)

#FOR B SECTION
BSit1=Button(f1ab,image=B1).grid(row=1,column=3)
BSit2=Button(f1ab,image=B2).grid(row=1,column=4)
BSit3=Button(f1ab,image=B3).grid(row=2,column=3)
BSit4=Button(f1ab,image=B4).grid(row=2,column=4)
BSit5=Button(f1ab,image=B5).grid(row=3,column=3)
BSit6=Button(f1ab,image=B6).grid(row=3,column=4)
BSit7=Button(f1ab,image=B7).grid(row=4,column=3)
BSit8=Button(f1ab,image=B8).grid(row=4,column=4)
BSit9=Button(f1ab,image=B9).grid(row=5,column=3)
BSit10=Button(f1ab,image=B10).grid(row=5,column=4)
BSit11=Button(f1ab,image=B11).grid(row=6,column=3)
BSit12=Button(f1ab,image=B12).grid(row=6,column=4)

SECTION=Label(f1ab,text='LEFT--- RIGHT',font=('arial',15,'bold')).grid(row=0,column=2)







root.mainloop()
