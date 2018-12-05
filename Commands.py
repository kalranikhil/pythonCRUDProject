# Author : Nikhil Kalra #
# CST8333 Final project#
# December 2,2018 #
import tkinter

import mysql.connector
import sys
import csv
# Primitive Data Type to Declare Variables # by Nikhil Kalra
data_filename = "32100054.csv"
firstLine = ""
mydb = ""
mydb = mysql.connector.connect( # Representing Database Connectivity
            host="localhost",
            user="root",
            passwd="Nikhil1997",
            database="nik"
        )
mycursor = mydb.cursor()
class Commands:#Class used as connectivity class and to run SQL Queries by Nikhil Kalra

    def readFile(): # Method used to read file by Nikhil Kalra
        global firstLine
        global mydb
        global mycursor

        firstLine = True

        mycursor.execute("DROP TABLE IF EXISTS finalProject")
        mycursor.execute("""CREATE TABLE finalProject (ID INT PRIMARY KEY AUTO_INCREMENT, 
        REF_DATE VARCHAR(255), 
        GEO VARCHAR(255), 
        DGUID VARCHAR(255), 
        FoodCategories VARCHAR(255), 
        Commodity VARCHAR(255), 
        UOM VARCHAR(255), 
        UOM_ID VARCHAR(255), 
        SCALAR_FACTOR VARCHAR(255), 
        SCALAR_ID VARCHAR(255), 
        VECTOR VARCHAR(255), 
        COORDINATE VARCHAR(255), 
        VALUE VARCHAR(255), 
        STATUS VARCHAR(255), 
        SYMBOL VARCHAR(255), 
        TERMINATE VARCHAR(5), 
        DECIMALS VARCHAR(255)
        );
        """)

        try: # FILE IO by Nikhil Kalra
            with open(data_filename) as csv_file:
                csv_data = csv.reader(csv_file)
                for row in csv_data:
                    if firstLine: # DECISION STRUCTURE by Nikhil Kalra
                        firstLine = False
                    else:
                        mycursor.execute("""
                        INSERT INTO finalProject(REF_DATE, GEO, DGUID, FoodCategories, Commodity, UOM, UOM_ID, SCALAR_FACTOR, SCALAR_ID, VECTOR, COORDINATE, VALUE, STATUS, SYMBOL, TERMINATE, DECIMALS )
                         VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s");
                         """, row)
        except IOError:
            print("Error in Syntax. Please check and change the syntax")
        # close the connection to the database.
        mycursor.execute("""
        ALTER TABLE finalProject
        DROP COLUMN VALUE,
        DROP COLUMN TERMINATE;
        """)
        mydb.commit()
        print("Fetching Done")
        tkinter.messagebox.showinfo("Information", "Data Fetched Successfully")
        return "Pass"

    def insertData(refDate, geo, dguid, fc, comm, uom, uomid, scalarf, scalari, vector, coords, status, symbol, decimal): # Method used to insert  data by Nikhil Kalra
        global mydb
        global mycursor

        try:
            mycursor.execute("""
            INSERT INTO finalProject(REF_DATE, GEO, DGUID, FoodCategories, Commodity, UOM, UOM_ID, SCALAR_FACTOR, SCALAR_ID, VECTOR, COORDINATE, STATUS, SYMBOL, DECIMALS)
                             VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}",  "{}",  "{}");
            """.format(refDate, geo, dguid, fc, comm, uom, uomid, scalarf, scalari, vector, coords, status, symbol, decimal))
        except mysql.connector.Error as error:
            print(error)
        mydb.commit()

        print("Inserting Done")
        return "Pass"

    def updateData(refDate, geo, dguid, fc, comm, uom, uomid, scalarf, scalari, vector, coords, status, symbol, decimal, id): # Method used to update data by Nikhil Kalra
        global mydb
        global mycursor
        try:
            mycursor.execute("""
            UPDATE finalProject SET REF_DATE = "{}", GEO = "{}", DGUID = "{}", FoodCategories = "{}", Commodity = "{}", UOM = "{}", UOM_ID = "{}", SCALAR_FACTOR = "{}", SCALAR_ID = "{}", VECTOR = "{}", COORDINATE = "{}", STATUS = "{}", SYMBOL = "{}", DECIMALS = "{}" WHERE ID = "{}";
            """.format(refDate, geo, dguid, fc, comm, uom, uomid, scalarf, scalari, vector, coords, status, symbol, decimal, id))
        except mysql.connector.Error as error:
            print(error)
        mydb.commit()

        print("Updating Done")
        return "Pass"

    def deleteData(id): # Method used to delete data by Nikhil Kalra
        global mydb
        global mycursor
        try: # EXCEPTION HANDLING
            mycursor.execute("""
            DELETE FROM finalProject WHERE ID = "{}";
            """.format(id))
        except mysql.connector.Error as error:
            print(error)
        mydb.commit()

        print("Deleting Done")
        return "Pass"

    def searchData(ID): # Method used to search data by Nikhil Kalra
        global mydb
        global mycursor

        mycursor.execute("SELECT * FROM finalProject WHERE ID = " + ID)
        data = mycursor.fetchone()

        result = [0] * len(data)
        i = 0
        for row in data: # LOOPING STRUCTURE by Nikhil Kalra
            result[i] = row
            i = i+1

        return result
