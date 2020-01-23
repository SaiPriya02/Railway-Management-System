#import modules
from Tkinter import *
import tkMessageBox
'''import sqlite3
#connect to the database
conn = sqlite3.connect('database.db')
print("successfully connected")
c = conn.cursor() '''
import MySQLdb
# Open database connection
conn = MySQLdb.connect("localhost","root","","database")

# prepare a cursor object using cursor() method
c = conn.cursor()

#tkinter window
class Application:
    def __init__(self, master):
        self.master = master
        #creating the frames in the master
        self.left = Frame(master, width=800, height=720, bg='grey')
        self.left.pack(side = LEFT)

        self.right = Frame(master, width=400, height=720, bg='black')
        self.right.pack(side = RIGHT)

        #labels for the window
        self.heading = Label(self.left, text = "Railway Bookings", font=('Cocogoose 40'), fg='white', bg='grey')
        self.heading.place(x=0, y=0)

        self.New_Booking = Button(self.right, text="Book New Ticket", width=30, height=1, bg='grey', fg='black', font=('Cocogoose 10'), command=lambda: self.new_ticket())
        self.New_Booking.place(x=65, y=100)
        
        self.Search_Booking = Button(self.right, text="Search Booking", width=30, height=1, bg='grey', fg='black', font=('Cocogoose 10'), command=lambda: self.search())
        self.Search_Booking.place(x=65, y=150)

        self.Cancel_Booking = Button(self.right, text="Cancel Ticket", width=30, height=1, bg='grey', fg='black', font=('Cocogoose 10'), command=lambda: self.cancel())
        self.Cancel_Booking.place(x=65, y=200)

    def new_ticket(self):
        self.res_no = Label(self.left, text="Reservation No.", font=('Cocogoose_Light 15'), fg='white', bg='grey')
        self.res_no.place(x=1, y=100)

        self.train_no = Label(self.left, text="Train No.", font=('Cocogoose_Light 15'), fg='white', bg='grey')
        self.train_no.place(x=1, y=130)

        self.seat_no = Label(self.left, text="Seat No.", font=('Cocogoose_Light 15'), fg='white', bg='grey')
        self.seat_no.place(x=1, y=160)

        self.tt = Label(self.left, text="Ticket Type", font=('Cocogoose_Light 15'), fg='white', bg='grey')
        self.tt.place(x=1, y=190)

        self.time = Label(self.left, text="Departure at", font=('Cocogoose_Light 15'), fg='white', bg='grey')
        self.time.place(x=1, y=220)

        self.name = Label(self.left, text="Name", font=('Cocogoose_Light 15'), fg='white', bg='grey')
        self.name.place(x=1, y=250)

        self.pp_no = Label(self.left, text="Passport No.", font=('Cocogoose_Light 15'), fg='white', bg='grey')
        self.pp_no.place(x=1, y=280)

        self.From = Label(self.left, text="From", font=('Cocogoose_Light 15'), fg='white', bg='grey')
        self.From.place(x=1, y=310)

        self.to = Label(self.left, text="To", font=('Cocogoose_Light 15'), fg='white', bg='grey')
        self.to.place(x=1, y=340)

        #entries for all labels----------------------------------------
        #reservation no.
        self.res_ent = Entry(self.left, width=40)
        self.res_ent.place(x=150, y=105) #y increases by 30
        #train no.
        self.train_ent = Entry(self.left, width=40)
        self.train_ent.place(x=150, y=135)
        #seat no.
        self.seat_ent = Entry(self.left, width=40)
        self.seat_ent.place(x=150, y=165)
        #ticket type
        self.tt_ent = Entry(self.left, width=40)
        self.tt_ent.place(x=150, y=195)
        #time of arrival
        self.toa_ent = Entry(self.left, width=40)
        self.toa_ent.place(x=150, y=225)
        #name
        self.name_ent = Entry(self.left, width=40)
        self.name_ent.place(x=150, y=255)
        #passport no.
        self.pp_ent = Entry(self.left, width=40)
        self.pp_ent.place(x=150, y=285)
        #from
        self.from_ent = Entry(self.left, width=40)
        self.from_ent.place(x=150, y=315)
        #to
        self.to_ent = Entry(self.left, width=40)
        self.to_ent.place(x=150, y=345)
        
        #button to perform the command
        self.submit = Button(self.left, text="Book Ticket", width=15, height=1, bg='black', fg='grey', font=('Cocogoose 10'), command= self.add_booking)
        self.submit.place(x=250,y=380)


        #function to call when button is pressed 
    def add_booking(self):
        #take all inputs
        #check if seats are available
            #if available, book seat and mention price
            #if not available, display message saying choose another flight

        self.val1 = self.res_ent.get()
        self.val2 = self.train_ent.get()
        self.val3 = self.seat_ent.get()
        self.val4 = self.toa_ent.get()
        self.val5 = self.name_ent.get()
        self.val6 = self.pp_ent.get()
        self.val7 = self.from_ent.get()
        self.val8 = self.to_ent.get()
        self.val9 = self.tt_ent.get()

            #check if user input is empty
        if self.val1=='' or self.val2=='' or self.val3=='' or self.val4=='' or self.val5=='' or self.val6=='' or self.val7=='' or self.val8=='' or self.val9=='':
            tkMessageBox.showinfo("Warning", "Please fill all the fields.")
        else:
            sql = "INSERT INTO passenger (Reservation_no, Train_no, Seat_no, Ticket_type, Time_of_departure, Name, Passport_no, Source, Destination) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            c.execute(sql, (self.val1, self.val2, self.val3, self.val9, self.val4, self.val5, self.val6, self.val7, self.val8))
            #trig = "create trigger valFilled after insert on passenger for each row update schedules set No_Booked=No_Booked+1 where passengers.Train_no=schedules.Train_no"
            #c.execute(trig)
            conn.commit()
            tkMessageBox.showinfo("Success", "Reservation made for " + str(self.val5))


    def search(self):
        #enter res number to search table
        self.to = Label(self.left, text="SEARCH: Enter the Reservation Number", font=('Cocogoose 15'), fg='white', bg='grey')
        self.to.place(x=5, y=415)
        #entry box
        self.res_ent = Entry(self.left, width=45)
        self.res_ent.place(x=5, y=450)
        #search button that leads you to the next function that does the actual searching
        self.srch = Button(self.left, text="Search", width=15, height=1, bg='black', fg='grey', font=('Cocogoose 10'), command= self.actual_search)
        self.srch.place(x=5, y=480)

    def actual_search(self):
        val = self.res_ent.get() #res no is stored in val
        #now you search if the table has the res no and then display details
        query1='SELECT * FROM passenger WHERE Reservation_no=%s'
        c.execute(query1, val)
        data=c.fetchall()
        #print(data)
        if data != []:
            tkMessageBox.showinfo("Reservation Details", data)
        else:
            tkMessageBox.showinfo("Error", "Reservation number does not exist in the records.")

    def cancel(self):
        #ask for what you wanna cancel
        #delete the entry in passenger
        #update the number of seats
        self.to = Label(self.left, text="CANCELLATION: Enter the Reservation Number", font=('Cocogoose 15'), fg='white', bg='grey')
        self.to.place(x=5, y=515)
        #entry box
        self.res_ent = Entry(self.left, width=45)
        self.res_ent.place(x=5, y=550)
        #button
        self.sc = Button(self.left, text="Search and Cancel", width=15, height=1, bg='black', fg='grey', font=('Cocogoose 10'), command= self.actual_cancel)
        self.sc.place(x=5, y=580)

    def actual_cancel(self):
        val = self.res_ent.get() #res no is stored in val
        #first you increase the seat count

        #now you remove entry from passenger
        query2='DELETE FROM passenger WHERE Reservation_no=%s'
        c.execute(query2, val)
        conn.commit()
        tkMessageBox.showinfo("Alert","Reservation Cancelled")


#creating the object
root = Tk()
b= Application(root)
#resolution of the window
root.geometry("1200x720+0+0")

#preventing the resize feature
root.resizable(False, False)

#end of loop
root.mainloop()