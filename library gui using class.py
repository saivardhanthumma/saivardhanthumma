#firstly import the modules what we required.....

from tkinter import *
from tkinter import ttk

from PIL import ImageTk,Image

import pymysql

from tkinter import messagebox

from tkcalendar import *

#create the class........

class Window:
    def __init__(self,win):
        self.win=win
        self.win.title('library management service')
        self.win.geometry('1525x800')#we can give any size it accept
        self.win.resizable(width=False,height=False)
        self.loginwindow()


    def show_password(self):
        if self.c1.cget()=='*':
            slef.c1.configure(show='')
            
            
            

    def loginwindow(self):
        Frame_login=Frame(self.win,bg='white')
        Frame_login.place(x=0,y=0,height=800,width=1525)
        
        self.img=ImageTk.PhotoImage(file="C:\\Users\\thumm\\Downloads\\alfons-morales-YLSwjSy7stw-unsplash.png")
        #img=Label(Frame_login,image=self.img).place(x=0,y=0,width=1525,height=800)

        #tkinter canvas
        can=Canvas(Frame_login,width=1525,height=800,bd=0,highlightthickness=0)
        can.pack(fill='both',expand=True)
        can.create_image(0,0,image=self.img)
        can.create_text(760,120,text='library management service',fill='white',font=('broadway',50))
        can.create_text(1250,600,text='DEVOLEPED BY:',fill='white',font=('arial black',18))
        can.create_text(1250,650,text='SAIVARDHAN THUMMA',fill='white',font=('cooper black',20))
                                
        f1=Frame(self.win,bg='green')
        f1.place(x=550,y=220,height=330,width=418)

        self.img1=ImageTk.PhotoImage(file="C:\\Users\\thumm\\Downloads\\Mc8kW4x9Q3aRR3RkP5Im_IMG_4417.png")
        #img1=Label(f1,image=self.img1).place(x=0,y=0,height=320,width=418)
        self.img2=ImageTk.PhotoImage(file="C:\\Users\\thumm\\Downloads\\user-3297 (1).png")
        
        can=Canvas(f1,width=418,height=320,bd=0,highlightthickness=0)
        can.pack(fill='both',expand=True)
        can.create_image(0,0,image=self.img1,anchor='nw')
        can.create_image(200,10,image=self.img2,anchor='n')
        can.create_text(110,150,text='username :',fill='white',font=('arial black',18))
        can.create_text(110,195,text='password :',fill='white',font=('arial black',18))
        can.create_text(200,100,text='login',fill='black',font=('cooper black',20,'bold'))
        
                
        self.t1=Entry(f1,width=15,font=('arial',15),bg='lightpink')
        self.t1.place(x=200,y=140)

        self.t2=Entry(f1,width=15,show='*',font=('arial',15),bg='lightpink')
        self.t2.place(x=200,y=180)
        
        #self.c1=Checkbutton(f1,text='show password',command=self.show_password)
       # self.c1.place(x=200,y=200)

        self.b1=Button(f1,text='login',command=self.login,bg='blue',fg='white',font=('arial',12),bd=0,width=10)
        self.b1.place(x=90,y=250)
        self.b2=Button(f1,text='register',command=self.register_page,bg='blue',fg='white',font=('arial',12),bd=0,width=10)
        self.b2.place(x=210,y=250)

    def login(self):
        if self.t1.get()=='' or self.t2.get()=='':
            messagebox.showerror('error',' All fields are required',parent=self.win)
        else:
             try:
                 db=pymysql.connect(host='localhost', user='root', password='', db='register_login')
                 cur=db.cursor()
                 username=self.t1.get()
                 password=self.t2.get()
        
                 sql="select * from registration where username='%s' and password='%s'" % (username,password)        
                 cur.execute(sql)
                 if cur.rowcount==0:
                     
                     messagebox.showerror('error',' invalid username and password',parent=self.win)
                        
                
                 else:
                     self.lib_page()
                     db.close()
                
             except:
                 messagebox.showerror('error','error due to connection')


    def register(self):
         if self.t1.get()==''or self.t2.get()=='' or self.t3.get()=='' or self.t4.get()=='':
             
             messagebox.showerror('error',' All fields are required',parent=self.win)
         else:
             try:
                 db=pymysql.connect(host='localhost', user='root', password='', db='register_login')
                 cur=db.cursor()
                 username=self.t1.get()
                 password=self.t2.get()
                 mobileno=self.t3.get()
                 email=self.t4.get()
                 cur.execute("select * from registration where username='%s' or mobile_no='%s'"%(username,mobileno))
                 if cur.rowcount!=0:
                     messagebox.showerror('error',' already username or mobileno is exist try with another')
                 else:
                     sql="insert into registration(username,password,mobile_no,email) values('%s','%s','%s','%s')" % (username,password,mobileno,email)
                     cur.execute(sql)
                     db.commit()
                     db.close()
                     messagebox.showinfo('regitration details','successfully registered')
             except:
                 
                 messagebox.showerror('erroe','error due to connection')            
                
                 
    
    
    def register_page(self):
        Frame_login1=Frame(self.win,bg='white')
        Frame_login1.place(x=0,y=0,height=800,width=1525)
        
        self.img=ImageTk.PhotoImage(file="C:\\Users\\thumm\\Downloads\\alfons-morales-YLSwjSy7stw-unsplash.png")
        #img=Label(Frame_login1,image=self.img).place(x=0,y=0,width=1525,height=800)

        
        self.img1=ImageTk.PhotoImage(file="C:\\Users\\thumm\\Downloads\\navy-blue-concrete-wall-with-scratches_53876-102666.png")
        can=Canvas(Frame_login1,width=1525,height=800,bd=0,highlightthickness=0)
        can.pack(fill='both',expand=True)
        can.create_image(0,0,image=self.img)
        can.create_text(760,120,text='library management service',fill='white',font=('broadway',50))

        
        f2=Frame(self.win,bg='white')
        f2.place(x=600,y=190,height=350,width=350)
        
        
        can=Canvas(f2,width=350,height=350,bd=0,highlightthickness=0)
        can.pack(fill='both',expand=True)
        can.create_image(40,150,image=self.img1) 
        can.create_text(100,82,text='username :',fill='white',font=('arial ',15))
        can.create_text(100,115,text='password :',fill='white',font=('arial ',15))
        can.create_text(100,150,text='mobile no :',fill='white',font=('arial ',15))
        can.create_text(100,185,text='email       :',fill='white',font=('arial',15))
        can.create_text(165,21,text='Registration form',fill='white',font=('arial black',18))


        self.t1=Entry(f2,width=20,bg='lightpink')
        self.t1.place(x=165,y=75)
        self.t2=Entry(f2,width=20,bg='lightpink')
        self.t2.place(x=165,y=110)
        self.t3=Entry(f2,width=20,bg='lightpink')
        self.t3.place(x=165,y=145)
        self.t4=Entry(f2,width=20,bg='lightpink')
        self.t4.place(x=165,y=180)


       

        b1=Button(f2,text='submit',command=self.register,bg='blue',fg='white',font=('calibri',12,'bold'),width=10)
        b1.place(x=130,y=225)

        b2=Button(f2,text='already registered!login',command=self.loginwindow,bg='brown',fg='white',font=('calibri',12,'bold'),width=20)
        b2.place(x=90,y=280)
        
     
        
class Library(Window):
    def add_student(self):
        f3=Frame(self.win,bg='white')
        f3.place(x=0,y=0,height=800,width=1525)
        
        
        self.img=ImageTk.PhotoImage(file="C:\\Users\\thumm\\Downloads\\alfons-morales-YLSwjSy7stw-unsplash.png")
        can=Canvas(f3,width=1525,height=800,bd=0,highlightthickness=0)
        can.pack(fill='both',expand=True)
        can.create_image(0,0,image=self.img)
        can.create_text(760,120,text='library management service',fill='white',font=('broadway',50))

        can.create_text(600,275,text='Hall ticket      :',fill='white',font=('arial black',20))
        can.create_text(600,325,text='Student name:',fill='white',font=('arial black',20))
        can.create_text(600,373,text='Branch           :',fill='white',font=('arial black',20))
        can.create_text(600,423,text='Semister        :',fill='white',font=('arial black',20))
        can.create_text(600,475,text='Year               :',fill='white',font=('arial black',20))


        
        
        self.T1=Entry(f3,width=20,font=('arial',16),bg='lightpink')
        self.T1.place(x=750,y=267)
        self.T2=Entry(f3,width=20,font=('arial',16),bg='lightpink')
        self.T2.place(x=750,y=317)
        self.T3=Entry(f3,width=20,font=('arial',16),bg='lightpink')
        self.T3.place(x=750,y=365)
        self.T4=Entry(f3,width=20,font=('arial',16),bg='lightpink')
        self.T4.place(x=750,y=415)
        self.T5=Entry(f3,width=20,font=('arial',16),bg='lightpink')
        self.T5.place(x=750,y=465)

        b1=Button(f3,text='submit',command=self.insert_stdetails,bg='light green',fg='white',font=('calibri',15,'bold'),width=25)
        b1.place(x=630,y=550)

        l1=Label(f3,text='ADD STUDENT DETAILS',bg='blue',fg='white',font=('calibri',25,'bold'),width=25)
        l1.place(x=530,y=180)
        
        b2=Button(f3,text='back',command=self.lib_page,bg='brown',fg='white',font=('calibri',15,'bold'),width=25)
        b2.place(x=0,y=0)


    def insert_stdetails(self):
         if self.T1.get()==''or self.T2.get()=='' or self.T3.get()=='' or self.T4.get()=='' or self.T5.get()=='':
             
             messagebox.showerror('error',' All fields are required',parent=self.win)
         else:
             try:
                 db=pymysql.connect(host='localhost', user='root', password='', db='librarydb')
                 cur=db.cursor()
                 htno=self.T1.get()
                 name=self.T2.get()
                 branch=self.T3.get()
                 sem=self.T4.get()
                 year=self.T5.get()
                 cur.execute("select * from student where htno='%s' or name='%s'"%(htno,name))
                 if cur.rowcount!=0:
                     messagebox.showerror('error',' already hallticket no.  or name is exist try with another')
                 else:
                     sql="insert into student(htno,name,branch,sem,year) values('%s','%s','%s','%s','%s')" % (htno,name,branch,sem,year)
                     cur.execute(sql)
                     db.commit()              
                     db.close()                   
                     messagebox.showinfo('student details','successfully recorded')
                    
             except:
                 messagebox.showerror('erroe','error due to connection')            
                
    def add_books(self):
        f3=Frame(self.win,bg='white')
        f3.place(x=0,y=0,height=800,width=1525)
        
        
        self.img=ImageTk.PhotoImage(file="C:\\Users\\thumm\\Downloads\\alfons-morales-YLSwjSy7stw-unsplash.png")
        can=Canvas(f3,width=1525,height=800,bd=0,highlightthickness=0)
        can.pack(fill='both',expand=True)
        can.create_image(0,0,image=self.img)
        can.create_text(760,120,text='library management service',fill='white',font=('broadway',50))

        can.create_text(600,275,text='Book_no      :',fill='white',font=('arial black',20))
        can.create_text(600,325,text='Title           :',fill='white',font=('arial black',20))
        can.create_text(600,373,text='Author         :',fill='white',font=('arial black',20))
        can.create_text(600,423,text='Subject        :',fill='white',font=('arial black',20))
        can.create_text(600,475,text='Price            :',fill='white',font=('arial black',20))
        can.create_text(600,525,text='Quantity        :',fill='white',font=('arial black',20))


        
        
        self. a1=Entry(f3,width=20,font=('arial',16),bg='lightpink')
        self.a1.place(x=750,y=267)
        self.b2=Entry(f3,width=20,font=('arial',16),bg='lightpink')
        self.b2.place(x=750,y=317)
        self.c3=Entry(f3,width=20,font=('arial',16),bg='lightpink')
        self.c3.place(x=750,y=365)
        self.d4=Entry(f3,width=20,font=('arial',16),bg='lightpink')
        self.d4.place(x=750,y=415)
        self.e5=Entry(f3,width=20,font=('arial',16),bg='lightpink')
        self.e5.place(x=750,y=465)
        self.f5=Entry(f3,width=20,font=('arial',16),bg='lightpink')
        self.f5.place(x=750,y=515)


        b1=Button(f3,text='submit',command=self.insert_bdetails,bg='light green',fg='white',font=('calibri',15,'bold'),width=25)
        b1.place(x=630,y=570)

        l1=Label(f3,text='ADD BOOK DETAILS',bg='green',fg='white',font=('calibri',25,'bold'),width=25)
        l1.place(x=530,y=180)
        
        b2=Button(f3,text='back',command=self.lib_page,bg='brown',fg='white',font=('calibri',15,'bold'),width=25)
        b2.place(x=0,y=0)

    def insert_bdetails(self):
        if self.a1.get()==''or self.b2.get()=='' or self.c3.get()=='' or self.d4.get()=='' or self.e5.get()=='' or self.f5.get()=='':
             
             messagebox.showerror('error',' All fields are required',parent=self.win)
        else:
             
            try:
                db=pymysql.connect(host='localhost', user='root', password='', db='librarydb')
                cur=db.cursor()
                book_no=self.a1.get()
                title=self.b2.get()
                author=self.c3.get()
                subject=self.d4.get()
                price=self.e5.get()
                qty=self.f5.get()
                cur.execute("select * from student where htno='%s' or name='%s'"%(book_no,title))
                if cur.rowcount!=0:
                    messagebox.showerror('error',' already hallticket no.  or name is exist try with another')
                else:
                    sql="insert into books(book_no,title,author,subject,price,qty) values('%s','%s','%s','%s','%s','%s')" % (book_no,title,author,subject,price,qty)
                    cur.execute(sql)
                    db.commit()
                    db.close()
                    messagebox.showinfo('book details','successfully recorded')  
            except:
                messagebox.showerror('erroe','error due to connection')            
    def issue_book(self):
        
        f3=Frame(self.win,bg='white')
        f3.place(x=0,y=0,height=800,width=1525)
        
        
        self.img=ImageTk.PhotoImage(file="C:\\Users\\thumm\\Downloads\\alfons-morales-YLSwjSy7stw-unsplash.png")
        can=Canvas(f3,width=1525,height=800,bd=0,highlightthickness=0)
        can.pack(fill='both',expand=True)
        can.create_image(0,0,image=self.img)
        can.create_text(760,120,text='library management service',fill='white',font=('broadway',50))

        can.create_text(600,275,text='Hall ticket      :',fill='white',font=('arial black',20))
        can.create_text(600,325,text='Book_no         :',fill='white',font=('arial black',20))
        
       

        
        
        self.A1=Entry(f3,width=20,font=('arial',16),bg='lightpink')
        self.A1.place(x=750,y=267)
        self.A2=Entry(f3,width=20,font=('arial',16),bg='lightpink')
        self.A2.place(x=750,y=317)
        
        
        


        b1=Button(f3,text='submit',command=self.insert_bissue_details,bg='light green',fg='white',font=('calibri',15,'bold'),width=25)
        b1.place(x=630,y=480)
        
        l1=Label(f3,text='BOOK ISSUE DETAILS',bg='orange',fg='white',font=('calibri',25,'bold'),width=25)
        l1.place(x=530,y=180)
        
        b2=Button(f3,text='back',command=self.lib_page,bg='brown',fg='white',font=('calibri',15,'bold'),width=25)
        b2.place(x=0,y=0)
          
    def insert_bissue_details(self):
        if self.A1.get()=='' or self.A2.get()=='' :
             
             messagebox.showerror('error',' All fields are required',parent=self.win)
        else:
             
            try:
                db=pymysql.connect(host='localhost', user='root', password='', db='librarydb')
                cur=db.cursor()
                htno=self.A1.get()
                book_no=self.A2.get()
                
             
                cur.execute("select * from student where htno='%s' "%(htno))
                if cur.rowcount!=0:
                    sql="insert into issue(htno,book_no,issue_date) values('%s','%s',curdate())" % (htno,book_no)
                    cur.execute(sql)
                    db.commit()
                    db.close()
                    messagebox.showinfo('details','successfully recorded')
                    
                else:
                    
                    messagebox.showerror('error','Details not found')
            except:
                messagebox.showerror('error','error due to connection')       
          
          
    
    def returndate(self):
        
        f3=Frame(self.win,bg='white')
        f3.place(x=0,y=0,height=800,width=1525)
        
        
        self.img=ImageTk.PhotoImage(file="C:\\Users\\thumm\\Downloads\\alfons-morales-YLSwjSy7stw-unsplash.png")
        can=Canvas(f3,width=1525,height=800,bd=0,highlightthickness=0)
        can.pack(fill='both',expand=True)
        can.create_image(0,0,image=self.img)
        can.create_text(760,120,text='library management service',fill='white',font=('broadway',50))

        can.create_text(600,275,text='book_no      :',fill='white',font=('arial black',20))
        can.create_text(600,373,text='Date           :',fill='white',font=('arial black',20))
        can.create_text(600,325,text='Remarks       :',fill='white',font=('arial black',20))
        
       

        
        
        self.B1=Entry(f3,width=20,font=('arial',16),bg='lightpink')
        self.B1.place(x=750,y=267)
        self.B2=Entry(f3,width=20,font=('arial',16),bg='lightpink')
        self.B2.place(x=750,y=317)
        self.B3=DateEntry(f3,selcetmode='year',font=('arial',16),date_pattern='yyyy/mm/dd')
        self.B3.place(x=750,y=365)
        
        


        b1=Button(f3,text='submit',command=self.insert_rdate,bg='light green',fg='white',font=('calibri',15,'bold'),width=25)
        b1.place(x=630,y=480)
        
        l1=Label(f3,text='RETURN DATE & REMARKS',bg='orange',fg='white',font=('calibri',25,'bold'),width=28)
        l1.place(x=530,y=180)
        
        b2=Button(f3,text='back',command=self.lib_page,bg='brown',fg='white',font=('calibri',15,'bold'),width=25)
        b2.place(x=0,y=0)
          
    def insert_rdate(self):
        if self.B1.get()==''or self.B2.get()=='' or self.B3.get()=='' :
             
             messagebox.showerror('error',' All fields are required',parent=self.win)
        else:
             
            try:
                db=pymysql.connect(host='localhost', user='root', password='', db='librarydb')
                cur=db.cursor()
                book_no=self.B1.get()
                print('l')
                remarks=self.B2.get()
                print(remarks)
                date=self.B3.get()
                print(date)
                
             
                cur.execute("select * from issue where book_no='%s' "%(book_no))
                print('l')
                if cur.rowcount!=0:
                    print('l')
                    sql="update issue set return_date='%s',remarks='%s' where book_no='%s'" % (date,remarks,book_no)
                    cur.execute(sql)
                    print('l')
                    db.commit()
                    db.close()
                    messagebox.showinfo('details','records updated')
                    
                else:
                    
                    messagebox.showerror('error','Details not found')
            except:
                messagebox.showerror('erroe','error due to connection')       
          
              

    def view_issued_books(self):
        f1=Frame(self.win,bg='white')
        f1.place(x=0,y=0,height=800,width=1525)

        self.img=ImageTk.PhotoImage(file="C:\\Users\\thumm\\Downloads\\alfons-morales-YLSwjSy7stw-unsplash.png")
        can=Canvas(f1,width=1525,height=800,bd=0,highlightthickness=0)
        can.pack(fill='both',expand=True)
        can.create_image(0,0,image=self.img)
        can.create_text(760,120,text='library management service',fill='white',font=('broadway',50))
        b2=Button(f1,text='back',command=self.lib_page,bg='brown',fg='white',font=('calibri',12,'bold'),width=20)
        b2.place(x=0,y=0)

        l1=Label(f1,text='ISSUED BOOKS',bg='gray',fg='black',font=('calibri',25,'bold'),width=25)
        l1.place(x=530,y=180)
        
        
         
      
        db=pymysql.connect(host='localhost', user='root', password='', db='librarydb')
        cur=db.cursor()
        sql="select htno, book_no, issue_date, return_date, remarks from issue order by issue_date desc"
        cur.execute(sql)
        rows=cur.fetchall()

        tree=ttk.Treeview(f1)
        s=ttk.Style(f1)
        s.theme_use("clam")
        s.configure(".",font=('arial',11))
        s.configure('Treeview.Heading',foreground='white',background='blue',font=('arial',11,'bold'))
        tree.place(x=450,y=280)
        tree['columns']=('htno',"book_no","issue_date","return_date","subject")
        tree['show']='headings'
        tree.column("htno",anchor='center',width=100)
        tree.column("book_no",anchor='center',width=100)
        tree.column("issue_date",anchor='w',width=130)
        tree.column("return_date",anchor='w',width=130)
        tree.column("subject",anchor='w',width=150)
 

        tree.heading('htno',text='htno',anchor='center')
        tree.heading('book_no',text='book_no',anchor='center')
        tree.heading('issue_date',text='issue_date',anchor='w')
        tree.heading('return_date',text='return_date',anchor='w')
        tree.heading('subject',text='subject',anchor='w')
        

        
        index=0
        iid=0
        for row in rows:
            tree.insert(parent='',index=index,iid=iid,text='parent',values=row)
            iid=index=iid+1
            
            
    def view_books(self):
        f1=Frame(self.win,bg='white')
        f1.place(x=0,y=0,height=800,width=1525)

        #self.img=ImageTk.PhotoImage(file="C:\\Users\\thumm\\Downloads\\alfons-morales-YLSwjSy7stw-unsplash.png")
        #img=Label(f1,image=self.img).place(x=0,y=0,width=1525,height=800)

        self.img=ImageTk.PhotoImage(file="C:\\Users\\thumm\\Downloads\\alfons-morales-YLSwjSy7stw-unsplash.png")
        can=Canvas(f1,width=1525,height=800,bd=0,highlightthickness=0)
        can.pack(fill='both',expand=True)
        can.create_image(0,0,image=self.img)
        can.create_text(760,120,text='library management service',fill='white',font=('broadway',50))
        b2=Button(f1,text='back',command=self.lib_page,bg='brown',fg='white',font=('calibri',12,'bold'),width=20)
        b2.place(x=0,y=0)

        l1=Label(f1,text='BOOKS DETAILS',bg='yellow',fg='black',font=('calibri',25,'bold'),width=25)
        l1.place(x=530,y=180)
        
        
        db=pymysql.connect(host='localhost', user='root', password='', db='librarydb')
        cur=db.cursor()
        sql="select * from books order by price asc "
        cur.execute(sql)
        rows=cur.fetchall()

        tree=ttk.Treeview(f1)
        s=ttk.Style(f1)
        s.theme_use("clam")
        s.configure(".",font=('arial',11))
        s.configure('Treeview.Heading',foreground='white',background='blue',font=('arial',11,'bold'))
        tree.place(x=470,y=280)
        tree['columns']=('id',"book_no","title","author","subject","price","qty")
        tree['show']='headings'
        tree.column("id",anchor='center',width=50)
        tree.column("book_no",anchor='center',width=50)
        tree.column("title",anchor='w',width=120)
        tree.column("author",anchor='w',width=100)
        tree.column("subject",anchor='w',width=120)
        tree.column("price",anchor='center',width=50)
        tree.column("qty",anchor='center',width=50)

        tree.heading('id',text='id',anchor='center')
        tree.heading('book_no',text='book_no',anchor='center')
        tree.heading('title',text='title',anchor='w')
        tree.heading('author',text='author',anchor='w')
        tree.heading('subject',text='subject',anchor='w')
        tree.heading('price',text='price',anchor='center')
        tree.heading('qty',text='qty',anchor='center')

        
        index=0
        iid=0
        for row in rows:
            
            tree.insert(parent='',index=index,iid=iid,text='parent',values=row)
            iid=index=iid+1
                        
            print('{:<20s} {:<20s} {:<15s} {:<15s} {:<30s} {:<15s} {:<30s}'.format(str(row[0]), str(row[1]), str(row[2]),str(row[3]),str(row[4]),str(row[5]),str(row[6])))
       
        
        

    def view_students(self):
        f1=Frame(self.win,bg='white')
        f1.place(x=0,y=0,height=800,width=1525)

        #self.img=ImageTk.PhotoImage(file="C:\\Users\\thumm\\Downloads\\alfons-morales-YLSwjSy7stw-unsplash.png")
        #img=Label(f1,image=self.img).place(x=0,y=0,width=1525,height=800)

        self.img=ImageTk.PhotoImage(file="C:\\Users\\thumm\\Downloads\\alfons-morales-YLSwjSy7stw-unsplash.png")
        can=Canvas(f1,width=1525,height=800,bd=0,highlightthickness=0)
        can.pack(fill='both',expand=True)
        can.create_image(0,0,image=self.img)
        can.create_text(760,120,text='library management service',fill='white',font=('broadway',50))
        b2=Button(f1,text='back',command=self.lib_page,bg='brown',fg='white',font=('calibri',12,'bold'),width=20)
        b2.place(x=0,y=0)

        l1=Label(f1,text='STUDENT DETAILS',bg='light yellow',fg='black',font=('calibri',25,'bold'),width=25)
        l1.place(x=530,y=180)
        
        flag=False
        db=pymysql.connect(host='localhost', user='root', password='', db='librarydb')
        cur=db.cursor()
        sql="select htno,name,branch,sem,year from student order by sem asc "
        cur.execute(sql)
        rows=cur.fetchall()

        tree=ttk.Treeview(f1)
        s=ttk.Style(f1)
        s.theme_use("clam")
        s.configure(".",font=('arial',11))
        s.configure('Treeview.Heading',foreground='white',background='blue',font=('arial',11,'bold'))
        tree.place(x=460,y=275)
        tree['columns']=('htno',"name","branch","sem","year")
        tree['show']='headings'
        tree.column("htno",anchor='center',width=100)
        tree.column("name",anchor='center',width=120)
        tree.column("branch",anchor='w',width=120)
        tree.column("sem",anchor='center',width=100)
        tree.column("year",anchor='center',width=120)
        

        tree.heading('htno',text='id',anchor='center')
        tree.heading('name',text='name',anchor='center')
        tree.heading('branch',text='branch',anchor='w')
        tree.heading('sem',text='sem',anchor='w')
        tree.heading('year',text='year',anchor='w')
        
        
        index=0
        iid=0
        for row in rows:
            
            tree.insert(parent='',index=index,iid=iid,text='parent',values=row)
            iid=index=iid+1
                        
            
       
        
        
        
        
    def lib_page(self):
        f3=Frame(self.win,bg='white')
        f3.place(x=0,y=0,height=800,width=1525)
        
        self.img=ImageTk.PhotoImage(file="C:\\Users\\thumm\\Downloads\\alfons-morales-YLSwjSy7stw-unsplash.png")
        can=Canvas(f3,width=1525,height=800,bd=0,highlightthickness=0)
        can.pack(fill='both',expand=True)
        can.create_image(0,0,image=self.img)
        can.create_text(760,120,text='library management service',fill='white',font=('broadway',50))
        
        

        
        b2=Button(f3,text='ADD STUDENTS',command=self.add_student,bg='blue',fg='white',font=('calibri',15,'bold'),width=25)
        b2.place(x=400,y=280)
        
        b2=Button(f3,text='ADD BOOKS',command=self.add_books,bg='green',fg='white',font=('calibri',15,'bold'),width=25)
        b2.place(x=800,y=280)
        
        b2=Button(f3,text='VIEW STUDENTS',command=self.view_students,bg='yellow',fg='white',font=('calibri',15,'bold'),width=25)
        b2.place(x=400,y=380)
        
        b2=Button(f3,text='VIEW BOOKS',command=self.view_books,bg='black',fg='white',font=('calibri',15,'bold'),width=25)
        b2.place(x=800,y=380)
        
        b2=Button(f3,text='ISSUE BOOKS',command=self.issue_book,bg='orange',fg='white',font=('calibri',15,'bold'),width=25)
        b2.place(x=400,y=480)
        
        b2=Button(f3,text='RETURN BOOKS',command=self.returndate,bg='gold',fg='white',font=('calibri',15,'bold'),width=25)
        b2.place(x=400,y=580)

        b2=Button(f3,text='SHOW ISSUED BOOKS',command=self.view_issued_books,bg='grey',fg='white',font=('calibri',15,'bold'),width=25)
        b2.place(x=800,y=480)
        
        b2=Button(f3,text='QUIT',command=self.loginwindow,bg='red',fg='white',font=('calibri',15,'bold'),width=25)
        b2.place(x=800,y=580)

        b2=Button(f3,text='back',command=self.loginwindow,bg='brown',fg='white',font=('calibri',15,'bold'),width=25)
        b2.place(x=0,y=0)

   
                 
win=Tk()
ob=Window(win)
ob1=Library(win)
win.mainloop()
        
