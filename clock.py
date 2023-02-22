from tkinter import *
from PIL import Image, ImageTk
import datetime
from tkinter import messagebox
import playsound
import pyttsx3

engine = pyttsx3.init()
volume = engine.getProperty('volume')
print(volume) 
engine.setProperty('volume',1.0)


# from gtts import gTTS
# import os

# tts = gTTS(text='get up Rahul', lang='en')
# filename = 'hello.mp3'
# tts.save(filename)
# os.system(f'start {filename}')

# mytext = 'wake up Rahul'
# language = 'en'
# myobj = gTTS(text=mytext, lang=language, slow=False)
# myobj.save('welcome.mp3')
# os.system("mpg321 welcome.mp3")

window = Tk()
window.config(bg='white')


frame = Frame(window, bg='white')
frame.grid(row=0, column=0, padx=150, pady=20)


alarm = None
stop = False

def beep():
    # playsound.playsound('welcome.mp3')
    engine.say('hello, Rahul get up for next work.')
    engine.runAndWait()
    
showtime = StringVar()
def show_time():
    now = datetime.datetime.now()
    showtime.set(now.strftime('%B %d, %y %H:%M:%S'))
    if alarm == now.strftime('%H:%M') and stop == False:
        # print('Yes')
        beep()
    l3.after(1000, show_time)
    
def set_alarm():
    time = e1.get()
    global alarm
    global stop
    stop = False
    if ':' in e1.get():
        alarm = time
        e1.delete(0, len(alarm))
    else:
        messagebox.showerror('Error', 'Wrong Input')
        
def stop_alarm():
    global stop
    stop = True

l1 = Label(frame, text="Alarm Clock", bg='white', font=('Cooper black', '20'))
l1.grid(row=0, column=0, columnspan=2, pady=10, sticky=EW)

img = Image.open('img1.png').resize((250, 300))
photo = ImageTk.PhotoImage(img)
l2 = Label(frame, image=photo, bg='white', font=('Cooper black', '20'))
l2.grid(row=1, column=0, columnspan=2, pady=10)

l3 = Label(frame, text='Show Time',textvariable=showtime, bg='white', font=('Cooper black', '20'))
l3.grid(row=2, column=0, columnspan=2, pady=10, sticky=EW)
show_time()


l4 = Label(frame, text='Set Time', bg='white', font=('Cooper black', '15'), padx=15)
l4.grid(row=3, column=0, pady=10)

e1 = Entry(frame, font=('Cooper black', '15'), width=10)
e1.grid(row=3, column=1, pady=10)

b1 = Button(frame, text='Set Alarm', bg='tomato', font=('Cooper black', '15'), bd=0, command=set_alarm)
b1.grid(row=4, column=0, pady=10, sticky=EW)

b2 = Button(frame, text='Stop Alarm', bg='tomato', font=('Cooper black', '15'),bd=0, command=stop_alarm)
b2.grid(row=4, column=1, pady=10, sticky=EW, padx=10)


window.title('Remind Me')
window.geometry('600x600')
window.resizable(False, False)
window.mainloop()