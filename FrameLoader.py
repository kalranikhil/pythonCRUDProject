# Author : Nikhil Kalra #
# CST8333 Final project#
# December 2,2018 #
from tkinter import *
import tkinter.messagebox
import sys
import Commands
import threading

# Data Type to Declare Class's Object # by Nikhil Kalra
command = Commands.Commands

# Primitive Data Type to Declare Variables # by Nikhil Kalra
primary = " "
primaryKeyEntry = " "
refEntry = " "
geoEntry = " "
dguidEntry = " "
foodCategoriesEntry = " "
commodityEntry = " "
uomEntry = " "
uomIdEntry = " "
scalarFactorEntry = " "
scalarIdEntry = " "
vectorEntry = " "
coordinateEntry = " "
statusEntry = " "
symbolEntry = " "
decimalsEntry = " "
primaryKeyButton = " "
progress = ""

class FrameLoader(Commands.Commands): #Class used as main class  by Nikhil Kalra. Also, showing Inheritance

    def __init__(self, master): #Method used to make GUI with different widgets by Nikhil Kalra

        master.wm_title("Final Project By Nikhil Kalra")
        mainFrame = Frame(master, bg="white")
        mainFrame.pack()

        self.menuBar(master)
        self.topFrame(mainFrame)
        self.bottomFrame(mainFrame)


    def menuBar(self, master):  # Method used to make Menu Bar by Nikhil Kalra

        menuBar = Menu(master)
        master.config(menu=menuBar)

        fileMenu = Menu(menuBar)
        menuBar.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="Read Data", command=self.fetchData)
        fileMenu.add_command(label="Insert Data", command=self.insertData)
        fileMenu.add_command(label="Update Data", command=self.updateData)
        fileMenu.add_command(label="Delete Data", command=self.deleteData)

        editMenu = Menu(menuBar)
        menuBar.add_cascade(label="Tools", menu=editMenu)
        editMenu.add_command(label="Quit", command=root.destroy)

    def topFrame(self, mainFrame):  # Method used to make Top Frame by Nikhil Kalra
        global primary
        global primaryKeyEntry
        global primaryKeyButton

        topFrame = Frame(mainFrame)
        topFrame.pack(side=TOP, fill=Y)

        primaryKeyLabel = Label(topFrame, text="Record Number", bg="black", fg="white")
        primaryKeyLabel.grid(row=0)

        primaryKeyEntry = Entry(topFrame)
        primaryKeyEntry.grid(row=0, column=1)
        primary = primaryKeyEntry.get()
        primaryKeyButton = Button(topFrame, text="SEARCH", fg="blue", command=self.searchData)
        primaryKeyButton.grid(row=0, column=2)

    def bottomFrame(self, mainFrame):  # Method used to make bottom Frame by Nikhil Kalra

        global refEntry
        global geoEntry
        global dguidEntry
        global foodCategoriesEntry
        global commodityEntry
        global uomEntry
        global uomIdEntry
        global scalarFactorEntry
        global scalarIdEntry
        global vectorEntry
        global coordinateEntry
        global statusEntry
        global symbolEntry
        global decimalsEntry

        bottomFrame = Frame(mainFrame, bg="black")
        bottomFrame.pack(side=BOTTOM, fill=Y)

        refLabel = Label(bottomFrame, text="REF_DATE", bg="black", fg="white")
        refLabel.grid(row=0)
        refEntry = Entry(bottomFrame)
        refEntry.grid(row=0, column=1)

        geoLabel = Label(bottomFrame, text="GEO", bg="black", fg="white")
        geoLabel.grid(row=1)
        geoEntry = Entry(bottomFrame)
        geoEntry.grid(row=1, column=1)

        dguidLabel = Label(bottomFrame, text="DGUID", bg="black", fg="white")
        dguidLabel.grid(row=2)
        dguidEntry = Entry(bottomFrame)
        dguidEntry.grid(row=2, column=1)

        foodCategoriesLabel = Label(bottomFrame, text="Food Categories", bg="black", fg="white")
        foodCategoriesLabel.grid(row=3)
        foodCategoriesEntry = Entry(bottomFrame)
        foodCategoriesEntry.grid(row=3, column=1)

        commodityLabel = Label(bottomFrame, text="Commodity", bg="black", fg="white")
        commodityLabel.grid(row=4)
        commodityEntry = Entry(bottomFrame)
        commodityEntry.grid(row=4, column=1)

        uomLabel = Label(bottomFrame, text="UOM", bg="black", fg="white")
        uomLabel.grid(row=5)
        uomEntry = Entry(bottomFrame)
        uomEntry.grid(row=5, column=1)

        uomIdLabel = Label(bottomFrame, text="UOM_ID", bg="black", fg="white")
        uomIdLabel.grid(row=6)
        uomIdEntry = Entry(bottomFrame)
        uomIdEntry.grid(row=6, column=1)

        scalarFactorLabel = Label(bottomFrame, text="SCALAR_FACTOR", bg="black", fg="white")
        scalarFactorLabel.grid(row=0, column=2)
        scalarFactorEntry = Entry(bottomFrame)
        scalarFactorEntry.grid(row=0, column=3)

        scalarIdLabel = Label(bottomFrame, text="SCALAR_ID", bg="black", fg="white")
        scalarIdLabel.grid(row=1, column=2)
        scalarIdEntry = Entry(bottomFrame)
        scalarIdEntry.grid(row=1, column=3)

        vectorLabel = Label(bottomFrame, text="VECTOR", bg="black", fg="white")
        vectorLabel.grid(row=2, column=2)
        vectorEntry = Entry(bottomFrame)
        vectorEntry.grid(row=2, column=3)

        coordinateLabel = Label(bottomFrame, text="COORDINATE", bg="black", fg="white")
        coordinateLabel.grid(row=3, column=2)
        coordinateEntry = Entry(bottomFrame)
        coordinateEntry.grid(row=3, column=3)

        statusLabel = Label(bottomFrame, text="STATUS", bg="black", fg="white")
        statusLabel.grid(row=4, column=2)
        statusEntry = Entry(bottomFrame)
        statusEntry.grid(row=4, column=3)

        symbolLabel = Label(bottomFrame, text="SYMBOL", bg="black", fg="white")
        symbolLabel.grid(row=5, column=2)
        symbolEntry = Entry(bottomFrame)
        symbolEntry.grid(row=5, column=3)

        decimalsLabel = Label(bottomFrame, text="DECIMALS", bg="black", fg="white")
        decimalsLabel.grid(row=6, column=2)
        decimalsEntry = Entry(bottomFrame)
        decimalsEntry.grid(row=6, column=3)

    def deleteData(self): # Method used to make delete data
        global primaryKeyEntry
        command.deleteData(primaryKeyEntry.get())
        primaryKeyEntry.delete(0, END)
        self.clearOutFields()
        tkinter.messagebox.showinfo("Information", "Data Deleted Successfully")

    def searchData(self): # Method used to make search data by Nikhil Kalra
        global refEntry
        global geoEntry
        global dguidEntry
        global foodCategoriesEntry
        global commodityEntry
        global uomEntry
        global uomIdEntry
        global scalarFactorEntry
        global scalarIdEntry
        global vectorEntry
        global coordinateEntry
        global statusEntry
        global symbolEntry
        global decimalsEntry
        global primaryKeyEntry

        self.clearOutFields()
        try:
            refEntry.insert(0, command.searchData(primaryKeyEntry.get())[1])
            geoEntry.insert(0, command.searchData(primaryKeyEntry.get())[2])
            dguidEntry.insert(0, command.searchData(primaryKeyEntry.get())[3])
            foodCategoriesEntry.insert(0, command.searchData(primaryKeyEntry.get())[4])
            commodityEntry.insert(0, command.searchData(primaryKeyEntry.get())[5])
            uomEntry.insert(0, command.searchData(primaryKeyEntry.get())[6])
            uomIdEntry.insert(0, command.searchData(primaryKeyEntry.get())[7])
            scalarFactorEntry.insert(0, command.searchData(primaryKeyEntry.get())[8])
            scalarIdEntry.insert(0, command.searchData(primaryKeyEntry.get())[9])
            vectorEntry.insert(0, command.searchData(primaryKeyEntry.get())[10])
            coordinateEntry.insert(0, command.searchData(primaryKeyEntry.get())[11])
            statusEntry.insert(0, command.searchData(primaryKeyEntry.get())[12])
            symbolEntry.insert(0, command.searchData(primaryKeyEntry.get())[13])
            decimalsEntry.insert(0, command.searchData(primaryKeyEntry.get())[14])
            print("Searching Done")
        except:
            tkinter.messagebox.showinfo("Warning", "Please put another ID NUMBER")


    def insertData(self): # Method used to make insert data by Nikhil Kalra
        global refEntry
        global geoEntry
        global dguidEntry
        global foodCategoriesEntry
        global commodityEntry
        global uomEntry
        global uomIdEntry
        global scalarFactorEntry
        global scalarIdEntry
        global vectorEntry
        global coordinateEntry
        global statusEntry
        global symbolEntry
        global decimalsEntry
        global primaryKeyEntry

        command.insertData(refEntry.get(), geoEntry.get(), dguidEntry.get(), foodCategoriesEntry.get(), commodityEntry.get(), uomEntry.get(), uomIdEntry.get(),
                           scalarFactorEntry.get(), scalarIdEntry.get(), vectorEntry.get(), coordinateEntry.get(),
                           statusEntry.get(), symbolEntry.get(), decimalsEntry.get())
        primaryKeyEntry.delete(0, END)
        self.clearOutFields()
        tkinter.messagebox.showinfo("Information", "Data Inserted Successfully")


    def updateData(self): # Method used to make update data by Nikhil Kalra
        global primaryKeyEntry
        global refEntry
        global geoEntry
        global dguidEntry
        global foodCategoriesEntry
        global commodityEntry
        global uomEntry
        global uomIdEntry
        global scalarFactorEntry
        global scalarIdEntry
        global vectorEntry
        global coordinateEntry
        global statusEntry
        global symbolEntry
        global decimalsEntry

        command.updateData(refEntry.get(), geoEntry.get(), dguidEntry.get(), foodCategoriesEntry.get(), commodityEntry.get(), uomEntry.get(), uomIdEntry.get(),
                           scalarFactorEntry.get(), scalarIdEntry.get(), vectorEntry.get(), coordinateEntry.get(),
                           statusEntry.get(), symbolEntry.get(), decimalsEntry.get(), primaryKeyEntry.get())
        tkinter.messagebox.showinfo("Information", "Data Updated Successfully")

    def clearOutFields(self): # Method used to make clear out fields by Nikhil Kalra
        global refEntry
        global geoEntry
        global dguidEntry
        global foodCategoriesEntry
        global commodityEntry
        global uomEntry
        global uomIdEntry
        global scalarFactorEntry
        global scalarIdEntry
        global vectorEntry
        global coordinateEntry
        global statusEntry
        global symbolEntry
        global decimalsEntry

        refEntry.delete(0, END)
        geoEntry.delete(0, END)
        dguidEntry.delete(0, END)
        foodCategoriesEntry.delete(0, END)
        commodityEntry.delete(0, END)
        uomEntry.delete(0, END)
        uomIdEntry.delete(0, END)
        scalarFactorEntry.delete(0, END)
        scalarIdEntry.delete(0, END)
        vectorEntry.delete(0, END)
        coordinateEntry.delete(0, END)
        statusEntry.delete(0, END)
        symbolEntry.delete(0, END)
        decimalsEntry.delete(0, END)

    def fetchData(self): # Method used to make New Thread and upload CSV in database by Nikhil Kalra. Also, it is representing Multithreading
        global progress
        startFetching = threading.Thread(target=command.readFile)
        startFetching.start()
        tkinter.messagebox.showinfo("Information", "Fetching is going on please wait.")


root = Tk()
b = FrameLoader(root)# Making an object or instance of Class by Nikhil Kalra
root.mainloop()