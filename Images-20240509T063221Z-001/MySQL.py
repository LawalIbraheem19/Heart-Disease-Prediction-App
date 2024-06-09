import mysql.connector
import os
from mysql.connector import errorcode
from tkinter import messagebox

def Save_Data_MySql(B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R):
    try:
        # Establish a connection to the database
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password=os.environ.get("sql_pass")
        )
        mycursor = mydb.cursor()
        print("Connection Established!")
    except mysql.connector.Error as err:
        messagebox.showerror("Connection", f"Database connection not established! {err}")
        

    try:
        
        mycursor.execute("""CREATE database Heart_data""")
        
        mycursor.execute("""USE Heart_data""")
        
        # Create table if not exists
        mycursor.execute("""CREATE TABLE IF NOT EXISTS data (
                            user INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
                            Name VARCHAR(50),
                            Date VARCHAR(100),
                            DOB VARCHAR(100),
                            age VARCHAR(100),
                            sex VARCHAR(100),
                            Cp VARCHAR(100),
                            trestbps VARCHAR(100),
                            chol VARCHAR(100),
                            fbs VARCHAR(100),
                            restcg VARCHAR(100),
                            thalach VARCHAR(100),
                            exang VARCHAR(100),
                            oldpeak VARCHAR(100),
                            slope VARCHAR(100),
                            ca VARCHAR(100),
                            thal VARCHAR(100),
                            result VARCHAR(100)
                            )""")

        # Insert data into the table
        insertion_query = """INSERT INTO data (Name, Date, DOB, age, sex, Cp, trestbps, chol, fbs, restcg, thalach, exang, oldpeak, slope, ca, thal, result) 
                             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        value = (B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R)
        mycursor.execute(insertion_query, value)
        mydb.commit()
        messagebox.showinfo("Register", "New User added successfully!")
          
    except:
        mycursor.execute("USE Heart_data")
        
        # Establish a connection to the database
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password=os.environ.get("sql_pass"),
            database= "Heart_data"
        )
        mycursor = mydb.cursor()
        
        insertion_query = """INSERT INTO data (Name, Date, DOB, age, sex, Cp, trestbps, chol, fbs, restcg, thalach, exang, oldpeak, slope, ca, thal, result) 
                             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        value = (B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R)
        mycursor.execute(insertion_query, value)
        mydb.commit()
        messagebox.showinfo("Register", "New User added successfully!")
        
    finally:
        if mydb.is_connected():
            mycursor.close()
            mydb.close()
# Example usage
#Save_Data_MySql("Mr Unknown", "08/08/2023", "1979", "44", "1", "1", "233", "233", "1", "1", "233", "1", "233.0", "0", "2", "1", "0")