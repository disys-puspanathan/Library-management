from mailbox import Error
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#from PIL import ImageTk,Image
import os,glob
import pyodbc as py

class Search(Tk):
    def __init__(self):
        super().__init__()
        f = StringVar()
        g = StringVar()
        self.title("SEARCH STUDENT")
        self.maxsize(800,520)
        self.canvas = Canvas(width=1366, height=768, bg='blue')
        self.canvas.pack()
        l1=Label(self,text="Search Student",bg='orange', font=("Courier new",20,'bold')).place(x=290,y=40)
        l = Label(self, text="Search By",bg='orange', font=("Courier new", 15, 'bold')).place(x=180, y=100)

        def insert(data):
            self.listTree.delete(*self.listTree.get_children())
            for row in data:
                self.listTree.insert("","end",text = row[0], values = (row[1],row[2],row[3]))


        def ge():
            if (len(self.entry.get())) == 0:
                messagebox.showinfo('Error', 'First select a item')
            elif (len(self.combo.get())) == 0:
                messagebox.showinfo('Error', 'Enter the '+ self.combo.get())
            elif self.combo.get() == 'student_name':
                try:
                    server = 'd2mtrainingdb.database.windows.net'
                    db = 'd2manalysistraining'
                    user = 'dbtuser'
                    pwd = 'Disys@2022'
                    self.conn = py.connect('DRIVER={SQL Server}'';SERVER=' + server +
                      ';DATABASE=' + db +
                      '; UID=' + user +
                      '; PWD=' + pwd +
                      ';Trusted_Connection=no')
                    self.cursor = self.conn.cursor()
                    name = self.entry.get()
                    self.cursor.execute("Select * from gp_student_details where student_name = " + name )
                    pc = self.cursor
                    if pc:
                        insert(pc)
                    else:
                        messagebox.showinfo("Oop's","Name not found")
                except Error:
                    messagebox.showerror("Error", "Something goes wrong")
            elif self.combo.get() == 'ID':
                try:
                    server = 'd2mtrainingdb.database.windows.net'
                    db = 'd2manalysistraining'
                    user = 'dbtuser'
                    pwd = 'Disys@2022'

                    self.conn = py.connect('DRIVER={SQL Server}'';SERVER=' + server +
                      ';DATABASE=' + db +
                      '; UID=' + user +
                      '; PWD=' + pwd +
                      ';Trusted_Connection=no')
                    self.cursor = self.conn.cursor()
                    id = self.entry.get()
                    self.cursor.execute("Select * from gp_student_details where student_id =  " + id )
                    pc = self.cursor.fetchall()
                    if pc:
                        insert(pc)
                    else:
                        messagebox.showinfo("Oop's", "Id not found")
                except Error:
                    messagebox.showerror("Error", "Something goes wrong")


        self.b= Button(self,text="Find",width=8, bg = 'orange', font=("Courier new",8,'bold'),command= ge )
        self.b.place(x=400,y=170)
        self.combo=ttk.Combobox(self,textvariable=g,values=["Name","ID"],width=40,state="readonly")
        self.combo.place(x = 310, y = 105)
        self.entry = Entry(self,textvariable=f,width=43)
        self.entry.place(x=310,y=145)
        self.la = Label(self, text="Enter",bg = 'orange', font=("Courier new", 15, 'bold')).place(x=180, y=140)

        def handle(event):
            if self.listTree.identify_region(event.x,event.y) == "separator":
                return "break"


        self.listTree = ttk.Treeview(self, height=13,columns=('Student Name', 'sex', 'DOB'))
        self.vsb = ttk.Scrollbar(self,orient="vertical",command=self.listTree.yview)
        self.listTree.configure(yscrollcommand=self.vsb.set)
        
        self.listTree.heading("#0", text='student_id', anchor='w')
        self.listTree.column("#0", width=100, anchor='w')
        
        self.listTree.heading("Student Name", text='student_name')
        self.listTree.column("Student Name", width=200, anchor='center')
        
        self.listTree.heading("sex", text='sex')
        self.listTree.column("sex", width=200, anchor='center')
        
        self.listTree.heading("DOB", text='date_of_birth')
        self.listTree.column("DOB", width=200, anchor='center')
        
        self.listTree.place(x=40, y=200)
        self.vsb.place(x=743,y=200,height=287)
        
        ttk.Style().configure("Treeview", font=('Times new Roman', 15))

Search().mainloop()
