from tkinter import *
import speech_recognition as sr

LARGE_FONT = ('Helvetica', 16 ,'bold')
RELAXING_TIME = 4000
N_TRIALS = 3
COUNT = -2
N_INTERVALS = 2 * N_TRIALS + 1
r = sr.Recognizer()
m = sr.Microphone()


global correct_click, wrong_click, total_click
correct_click = 0
wrong_click = 0
total_click = 0


def retrieve():
    global total_click
    total_click = correct_click + wrong_click
    print("The total number of attempts is", total_click)
    print("The number of correct results is",correct_click)
    print("The number of wrong results is",wrong_click)
    root1.destroy()


def correctclick():
    global correct_click
    correct_click = correct_click + 1
    #print(correct_click)
    raise_frame(x4)


def wrongclick():
    global wrong_click
    wrong_click = wrong_click + 1
    #print(wrong_click)
    raise_frame(x4)
    


def insert(limit):
    T.insert(END, "{}".format(limit))

"""def listen(sourcee):
    global audioo
    audioo = r.listen(sourcee)
    return audioo
"""
def raise_frame(frame):
    frame.tkraise()
    global audio
    global value

    if frame == x1:
        with m as source:
            r.adjust_for_ambient_noise(source)
        frame.after(RELAXING_TIME, lambda: raise_frame(x3))

    elif frame == x3:
        frame.after(RELAXING_TIME, lambda: raise_frame(x4))

    elif frame == x4:
        with m as source:
            audio = r.listen(source)
        frame.after(RELAXING_TIME, lambda: raise_frame(x5))

    elif frame == x5:
        frame.after(RELAXING_TIME, lambda: raise_frame(x6))

    elif frame == x6:
        value = r.recognize_sphinx(audio)
        print("You said {}".format(value))
        insert(value)


root1 = Tk()

x1 = Frame(root1)
x2 = Frame(root1)
x3 = Frame(root1)
x4 = Frame(root1)
x5 = Frame(root1)
x6 = Frame(root1)

for frame in (x1, x3, x4, x5, x6):
    frame.grid(row=0, column=0, sticky='nsew')


logo = PhotoImage(file="images.png")
exp = """A moment of Silence please......"""

w2 = Label(x1,justify=LEFT,padx = 10,
              text = exp,font = "Helvetica 16 bold").pack()
w1 = Label(x1,image=logo)
w1.pack()

w8 = Label(x2, text="Result......", font="Helvetica 16 bold")
w8.pack()

T = Text(x2, height=10, width=30)
T.pack()

button = Button(x2, text="Correct", fg="white", padx="25", pady="10", bg="green", command=correctclick)
button.pack()

slogan = Button(x2, text="Wrong", fg="white", padx="25", pady="15", bg="red", command=wrongclick)
slogan.pack()

end = Button(x2, text="End Session", padx="25", pady="15", bg="blue", fg="white", command=retrieve)
end.pack()

x2.grid(row=0, column=1)

w3 = Label(x3, text="Threshold Established.......", font="Helvetica 16 bold", padx=10).pack()

exp = """Say Something....."""

log = PhotoImage(file="audio_recording.png")

w4 = Label(x4,justify=LEFT,padx = 10,
              text = exp,font = "Helvetica 16 bold").pack()

w5 = Label(x4,image=log).pack()

lo = PhotoImage(file="load.png")

w6 = Label(x5,justify=LEFT,padx=10,
        text = "Got it....Trying to recognise",font = "Helvetica 16 bold").pack()

w7 = Label(x5,image=lo).pack()

w9 = Label(x6, text="Recongnition Successful", font="Helvetica 16 bold", padx=10).pack()

raise_frame(x1)

root1.title("Python PocketSphinx Demo")

root1.geometry("600x400")

root1.mainloop()
