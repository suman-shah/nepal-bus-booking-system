from tkinter import*
from tkinter.ttk import Combobox
from PIL import*
from tkcalendar import*
from tkinter import messagebox as ms
import sqlite3



root=Tk()
root.title('Bus Ticket Booking System V 2.0.7.7.0.3')
w=root.winfo_screenwidth()
h=root.winfo_screenwidth()
root.geometry("%dx%d+0+0"%(w,h))
#===========================database connect===================
# make database and users (if not exists already) table at programme start up
with sqlite3.connect('quit.db') as db:
    c = db.cursor()

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL PRIMARY KEY,password TEX NOT NULL);')
db.commit()
db.close()

conn_bus=sqlite3.connect('bus_route.db')
c=conn_bus.cursor()
c.execute('CREATE TABLE IF NOT EXISTS busroute(Route TEXT NOT NULL PRIMARY KEY, Bus_name TEXT, Bus_no TEXT, fare TEXT, Distance);')
    

conn=sqlite3.connect('bus_records.db')
c=conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS addresses(Bus_Name TEXT NOT NULL PRIMARY KEY, Bus_no TEXT, From_City TEXT, To_City TEXT, Departure_Time TEXT, Arrival_Time TEXT, Travel_Time TEXT, Distance TEXT);')
    
#==============variable================
g=IntVar()
g.set(1)
us=StringVar()
bus_route=StringVar()
fbusdestination_cobobox=StringVar()
fare=StringVar()
distance=StringVar()
travel_time=StringVar()
arrival_time=StringVar()
departure_time=StringVar()
to_city=StringVar()
from_city=StringVar()
bus_no=StringVar()
bus_name=StringVar()
name_passanger=StringVar()
address_passanger=StringVar()
gender_passanger=StringVar()
username = StringVar()
password = StringVar()
n_username = StringVar()
n_username.set('noitanobi')
n_password = StringVar()
passwordad_bot=StringVar()
user_bot=StringVar()
login=StringVar()
passwordadmin=StringVar()
passwordadmin.set('********')
fname=StringVar()
fname.set("nobita")
lname=StringVar()
lname.set('nobi')
uname=StringVar()
uname.set('nobirsi')
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
frame3=Frame(root,width=(w),height=900,relief="raise")
frame3.pack(side=TOP,fill=BOTH)
#==========destroy all 3 frames========================
def hide_frame1_welcome():
    for widget in frame1.winfo_children():
        widget.destroy()
def hide_frame2_welcome():
    for widget in frame2.winfo_children():
        widget.destroy()
def hide_frame3_welcome():
    for widget in frame3.winfo_children():
        widget.destroy()
def hide_frame4_welcome():
    for widget in frame4.winfo_children():
        widget.destroy()
#=======================================================
def useroradmin():
    usercheck=username.get()
    passcheck=password.get()
    if usercheck=='admin'and passcheck=='admin':
        admindasboard()
    else:
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(username.get()),(password.get())])
        result = c.fetchall()
        if result:
           usersdasboard()
        else:
            ms.showerror('Oops!','Username Not Found.')
def login_pannel():
    	#Establish Connection
        with sqlite3.connect('quit.db') as db:
            c = db.cursor()

        #Find user If there is any take proper action
        find_user = ('SELECT * FROM user WHERE username = ? and password = ?')
        c.execute(find_user,[(username.get()),(password.get())])
        result = c.fetchall()
        if result:
           useroradmin()
        else:
            ms.showerror('Oops!','Username Not Found.')
            
def new_user():
    #Establish Connection
    with sqlite3.connect('quit.db') as db:
        c = db.cursor()

    #Find Existing username if any take proper action
    find_user = ('SELECT username FROM user WHERE username = ?')
    c.execute(find_user,[(n_username.get())])        
    if c.fetchall():
        ms.showerror('Error!','Username Taken Try a Diffrent One.')
    else:
        ms.showinfo('Success!','Account Created!')
      
    #Create New Account 
    insert = 'INSERT INTO user(username,password) VALUES(?,?)'
    c.execute(insert,[(n_username.get()),(n_password.get())])
    db.commit()
        
        
def home_window_frame3():
    hide_frame2_welcome()
    hide_frame3_welcome()
    passwordadmin.set('********')
    login.set('admin')
    frame2_button1=Button(frame2,text='Home',command=home_window_frame3,font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=0)
    frame2_button2=Button(frame2,text='About Project',command=aboutus_window_frame3,font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=1)
    frame2_button3=Button(frame2,text='Login',command=login_window_frame3,font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=2)
    frame2_button4=Button(frame2,text='Register',command=register_window_frame3,font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=3)
    frame2_button5=Button(frame2,text='Contact',command=contact_window_frame3,font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=4)
    logo=Label(frame3,image=bus_logo)
    logo.grid(row=0,column=0)
#===============about us===
def aboutus_window_frame3():
    hide_frame3_welcome()
    l1=Label(frame3,text='About Project\n\n',font=('Arial',20,'bold')).pack(side=TOP)
    l2=Label(frame3,text='This project is made with the help of all friends of the batch 2075\n',font=('Arial',10,'bold')).pack(side=LEFT)
    bus_lab=Label(frame3,image=img_bus).pack(side=RIGHT)
def login_window_frame3():
    hide_frame3_welcome()
    login_frame=Frame(frame3,width=500,height=300)
    login_frame.pack(side=LEFT)
    pict_frame=Frame(frame3,width=500,height=300,bd=10)
    pict_frame.pack(side=RIGHT)
        #========Labels frame 3 childeren==========
    l2=Label(login_frame,text='Login to your account\n\n',font=('arial',20,'bold')).pack()
    user_name_label=Label(login_frame,text='username',font=('arial',15,'bold')).pack()
    user_name_entry=Entry(login_frame,textvariable=username,width=50,bd=5).pack()
    password_name_label=Label(login_frame,text='Password',font=('arial',15,'bold')).pack()
    password_name_entry=Entry(login_frame,textvariable=password,width=50,bd=5).pack()
 
    image_login=Label(pict_frame,image=img_login).pack()
    #==================login button=============
    login_button=Button(login_frame,text='Sign in',command=login_pannel,font=("arial",20,'bold'),fg='yellow',bg='black',padx=15,pady=5).pack()
def register_window_frame3():
    hide_frame3_welcome()
    registration_frame=Frame(frame3,width=500,height=300)
    registration_frame.pack(side=LEFT,fill=BOTH)
    rpict_frame=Frame(frame3,width=500,height=300,bd=10)
    rpict_frame.pack(side=RIGHT)
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
    #=============Entry box===================n_username

    first_name_entry=Entry(registration_frame,textvariable=fname,width=80,bd=6).grid(row=2,column=0)
    last_name_entry=Entry(registration_frame,textvariable=lname,width=80,bd=6).grid(row=4,column=0)
    user_name_entry=Entry(registration_frame,textvariable=n_username,width=80,bd=6).grid(row=6,column=0)
    password_name_entry=Entry(registration_frame,textvariable=n_password,width=80,bd=6).grid(row=8,column=0)
    email_name_entry=Entry(registration_frame,textvariable=email,width=80,bd=6).grid(row=14,column=0)
    dob_name_entry=Entry(registration_frame,textvariable=dob,width=80,bd=6).grid(row=16,column=0)
    fulladdress_name_entry=Entry(registration_frame,textvariable=fullad,width=80,bd=6).grid(row=18,column=0)

    #===========register button========
    register_button=Button(registration_frame,text='Register',command=new_user,font=('arial',20,'bold'),fg='White',bg='Green',padx=8,pady=9).grid(row=20,column=0)
    reg_lab=Label(rpict_frame,image=reg_image).pack()
def contact_window_frame3():
    hide_frame3_welcome()
    Label(frame3,text='Contact Detial',font=('arial',20,'bold')).pack()
    Label(frame3,text='Phone no: +977 9826282691\nAddress: Panitanki Birgunj\nWebsite: sumansah.com.np\nEmail: sumanshah0133@gmail.com',font=(10)).pack(side=LEFT)
    Label(frame3,image=contact_image).pack(side=RIGHT)
def adding_passangerdetial():
    frame5=Frame(frame3,width=(w),height=200,bd=10,relief="raise")
    frame5.pack(side=LEFT,fill=BOTH)
    frame4=Frame(frame3,width=(w),height=200,bd=10,relief="raise")
    frame4.pack(side=RIGHT,fill=BOTH)
    busdetial_frame=Frame(frame4,width=w,height=300,relief="raise")
    busdetial_frame.pack(side=TOP,fill=BOTH)

    
    database_frame_child=LabelFrame(database_frame,text='--------',width=w,height=300,relief="raise")
    database_frame_child.pack(side=TOP,fill=BOTH)   
    sn_label=Label(database_frame_child,text='S.no\t',font=('arial',10,'bold')).grid(row=0,column=0,sticky=W)
    name_label=Label(database_frame_child,text='Name\t',font=('arial',10,'bold')).grid(row=0,column=1,sticky=W)
    busname_label=Label(database_frame_child,text='Bus Name\t',font=('arial',10,'bold')).grid(row=0,column=2,sticky=W)
    sn_label=Label(database_frame_child,text='Bus No\t',font=('arial',10,'bold')).grid(row=0,column=3,sticky=W)
    sn_label=Label(database_frame_child,text='Age\t',font=('arial',10,'bold')).grid(row=0,column=4,sticky=W)
    sn_label=Label(database_frame_child,text='Gender\t',font=('arial',10,'bold')).grid(row=0,column=5,sticky=W)
    sn_label=Label(database_frame_child,text='Date\t',font=('arial',10,'bold')).grid(row=0,column=6,sticky=W)
    sn_label=Label(database_frame_child,text='Fare\t',font=('arial',10,'bold')).grid(row=0,column=7,sticky=W)
    sn_label=Label(database_frame_child,text='Action\t',font=('arial',10,'bold')).grid(row=0,column=8,sticky=W)

def usersdasboard_search_allavaiablebus_booknow():
    hide_frame3_welcome()
    frame5=Frame(frame3,width=(w),height=200,bd=10,relief="raise")
    frame5.pack(side=LEFT,fill=BOTH)
    frame4=Frame(frame3,width=(w),height=200,bd=10,relief="raise")
    frame4.pack(side=RIGHT,fill=BOTH)
    busdetial_frame=Frame(frame4,width=w,height=300,relief="raise")
    busdetial_frame.pack(side=TOP,fill=BOTH)
    database_frame=LabelFrame(frame4,text='S.no\tName\t\tBus Name\t\tBus No\t\tAge\t\tGender\t\tDate\t\tFare\t\t',font=(10),width=w,height=300,relief="raise")
    database_frame.pack(side=TOP,fill=BOTH)
    database_frame_child=LabelFrame(database_frame,text='--------',width=w,height=300,relief="raise")
    database_frame_child.pack(side=TOP,fill=BOTH)
   
    
    #=============bus detial image==============
    
    logo_set=Label(frame5,image=bus_detial_image).grid(row=0,column=0,sticky=W)

    #============bus detial labels==============
    to_lab=Label(frame5,text='Bus Detial\n',font=('arial',15,'bold')).grid(row=1,column=0,sticky=W)
    bus_name_label=Label(frame5,text='Bus name:',font=('arial',10,'bold')).grid(row=2,column=0,sticky=W)
    bus_number_label=Label(frame5,text='Bus number:',font=('arial',10,'bold')).grid(row=3,column=0,sticky=W)
    from_city_label=Label(frame5,text='Bus city:',font=('arial',10,'bold')).grid(row=4,column=0,sticky=W)
    bus_fare_label=Label(frame5,text='Bus fare:',font=('arial',10,'bold')).grid(row=5,column=0,sticky=W)

    #=============passanger detil label==============
    passanger_name_detial=Label(busdetial_frame,text='Name\t\t',font=('arial',14,'bold'),bg='green',fg='white').grid(row=0,column=0,sticky=W)
    passanger_address_detial=Label(busdetial_frame,text='Address\t\t',font=('arial',14,'bold'),bg='green',fg='white').grid(row=0,column=1,sticky=W)
    passanger_gender_detial=Label(busdetial_frame,text='Gender\t\t',font=('arial',14,'bold'),bg='green',fg='white').grid(row=0,column=2,sticky=W)
    #====================passanger detil entry=============
    passanger_name_detial_entry=Entry(busdetial_frame,textvariable=name_passanger,bd=5).grid(row=1,column=0)
    passanger_address_detial_entry=Entry(busdetial_frame,textvariable=address_passanger,bd=5).grid(row=1,column=1)
    passanger_gender_detial_entry=Entry(busdetial_frame,textvariable=gender_passanger,bd=5).grid(row=1,column=2)

    #===================add button & total book==========
    bnank=Label(busdetial_frame).grid(row=2)#bnak space
    add_button=Button(busdetial_frame,text='Add',command=adding_passangerdetial,font=('arial',15,'bold'),fg='white',bg='green').grid(row=3,column=0,sticky=W)
    bnank=Label(busdetial_frame).grid(row=4)
    all_added=Label(busdetial_frame,text='All Added Passanger',font=('arial',13,'bold')).grid(row=5)
    total_cost_label=Label(frame5,text='Total= 0$',font=('arial',12,'bold'),bd=5,padx=5,pady=4,fg='white',bg='green').grid(row=6,sticky=W)
    l=Label(frame5).grid(row=7)
    book_now_butt=Button(frame5,text='Book Now',font=('arial',15,'bold'),width=15,bd=5,padx=5,pady=6,fg='white',bg='green').grid(row=8)
    #============================database===================
    
    
def usersdasboard_search_allavaiablebus():
    hide_frame3_welcome()
    
    avaiable_frame=Frame(frame3,width=500,height=300)
    avaiable_frame.pack(side=LEFT,fill=BOTH)
    apict_frame=Frame(frame3,width=500,height=300,bd=10)
    apict_frame.pack(side=RIGHT)
    
    #================label=======================
    to_lab=Label(avaiable_frame,text='All Avaibale Bus\n',font=('arial',20,'bold')).grid(row=0,column=1)
    bus_name_label=Label(avaiable_frame,text='Bus name:',font=('arial',15,'bold')).grid(row=1,column=0,sticky=W)
    bus_number_label=Label(avaiable_frame,text='Bus number:',font=('arial',15,'bold')).grid(row=2,column=0,sticky=W)
    from_city_label=Label(avaiable_frame,text='Bus city:',font=('arial',15,'bold')).grid(row=3,column=0,sticky=W)
    bus_fare_label=Label(avaiable_frame,text='Bus fare:',font=('arial',15,'bold')).grid(row=4,column=0,sticky=W)

    #=========book now button================
    book_button=Button(avaiable_frame,text='Book Now',command=usersdasboard_search_allavaiablebus_booknow,bg='green',fg='white',font=('arial',20,'bold')).grid(row=5,column=1)

    #======choosen number====================
    
    book_image_label=Label(apict_frame,image=book_image).pack()
def usersdasboard_search():
    hide_frame3_welcome()
    userdasboard_frame=Frame(frame3,width=500,height=300)
    userdasboard_frame.pack(side=LEFT,fill=BOTH)
    userdaspic_frame=Frame(frame3,width=500,height=300,bd=10)
    userdaspic_frame.pack(side=RIGHT)
    
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
    search_us_button=Button(userdasboard_frame,text='Search Bus Now',command=usersdasboard_search_allavaiablebus,font=('Arial',20,'bold'),fg='white',bg='green',padx=10,pady=5).grid(row=7,column=0,sticky=W)
   
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
def usersdasboard():    
    hide_frame2_welcome()
    hide_frame3_welcome()
    frame4=Frame(root,width=(w),height=500,relief="raise")
    frame4.pack(side=RIGHT,fill=BOTH)
    #==============user welcome note================
    Label(frame3,text='User Screen',font=('Arial',30,'bold'),fg='green').pack()
    #===============frame2-buttons===============
    frame2_button1=Button(frame2,text='Dasboard',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=0)
    frame2_button2=Button(frame2,text='Search Bus',command=usersdasboard_search,font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=1)
    frame2_button3=Button(frame2,text='My Booking',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=2)
    frame2_button4=Button(frame2,text='Logout',command=home_window_frame3,font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=3)
    frame2_button5=Button(frame2,text='Contact',font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=4)
    
    user_bus_iamge_label=Label(frame3,image=user_bus_iamge).pack(side=RIGHT)
    #===========das board==============
    das_button=Button(frame3,text='Dashboard',font=('Arial',16,'bold'),bg='black',fg='white',width=30,bd=1).pack()
    addbus_button=Button(frame3,text='Search Bus',command=usersdasboard_search,font=('Arial',16,'bold'),bg='black',fg='white',width=30,bd=1).pack()
    addroute_button=Button(frame3,text='My Booking',font=('Arial',16,'bold'),bg='black',fg='white',width=30,bd=1).pack()
    viewr_button=Button(frame3,text='Logout',command=home_window_frame3,font=('Arial',16,'bold'),bg='black',fg='white',width=30,bd=1).pack()
    areports_button=Button(frame3,text='Contact',font=('Arial',16,'bold'),bg='black',fg='white',width=30,bd=1).pack()
def adding_recordto_databse():
    conn=sqlite3.connect('bus_records.db')
    c=conn.cursor()
    
    c.execute("INSERT INTO addresses VALUES (:Bus_Name,:Bus_no,:From_City,:To_City,:Departure_Time,:Arrival_Time,:Travel_Time,:Distance)",
              {
                 'Bus_Name':bus_name.get(),
                 'Bus_no':bus_no.get(),
                 'From_City':from_city.get(),
                 'To_City':to_city.get(),
                 'Departure_Time':departure_time.get(),
                 'Arrival_Time':arrival_time.get(),
                 'Travel_Time':travel_time.get(),
                 'Distance':distance.get()
              })
    conn.commit()
    conn.close()
    #============clearing all text fields============
    bus_name.set('')
    bus_no.set('')
    from_city.set('')
    to_city.set('')
    departure_time.set('')
    arrival_time.set('')
    travel_time.set('')
    distance.set('')
def admin_bus_report():
    hide_frame3_welcome()
        #================frame 3-add bus labels and entry wizrad=======================
    Label(frame3,text='BUS REPORT',font=('Arial',20,'bold')).grid(row=0,column=10)
    conn=sqlite3.connect('bus_records.db')
    c=conn.cursor()
    c.execute('SELECT*,oid FROM addresses')
    
    ll=c.fetchall()
    global print_name,print_no
    print_name=''
    print_no=''
    print_from=''
    print_to=''
    print_depart=''
    print_arrival=''
    print_travel=''
    print_distanc=''
    
    for busname in ll:
        print_name+=str(busname[0])+'\n'
        print_no+=str(busname[1])+'\n'
        print_from+=str(busname[2])+'\n'
        print_to+=str(busname[3])+'\n'
        print_depart+=str(busname[4])+'\n'
        print_arrival+=str(busname[5])+'\n'
        print_travel+=str(busname[6])+'\n'
        print_distanc+=str(busname[7])+'\n'
        us=print_name
        
    Label(frame3,text='Bus Name\t',font=('Arial',15,'bold')).grid(row=1,column=0,sticky=W)
    Label(frame3,text='Bus No\t',font=('Arial',15,'bold')).grid(row=1,column=1,sticky=W)
    Label(frame3,text='From City\t',font=('Arial',15,'bold')).grid(row=1,column=2,sticky=W)
    Label(frame3,text='To City\t',font=('Arial',15,'bold')).grid(row=1,column=3,sticky=W)
    Label(frame3,text='Deparature\t',font=('Arial',15,'bold')).grid(row=1,column=4,sticky=W)
    Label(frame3,text='Arrival\t',font=('Arial',15,'bold')).grid(row=1,column=5,sticky=W)
    Label(frame3,text='Travel\t',font=('Arial',15,'bold')).grid(row=1,column=6,sticky=W)
    Label(frame3,text='Distance\t',font=('Arial',15,'bold')).grid(row=1,column=7,sticky=W)
    

    
    Label(frame3,text=print_name,font=('Arial',10,'bold')).grid(row=2,column=0,sticky=W)
    Label(frame3,text=print_no,font=('Arial',10,'bold')).grid(row=2,column=1,sticky=W)
    Label(frame3,text=print_from,font=('Arial',10,'bold')).grid(row=2,column=2,sticky=W)
    Label(frame3,text=print_to,font=('Arial',10,'bold')).grid(row=2,column=3,sticky=W)
    Label(frame3,text=print_depart,font=('Arial',10,'bold')).grid(row=2,column=4,sticky=W)
    Label(frame3,text=print_arrival,font=('Arial',10,'bold')).grid(row=2,column=5,sticky=W)
    Label(frame3,text=print_travel,font=('Arial',10,'bold')).grid(row=2,column=6,sticky=W)
    Label(frame3,text=print_distanc,font=('Arial',10,'bold')).grid(row=2,column=7,sticky=W)
    
    conn.commit()
    conn.close()
def all_added_route_databases():
    conn=sqlite3.connect('bus_route.db')
    c=conn.cursor()
    
    c.execute("INSERT INTO busroute VALUES (:Route,:Bus_name,:Bus_no,:fare,:Distance)",
              {
                 'Route':bus_route.get(),
                 'Bus_name':fbusdestination_cobobox.get(),
                 'Bus_no':nofbusdestination_cobobox.get(),
                 'fare':fare.get(),
                 'Distance':distance.get()
              })
    conn.commit()
    conn.close()
    #============clearing all text fields============
    bus_no.set('')
    fare.set('')
    distance.set('')
def admindashboard_viewroute():
    hide_frame3_welcome()
        #================frame 3-add bus labels and entry wizrad=======================
    Label(frame3,text='ALL ADDED ROUTE',font=('Arial',20,'bold')).grid(row=0,column=10)
    conn=sqlite3.connect('bus_route.db')
    c=conn.cursor()
    c.execute('SELECT*,oid FROM busroute')
    
    ll=c.fetchall()
    
    print_routes =''
    print_busname=''
    print_no=''
    print_fare=''
    print_distanc=''
    
    for busname in ll:
        print_routes+=str(busname[0])+'\n'
        print_busname+=str(busname[1])+'\n'
        print_no+=str(busname[2])+'\n'
        print_fare+=str(busname[3])+'\n'
        print_distanc+=str(busname[4])+'\n'
        
        
    Label(frame3,text='Bus Route\t',font=('Arial',15,'bold')).grid(row=1,column=0,sticky=W)
    Label(frame3,text='Bus Name\t',font=('Arial',15,'bold')).grid(row=1,column=1,sticky=W)
    Label(frame3,text='Bus Number\t',font=('Arial',15,'bold')).grid(row=1,column=2,sticky=W)
    Label(frame3,text='Fare\t',font=('Arial',15,'bold')).grid(row=1,column=3,sticky=W)
    Label(frame3,text='Distance\t',font=('Arial',15,'bold')).grid(row=1,column=7,sticky=W)
    

    
    Label(frame3,text=print_routes,font=('Arial',10,'bold')).grid(row=2,column=0,sticky=W)
    Label(frame3,text=print_busname,font=('Arial',10,'bold')).grid(row=2,column=1,sticky=W)
    Label(frame3,text=print_no,font=('Arial',10,'bold')).grid(row=2,column=2,sticky=W)
    Label(frame3,text=print_fare,font=('Arial',10,'bold')).grid(row=2,column=3,sticky=W)
    Label(frame3,text=print_distanc,font=('Arial',10,'bold')).grid(row=2,column=7,sticky=W)
    
    conn.commit()
    conn.close()
    
def admindasboard_busroute():
    hide_frame3_welcome()
    global fbusdestination_cobobox,nofbusdestination_cobobox
    #================frame 3-add bus labels and entry wizrad=======================
    Label(frame3,text='ADD NEW ROUTE',font=('Arial',20,'bold')).grid(row=0)
    Label(frame3,text='Select Bus',font=('Arial',15,'bold')).grid(row=1,column=0,sticky=W)
    fbusdestination_cobobox=Combobox(frame3,width=36,state='readonly',font=('arial',11,'bold'))
    fbusdestination_cobobox['value']=print_name
    fbusdestination_cobobox.grid(row=1,column=1)
    fbusdestination_cobobox.current(0) 

    Label(frame3,text='Route:',font=('Arial',15,'bold')).grid(row=2,column=0,sticky=W)
    Entry(frame3,width=50,textvariable=bus_route,bd=5).grid(row=2,column=1)

    Label(frame3,text='Distance:',font=('Arial',15,'bold')).grid(row=3,column=0,sticky=W)
    Entry(frame3,width=50,textvariable=distance,bd=5).grid(row=3,column=1)

    Label(frame3,text='Fare:',font=('Arial',15,'bold')).grid(row=4,column=0,sticky=W)
    Entry(frame3,width=50,textvariable=fare,bd=5).grid(row=4,column=1)

    Label(frame3,text='Select Bus no',font=('Arial',15,'bold')).grid(row=5,column=0,sticky=W)
    nofbusdestination_cobobox=Combobox(frame3,width=36,state='readonly',font=('arial',11,'bold'))
    nofbusdestination_cobobox['value']=print_no
    nofbusdestination_cobobox.grid(row=5,column=1)
    


    #==================Add bus button============
    Button(frame3,text='Add Route',command=all_added_route_databases,font=('Arial',25,'bold'),bg='black',fg='white').grid(row=9,column=1)
    
def admindasboard_addbus():
    hide_frame3_welcome()
        #================frame 3-add bus labels and entry wizrad=======================
    Label(frame3,text='ADD BUS',font=('Arial',20,'bold')).grid(row=0)
    Label(frame3,text='Bus Name',font=('Arial',15,'bold')).grid(row=1,column=0,sticky=W)
    Entry(frame3,textvariable=bus_name,width=50,bd=5).grid(row=1,column=1)

    Label(frame3,text='Bus no',font=('Arial',15,'bold')).grid(row=2,column=0,sticky=W)
    Entry(frame3,textvariable=bus_no,width=50,bd=5).grid(row=2,column=1)

    Label(frame3,text='From City',font=('Arial',15,'bold')).grid(row=3,column=0,sticky=W)
    Entry(frame3,textvariable=from_city,width=50,bd=5).grid(row=3,column=1)

    Label(frame3,text='To City',font=('Arial',15,'bold')).grid(row=4,column=0,sticky=W)
    Entry(frame3,textvariable=to_city,width=50,bd=5).grid(row=4,column=1)

    Label(frame3,text='Departure Time',font=('Arial',15,'bold')).grid(row=5,column=0,sticky=W)
    Entry(frame3,textvariable=departure_time,width=50,bd=5).grid(row=5,column=1)

    Label(frame3,text='Arrival Time',font=('Arial',15,'bold')).grid(row=6,column=0,sticky=W)
    Entry(frame3,textvariable=arrival_time,width=50,bd=5).grid(row=6,column=1)

    Label(frame3,text='Travel Time',font=('Arial',15,'bold')).grid(row=7,column=0,sticky=W)
    Entry(frame3,textvariable=travel_time,width=50,bd=5).grid(row=7,column=1)

    Label(frame3,text='Distance',font=('Arial',15,'bold')).grid(row=8,column=0,sticky=W)
    Entry(frame3,textvariable=distance,width=50,bd=5).grid(row=8,column=1)
    #==================Add bus button============
    Button(frame3,text='Add Bus',command=adding_recordto_databse,font=('Arial',25,'bold'),bg='green',fg='white').grid(row=9,column=1,ipadx=60)
    
def admindasboard():
    hide_frame2_welcome()
    hide_frame3_welcome()
    frame4=Frame(frame3,width=(w),height=500,relief="raise")
    frame4.pack(side=RIGHT,fill=BOTH)
        
    #===============frame2-buttons===============
    frame2_button1=Button(frame2,text='Dashboard',command=admindasboard,font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=0)
    frame2_button2=Button(frame2,text='Add Bus',command=admindasboard_addbus,font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=1)
    frame2_button3=Button(frame2,text='Add Route',command=admindasboard_busroute,font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=2)
    frame2_button4=Button(frame2,text='View Route',command=admindashboard_viewroute,font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=3)
    frame2_button5=Button(frame2,text='Bus Report',command=admin_bus_report,font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=4)
    frame2_button6=Button(frame2,text='Logout',command=home_window_frame3,font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=5)

   
    admin_bus_iamge_label=Label(frame4,image=admin_bus_iamge).pack(side=RIGHT)
    #===========das board==============
    das_button=Button(frame3,text='Dashboard',font=('Arial',16,'bold'),bg='black',fg='white',width=30,bd=1).pack()
    addbus_button=Button(frame3,text='Add Bus',command=admindasboard_addbus,font=('Arial',16,'bold'),bg='black',fg='white',width=30,bd=1).pack()
    addroute_button=Button(frame3,text='Add Route',command=admindasboard_busroute,font=('Arial',16,'bold'),bg='black',fg='white',width=30,bd=1).pack()
    viewr_button=Button(frame3,text='View Route',command=admindashboard_viewroute,font=('Arial',16,'bold'),bg='black',fg='white',width=30,bd=1).pack()
    areports_button=Button(frame3,text='Bus Report',command=admin_bus_report,font=('Arial',16,'bold'),bg='black',fg='white',width=30,bd=1).pack()
    logout_button=Button(frame3,text='Logout',command=home_window_frame3,font=('Arial',16,'bold'),bg='black',fg='white',width=30,bd=1).pack()
    
#===================frame1-label================================
frame1_label=Label(frame1,text=" Bus Ticket Booking System\t\t\t",font=('Arial',40,'bold'),bg='green',fg='white').pack()
#===============frame2-buttons===============
frame2_button1=Button(frame2,text='Home',command=home_window_frame3,font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=0)
frame2_button2=Button(frame2,text='About Project',command=aboutus_window_frame3,font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=1)
frame2_button3=Button(frame2,text='Login',command=login_window_frame3,font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=2)
frame2_button4=Button(frame2,text='Register',command=register_window_frame3,font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=3)
frame2_button5=Button(frame2,text='Contact',command=contact_window_frame3,font=('Arial',15,'bold'),bg='green',fg='white').grid(row=0,column=4)




#========================frame3-image======================
bus_logo=PhotoImage(file="bus-157723_1280.png")
bus_about=PhotoImage(file='bus-2028647_640.png')
img_bus=PhotoImage(file='panda-1454629_640.png')
img_login=PhotoImage(file='lock-4441691_640.png')
reg_image=PhotoImage(file='businessregistration_signpen_negocio_inscripcio_2358.png')
admin_bus_iamge=PhotoImage(file='volkswagen-158463_640.png')
contact_image=PhotoImage(file='users_theuser_6177.png')
user_bus_iamge=PhotoImage(file='bus-312565_640.png')
user_image=PhotoImage(file='avatar-3637561_640.png')
book_image=PhotoImage(file='greyhound_bus_18582.png')
bus_detial_image=PhotoImage(file='greyhound_bus_18582222.png')
logo=Label(frame3,image=bus_logo)
logo.pack()


conn.commit()
conn.close()
conn_bus.commit()
conn_bus.close()
root.mainloop()
