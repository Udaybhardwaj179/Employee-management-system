from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title('Employee Management System')
        
        #variables
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_designation=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_married=StringVar()
        self.var_dod=StringVar()
        self.var_doj=StringVar()
        self.var_idproofcomb=StringVar()
        self.var_idproofnumber=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_country=StringVar()
        self.var_salary=StringVar()
        

        # title block
        
        lbl_title=Label(self.root,text='ONLINE EMPLOYEE MANAGEMENT SYSTEM',font=('times new roman',33,'bold'),fg="darkgreen",bg="white")
        lbl_title.place(x=0,y=0,width=1530,height=60)
        
        # main frame
        
        Main_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Main_frame.place(x=10,y=65,width=1398,height=580)
        
        #upper frame
        
        upper_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg="white",text="Employee Information",font=('times new roman',11,'bold'),fg="red")
        upper_frame.place(x=10,y=10,width=1380,height=270)
        
        #Labels
        
        lbl_dep=Label(upper_frame,text="Department",font=('arial',11,'bold'),bg="white")
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)
        #Department
        
        
        combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_dep,font=('arial',11,'bold'),width=17,state='readonly')
        combo_dep['value']=('Select Department','HR','Software Engineer','Manager','VP')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        #name
        
        lbl_name=Label(upper_frame,text="Name:",font=('arial',12,'bold'),bg="white")
        lbl_name.grid(row=0,column=2,padx=2,sticky=W,pady=7)
        
        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=("arial",11,"bold"))
        txt_name.grid(row=0,column=3,padx=2,pady=7)
        
        #lbl_designation
        
        lbl_Designation=Label(upper_frame,font=("arial",12,"bold"),text="Designation:",bg='white')
        lbl_Designation.grid(row=1,column=0,sticky=W,padx=2,pady=7)
        
        txt_Designation=ttk.Entry(upper_frame,textvariable=self.var_designation,width=22,font=("arial",11,"bold"))
        txt_Designation.grid(row=1,column=1,padx=2,pady=7,sticky=W)
        
        #email
        
        lbl_email=Label(upper_frame,font=("arial",12,"bold"),text="Email:",bg='white')
        lbl_email.grid(row=1,column=2,sticky=W,padx=2,pady=7)
        
        txt_email=ttk.Entry(upper_frame,textvariable=self.var_email,width=22,font=("arial",11,"bold"))
        txt_email.grid(row=1,column=3,padx=2,pady=7)
        
        #Address
        
        lbl_address=Label(upper_frame,font=("arial",12,"bold"),text="Address:",bg='white')
        lbl_address.grid(row=2,column=0,sticky=W,padx=2,pady=7)
        
        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=("arial",11,"bold"))
        txt_address.grid(row=2,column=1,padx=2,pady=7)
        
        #married
        
        lbl_married=Label(upper_frame,font=("arial",12,"bold"),text="Marital Status:",bg='white')
        lbl_married.grid(row=2,column=2,sticky=W,padx=2,pady=7)
        
        com_txt_married=ttk.Combobox(upper_frame,textvariable=self.var_married,state="readonly",font=("arial",12,"bold"),width=18)
        com_txt_married['value']=("Married","Unmarried")
        com_txt_married.current(0)
        com_txt_married.grid(row=2,column=3,sticky=W,padx=2,pady=7)
        
        #Dob
        
        lbl_dob=Label(upper_frame,font=("arial",12,"bold"),text="DOB:",bg='white')
        lbl_dob.grid(row=3,column=0,sticky=W,padx=2,pady=7)
        
        txt_dob=ttk.Entry(upper_frame,textvariable=self.var_dod,width=22,font=("arial",11,"bold"))
        txt_dob.grid(row=3,column=1,padx=2,pady=7)
        
        #DOJ
        
        lbl_doj=Label(upper_frame,font=("arial",12,"bold"),text="DOJ:",bg='white')
        lbl_doj.grid(row=3,column=2,sticky=W,padx=2,pady=7)
        
        txt_doj=ttk.Entry(upper_frame,textvariable=self.var_doj,width=22,font=("arial",11,"bold"))
        txt_doj.grid(row=3,column=3,padx=2,pady=7)
        
        #idproof
        
        com_txt_proof=ttk.Combobox(upper_frame,textvariable=self.var_idproofcomb,state="readonly",font=("arial",12,"bold"),width=18)
        com_txt_proof['value']=("Select ID Proof","Pan Card","Aadhaar Card","Driving License")
        com_txt_proof.current(0)
        com_txt_proof.grid(row=4,column=0,sticky=W,padx=2,pady=7)
        
        txt_proof=ttk.Entry(upper_frame,textvariable=self.var_idproofnumber,width=22,font=("arial",11,"bold"))
        txt_proof.grid(row=4,column=1,padx=2,pady=7)
        

        
        # gender
        
        lbl_gender=Label(upper_frame,font=("arial",12,"bold"),text="Gender:",bg='white')
        lbl_gender.grid(row=4,column=2,sticky=W,padx=2,pady=7)
        
        com_txt_gender=ttk.Combobox(upper_frame,textvariable=self.var_gender,state="readonly",font=("arial",12,"bold"),width=18)
        com_txt_gender['value']=("Male","Female","Others")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=4,column=3,sticky=W,padx=2,pady=7)
        
        #phone
        
        lbl_phone=Label(upper_frame,font=("arial",12,"bold"),text="Phone No:",bg='white')
        lbl_phone.grid(row=0,column=4,sticky=W,padx=2,pady=7)
        
        txt_phone=ttk.Entry(upper_frame,textvariable=self.var_phone,width=22,font=("arial",11,"bold"))
        txt_phone.grid(row=0,column=5,padx=2,pady=7)
        
        #country
        
        lbl_country=Label(upper_frame,font=("arial",12,"bold"),text="Country:",bg='white')
        lbl_country.grid(row=1,column=4,sticky=W,padx=2,pady=7)
        
        txt_country=ttk.Entry(upper_frame,textvariable=self.var_country,width=22,font=("arial",11,"bold"))
        txt_country.grid(row=1,column=5,padx=2,pady=7)
        
        #ctc
        
        lbl_ctc=Label(upper_frame,font=("arial",12,"bold"),text="Salary(CTC):",bg='white')
        lbl_ctc.grid(row=2,column=4,sticky=W,padx=2,pady=7)
        
        txt_ctc=ttk.Entry(upper_frame,textvariable=self.var_salary,width=22,font=("arial",11,"bold"))
        txt_ctc.grid(row=2,column=5,padx=2,pady=7)
        
        # button frame
        
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=1100,y=20,width=170,height=210)
        
        btn_add=Button(button_frame,text="Save",command=self.add_data,font=("arial",15,"bold"),width=13,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=1,pady=5)
        
        btn_update=Button(button_frame,text="Update",command=self.update_data,font=("arial",15,"bold"),width=13,bg='blue',fg='white')
        btn_update.grid(row=1,column=0,padx=1,pady=5) 
        
        btn_delete=Button(button_frame,text="Delete",command=self.delete_data,font=("arial",15,"bold"),width=13,bg='blue',fg='white')
        btn_delete.grid(row=2,column=0,padx=1,pady=5)

        btn_clear=Button(button_frame,text="Clear",command=self.reset_data,font=("arial",15,"bold"),width=13,bg='blue',fg='white')
        btn_clear.grid(row=3,column=0,padx=1,pady=5)        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #lower frame
        
        lower_frame=LabelFrame(Main_frame,bd=2,relief=RIDGE,bg="white",text="Employee Information Table",font=('times new roman',11,'bold'),fg="red")
        lower_frame.place(x=10,y=290,width=1380,height=270)
        
        # search frame 
        
        search_frame=LabelFrame(lower_frame,bd=2,relief=RIDGE,bg="white",text="Search Employee Information",font=('times new roman',11,'bold'),fg="red")
        search_frame.place(x=0,y=0,width=1470,height=60)
        
        search_by=Label(search_frame,font=("arial",11,"bold"),text='Search By:',fg='white',bg='red')
        search_by.grid(row=0,column=0,sticky=W,padx=5)
        
        #search
        
    
        
        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,state='readonly',font=("arial",12,"bold"),width=18)
        com_txt_search['value']=("Select Option","Phone","ID_Proof")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5)
        
        
        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=("arial",11,"bold"))
        txt_search.grid(row=0,column=2,padx=5)  
         
        btn__search=Button(search_frame,command=self.search_data,font=("arial",11,"bold"),width=14,text="Search",bg="blue")
        btn__search.grid(row=0,column=3,padx=5) 
        
        btn__Showall=Button(search_frame,command=self.fetch_data,font=("arial",11,"bold"),width=14,text="Show All",bg="blue")
        btn__Showall.grid(row=0,column=4,padx=5) 
        
        #employee table
        
        table_frame=Frame(lower_frame,bd=3,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1375,height=170)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.employee_table=ttk.Treeview(table_frame,column=("dep","name","desig","email","address","marital","dob","doj","idproofcomb","idproofnumber","gender","phone","country","salary",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X) 
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)  
        
        self.employee_table.heading('dep',text='Department')
        self.employee_table.heading('name',text='Name')
        self.employee_table.heading('desig',text='Designation')
        self.employee_table.heading('email',text='Email')
        self.employee_table.heading('address',text='Address')
        self.employee_table.heading('marital',text='Marital_Status')
        self.employee_table.heading('dob',text='DOB')
        self.employee_table.heading('doj',text='DOJ')
        self.employee_table.heading('idproofcomb',text='ID_Type')
        self.employee_table.heading('idproofnumber',text='ID_Proof')
        self.employee_table.heading('gender',text='Gender')
        self.employee_table.heading('phone',text='Phone')
        self.employee_table.heading('country',text='Country')
        self.employee_table.heading('salary',text='Salary')
        
        self.employee_table['show']='headings'
        self.employee_table.column('dep',width=100)
        self.employee_table.column('name',width=100)
        self.employee_table.column('desig',width=100)
        self.employee_table.column('email',width=100)
        self.employee_table.column('address',width=100)
        self.employee_table.column('marital',width=100)
        self.employee_table.column('dob',width=100)
        self.employee_table.column('doj',width=100)
        self.employee_table.column('idproofcomb',width=100)
        self.employee_table.column('idproofnumber',width=100)
        self.employee_table.column('gender',width=100)
        self.employee_table.column('phone',width=100)
        self.employee_table.column('country',width=100)
        self.employee_table.column('salary',width=100)
        
        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    
    # Functions for all varaiables
    
    def add_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Protr@der1',database='mydata')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into emp values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                                  ( self.var_dep.get(),
                                    self.var_name.get(),
                                    self.var_designation.get(),
                                    self.var_email.get(),
                                    self.var_address.get(),
                                    self.var_married.get(),
                                    self.var_dod.get(),
                                    self.var_doj.get(),
                                    self.var_idproofcomb.get(),
                                    self.var_idproofnumber.get(),
                                    self.var_gender.get(),
                                    self.var_phone.get(),
                                    self.var_country.get(),
                                    self.var_salary.get()
                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success",'Employee data has been added',parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f'Due to:{str(es)}',parent=self.root)
    
    
    #fetch data
    
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='root',password='Protr@der1',database='mydata')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from emp')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.employee_table.delete(* self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        
    
    #get cursor
    
    def get_cursor(self,event):
        cursor_row=self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        data=content['values']
        
        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_designation.set(data[2])
        self.var_email.set(data[3])
        self.var_address.set(data[4])
        self.var_married.set(data[5])
        self.var_dod.set(data[6])
        self.var_doj.set(data[7])
        self.var_idproofcomb.set(data[8])
        self.var_idproofnumber.set(data[9])
        self.var_gender.set(data[10])
        self.var_phone.set(data[11])
        self.var_country.set(data[12])
        self.var_salary.set(data[13])
        
    def update_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                update=messagebox.askyesno('Update','Are you sure for the update')
                if update>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='Protr@der1',database='mydata')
                    my_cursor=conn.cursor()
                    my_cursor.execute('update emp set Department=%s,Name=%s,Designation=%s,Email=%s,Address=%s,Marital_Status=%s,DOB=%s,DOJ=%s,ID_Type=%s,Gender=%s,Phone=%s,Country=%s,Salary=%s where ID_Proof=%s',(
                        
                                                                                    self.var_dep.get(),
                                                                                    self.var_name.get(),
                                                                                    self.var_designation.get(),
                                                                                    self.var_email.get(),
                                                                                    self.var_address.get(),
                                                                                    self.var_married.get(),
                                                                                    self.var_dod.get(),
                                                                                    self.var_doj.get(),
                                                                                    self.var_idproofcomb.get(),
                                                                                    self.var_gender.get(),
                                                                                    self.var_phone.get(),
                                                                                    self.var_country.get(),
                                                                                    self.var_salary.get(),
                                                                                    self.var_idproofnumber.get()
                                                                                                                                            ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Employee sucessfully updated',parent=self.root)
                
            except Exception as es:
                messagebox.showerror("Error",f'Due to:{str(es)}',parent=self.root)
                    
                
    def delete_data(self):
        if self.var_idproofnumber.get()=="":
            messagebox.showerror('Error','Please select a row')  
        else:
            try:
                delete=messagebox.askyesno('Delete','Do you want to surely delete',parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host='localhost',username='root',password='Protr@der1',database='mydata')
                    my_cursor=conn.cursor()
                    sql='delete from emp where ID_PROOF=%s '
                    value=(self.var_idproofnumber.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Delete','Employee sucessfully deleted',parent=self.root)
                
            except Exception as es:
                messagebox.showerror("Error",f'Due to:{str(es)}',parent=self.root)
                
    
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_name.set("")
        self.var_designation.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_married.set("Marital Status")
        self.var_dod.set("")
        self.var_doj.set("")
        self.var_idproofcomb.set("ID Proof")
        self.var_idproofnumber.set("")
        self.var_gender.set("")
        self.var_phone.set("")
        self.var_country.set("")
        self.var_salary.set("")
        
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror('Error','Please select a option')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='root',password='Protr@der1',database='mydata')
                my_cursor=conn.cursor()
                my_cursor.execute('select * from emp where ' +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.employee_table.delete(* self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("",END,values=i)
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f'Due to:{str(es)}',parent=self.root)
                
                                        
                
                
        
        
        
        
        
        
                
            
        
        
        
           
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
    
if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()
        
        
    