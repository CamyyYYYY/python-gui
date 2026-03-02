from tkinter import *
from playsound import playsound
import schedule,time, threading

# widgets = gui elements: buttons, textbooks, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk() #instantiate an instance of a window
window.geometry("670x670") #size of window
window.title("MyWindow") #renames the window from "Tk"

icon=PhotoImage(file='logo.png') #picks picture for logo
window.iconphoto(True,icon) #sets picture as logo
window.config(background="blue") #changes background color

photo = PhotoImage(file='logo.png')

label = Label(window,
              text="Hello please give me kiss", 
              font=('Arial', 40, 'bold'),
              fg='green',
              bg='blue', #label is a widget that has text or images
              relief=RAISED,
              bd=10,
              padx=10,
              pady=10,
              image=photo,
              compound='bottom')
#label.place(x=0,y=0) #widget position controller function
label.pack() #places button

def givemeakiss(): #runs "give me kiss audio every 5 seconds"

    try:
        playsound("hellogivemeakiss.wav")
    except Exception as e:
        print(f"Error playing sound: {e}")

schedule.every(5).seconds.do(givemeakiss)

def stupiduglyfunction(): #stupid annoying function I had to look up to check every 1 sec if the function before ran every 5 seconds
    while True:
        schedule.run_pending()
        time.sleep(1)

threading.Thread(target=stupiduglyfunction, daemon=True).start()

#placed button section here so its nice fr
count=0 #counts
def clickme():
    print("mwah!")
    global count #sets as global variable
    count +=1 #adds to count
    #print(count) #prints number of kisses
    playsound("kiss.wav")
    label.config(text=count) #lets label count increase
    label2.place(x=20,y=0) #places button after clicking
    label2.after(1000,hide_labeltwo) #moves place_forget into another function so that the main one doesnt freeze, removes image after 1 second (1000 milliseconds)

def hide_labeltwo():
    label2.place_forget()
    playsound("thankyou.wav")

button = Button(window,text='Click to kiss!') #places button 
button.config(command=clickme) #performs function callback from clickme (prints hello)
button.config(font=('Ink Free',50,'bold')) #font type and size 
button.config(bg='black') #background color
button.config(fg='white') #font color
button.config(activebackground='green') #changes bg when pressed
button.config(activeforeground='yellow') #change font when pressed
imageone = PhotoImage(file='kiss.png') #image to press as button, replaces text unless otherwise stated
imagetwo = PhotoImage(file='thanks.png') #image that pops up after pressing
button.config(image=imageone) #sets the image on the button as imageone (which is our png file one line above)
button.config(compound='right') #puts image at right so text and image are not on same plane
button.config(state=ACTIVE) #allows button to work
#button.config(state=DISABLED) #disables button
label=Label(window,text=count) #puts a label that shows how many kisses
label.config(font=('Monospace',50)) #sets font and size
label.pack() #places label

button.pack() #places button

label2 = Label(window,image=imagetwo) #places label using thanks image


window.mainloop() #places window on screen, it also listens for events

while True: #end of stupid ugly background function
    time.sleep(10)