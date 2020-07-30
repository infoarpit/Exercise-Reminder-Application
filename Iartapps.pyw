try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *
import time
import datetime as dt
import json
from time import sleep
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import json
import datetime as dt
import time
execution_count = 0

t_now = dt.datetime.now()

# path to reminders.txt file
REM_FILE = "json/abf.txt"

a = []
execution_count=0


        # root (top level element) config
class REMINDER():
    def __init__(self):

        # root (top level element) config
        self.root = Tk()
        self.root.geometry("250x150+480+200")
        #self.root.geometry('%dx%d+%d+%d' % (220,270, 1050, 380))
        self.root.title("IALrt")
        self.root.iconbitmap("C:/Users/Arpit/Pictures/exercise.ico") 

        # Collect time information
        #t_now = dt.datetime.now()                       # Current time for reference.   [datetime object]
        #t_pom = 25*60                                   # Pomodoro time                 [int, seconds]
        #t_delta = dt.timedelta(0,t_pom)                 # Time delta in mins            [datetime object]
        #t_fut = t_now + t_delta                         # Future time for reference     [datetime object]
        #delta_sec = 1#60                                  # Break time, after pomodoro    [int, seconds]
        #t_fin = t_now + dt.timedelta(0,t_pom+delta_sec) # Final time (w/ 5 mins break)  [datetime object]
        # main frame (inside root) config
        self.mainFrame = Frame(self.root, padx=10, pady = 10)
        self.mainFrame.pack()

        # first field frame (inside main frame) config
        self.fieldRow1 = Frame(self.mainFrame, padx=5, pady=5)
        Label(self.fieldRow1, text="Current Time: "+t_now.strftime("%I:%M %p")).grid(row=0, column=0)
        #self.rem = Entry(self.fieldRow1)
        #self.rem.grid(row=0, column=1)
        self.fieldRow1.pack()

        # second field frame (inside main frame) config
#        self.fieldRow2 = Frame(self.mainFrame, padx=5, pady=5)
#        Label(self.fieldRow2, text="Active Between:", width=15).grid(row=0, column=0)
#        self.hrs1 = Entry(self.fieldRow2, width=5)
#        OptionMenu(self.fieldRow2, self.mins2,"00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11",
#         "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25","26", "27", "28", "29", "30", "31", "32", "33", "34", "35", 
#            "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60").grid(row=1, column=3)                
#        self.clk2 = StringVar()
 #       self.clk2.set('PM')
  #      OptionMenu(self.fieldRow2, self.clk2, 'AM', 'PM').grid(row=1, column=4)
 #       self.fieldRow2.pack()

        self.fieldRow3 = Frame(self.mainFrame, padx=5, pady=5)
        Label(self.fieldRow3, text="Reminder frequency (minutes):", width=25).grid(row=2, column=0)
        self.minsfrequency = Entry(self.fieldRow3, width=5)
        self.minsfrequency.grid(row=2, column=1)
        self.fieldRow3.pack()



        # button frame (inside main frame) config
        self.buttonRow = Frame(self.mainFrame, padx=10, pady=10)
        self.btn1 = Button(self.buttonRow, text="Save", command=self.saveReminder).grid(row=0, column=0)
        self.btn2 = Button(self.buttonRow, text="Cancel", command=self.cancelReminder).grid(row=0, column=2)
        self.buttonRow.grid_columnconfigure(1, minsize=10)
        self.buttonRow.pack()

        # call mainloop of Tk object
        self.root.mainloop()


    def saveReminder(self):
        '''
        utility function to save reminder
        '''
        #reminder = self.rem.get().strip()
 #       hrs1 = int(self.hrs1.get().strip())
  #      mins1 = int(self.mins1.get().strip())
   #     clk1 = self.clk1.get()
#        mins2 = int(self.mins2.get().strip())
#        clk2 = self.clk2.get()
#        if clk2 == 'PM':
#            hrs2 += 12    
#
#hrs1, mins1,hrs2,mins2,
        minsfrequency = int(self.minsfrequency.get().strip())    

        # update list of reminders
        with open(REM_FILE, 'r+') as f:
            reminders = json.load(f)
            f.seek(0)
            reminders.append((minsfrequency,(t_now.hour*60*60+t_now.minute*60)))
            f.write(json.dumps(reminders))
            f.truncate()

        self.root.destroy()
    

    def cancelReminder(self):
        '''
        utility function to close window
        '''
        self.root.destroy()






if __name__ == "__main__":
    REMINDER()

def center(win):
    # Call all pending idle tasks - carry out geometry management and redraw widgets.
    win.update_idletasks()
    # Get width and height of the screen
    width = win.winfo_width()
    height = win.winfo_height()
    # Calculate geometry
    x = (win.winfo_screenwidth() // 2) - (width)
    y = (win.winfo_screenheight() // 2) - (height)
    # Set geometry
    win.geometry('{}x{}+{}+{}'.format(220,270, 1050, 380))    


def eye_action(win, more):
    global execution_count
    global root
    print('Answer', more)
    if more:
        win.destroy()
        sleep(snooze_time)
        execution_count = execution_count + 1
        EyeReminderWindow()
    else:
        win.destroy()
        root.destroy()

def EyeReminderWindow():
    #global image_num
    global root
    print('Execution', execution_count)
    win = Toplevel()
    center(win)
    win.withdraw()
    win.update_idletasks()
    win.resizable(False,False)
    win.deiconify()
    win.title("IALrt")
    win.iconbitmap("C:/Users/Arpit/Pictures/exercise.ico")
 # width of the screen
 # height of the screen
    #ttk.Label(win,image=my_img1).grid(row=0,column=0)
    message1='Time for a little break!'
    #message2='Current Snooze time={0} seconds'.format(snooze_time)
    #message3 = 'Do you want more reminders?'
    i=execution_count % 5
    ttk.Label(win, text=message1).grid(column=0, row=0)
    ttk.Label(win,image=image_list[i]).grid(row=1,column=0,columnspan=2)
    #ttk.Label(win, text=message2).grid(column=0, row=1)
    #ttk.Label(win, text=message3).grid(column=0, row=2)
    #Label(mainFrame, text="Take a break!!",
     #            font = font.Font(family="Times", size=12),
      #               padx=20, pady=10, wraplength=300)
    #text.pack(fill=BOTH, expand=1)
    #yes_btn = ttk.Button(win, text='Sure', command=lambda: eye_action(win, True))
    #yes_btn.grid(column=0,row=3)
    ttk.Button(win, text='Dismiss', command=lambda: eye_action(win, False)).grid(column=1, row=3)
    #yes_btn.focus()
    win.lift()
    win.attributes('-topmost', True)
    win.after(5000, lambda:eye_action(win, True))

#im1=Image.open("C:/Users/Arpit/Desktop/imagefolder/p1.png")
#im2=Image.open("C:/Users/Arpit/Desktop/imagefolder/p2.png")
#im3=Image.open("C:/Users/Arpit/Desktop/imagefolder/p3.png")
#im4=Image.open("C:/Users/Arpit/Desktop/imagefolder/p4.png")
#im5=Image.open("C:/Users/Arpit/Desktop/imagefolder/p5.png")
#im6=Image.open("C:/Users/Arpit/Desktop/imagefolder/p6.png")
# list of reminders

with open(REM_FILE, 'r') as f:
    updated_reminders = json.loads(f.read())
    for ab in updated_reminders:
         if ab not in a:
             a.append(ab)
#print('\n\nThanks! You will get your first reminder in {0} seconds'.format(snooze_time))

t_pom = ab[0] *60   #ab[4]                                          
snooze_time=t_pom
# current hour and minute
cur_hrs = int(t_pom/3600)
minutes=t_pom-cur_hrs*60*60
cur_mins = int(minutes/60)
# find reminders to show
#for ab in a:
 #   rem_hrs = dt.datetime.now().hour
 #   rem_mins = dt.datetime.now().minute
 #   if cur_hrs == rem_hrs and cur_mins == rem_mins:
        # show reminder window
  #      REMINDER(a)
root = Tk()
root.withdraw()
execution_count = 0
#image_num=-1
my_img1=ImageTk.PhotoImage(Image.open("C:/Users/Arpit/Desktop/imagefolder/p1.png"))
my_img2=ImageTk.PhotoImage(Image.open("C:/Users/Arpit/Desktop/imagefolder/p2.png"))
my_img3=ImageTk.PhotoImage(Image.open("C:/Users/Arpit/Desktop/imagefolder/p3.png"))
my_img4=ImageTk.PhotoImage(Image.open("C:/Users/Arpit/Desktop/imagefolder/p4.png"))
my_img5=ImageTk.PhotoImage(Image.open("C:/Users/Arpit/Desktop/imagefolder/p5.png"))
my_img6=ImageTk.PhotoImage(Image.open("C:/Users/Arpit/Desktop/imagefolder/p6.png"))

image_list=[my_img1,my_img2,my_img3,my_img4,my_img5,my_img6]
#if dt.datetime.now().hour<ab[2] and dt.datetime.now().minute<ab[3]:
 #   if dt.datetime.now().hour>ab[0] and dt.datetime.now().minute>ab[1]:
EyeReminderWindow()  
#my_label=Label(image=my_img1)
#my_label.grid(row=2,column=2,columnspan=3)   
root.mainloop()
print('Exiting, bye')
