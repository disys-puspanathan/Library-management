import pyodbc as py
server = 'd2mtrainingdb.database.windows.net'
db = 'd2manalysistraining'
user = 'dbtuser'
pwd = 'Disys@2022'
conn = py.connect('DRIVER={SQL Server}'';SERVER=' + server +
';DATABASE=' + db +
'; UID=' + user +
'; PWD=' + pwd +
';Trusted_Connection=no')
cursor = conn.cursor()

#deleting
#SQLCommand = ("DELETE FROM product WHERE student_id in (71)")    

#Processing Query    
cursor.execute('''DELETE FROM gp_student_details WHERE student_id in (71)''')     

#Commiting any pending transaction to the database.    
conn.commit()    

#closing connection    
print("Data Successfully Deleted")   
conn.close()