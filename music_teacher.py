from tkinter import *
import pygame
import learn

pygame.init()
root = Tk()
root.title("Music Tutorial")
root.geometry('1000x1000')
root.configure(background='misty rose')

skltn = Frame(root, bg='LightSkyBlue4', width=800, height=800, bd=5, relief=FLAT)
skltn.place(relx=0.1, rely=0.1)

obj1 = Frame(skltn, bg='LightSkyBlue', width=600, bd=5, relief=FLAT)
obj1.grid(row=0, column=0)

obj3 = Frame(skltn, height=20, bg='Beige', bd=15)
obj3.grid(row=1, column=0)

obj2a = Frame(skltn, height=40, bg='White', bd=0)
obj2a.place(relx=0.28, rely=0.41)

obj2b = Frame(skltn, height=40, bg='White', bd=0)
obj2b.place(relx=0.5, rely=0.41)

obj4 = Frame(skltn, height=20, bd=0)
obj4.grid(row=3, column=0)

s = StringVar()
s.set("Question")

t = StringVar()
t.set("Your Answer will Display here!!")

u = StringVar()
u.set("MUSIC TUTORIAL")


def value_Cs():
	if s.get() == 'c sharp':
		t.set('c sharp')
	else:
		t.set('d flat')

def value_Ds():
	if s.get() == 'd sharp':
		t.set('d sharp')
	else:
		t.set('e flat')

def value_Fs():
	if s.get() == 'f sharp':
		t.set('f sharp')
	else:
		t.set('g flat')

def value_Gs():
	if s.get() == 'g sharp':
		t.set('g sharp')
	else:
		t.set('a flat')

def value_As():
	if s.get() == 'a sharp':
		t.set('a sharp')
	else:
		t.set('b flat')

def value_C():
    t.set('c')

def value_D():
    t.set('d')

def value_E():
    t.set('e')

def value_F():
    t.set('f')

def value_G():
    t.set('g')

def value_A():
    t.set('a')

def value_B():
    t.set('b')

panel = Label(obj1, height=3, width=70, text="M  U  S  I  C   P  L  A  Y  E  R", bd=0, bg='White', fg='Blue2', relief=RIDGE, justify=CENTER).grid(row=0)
prompt_display = Entry(obj1, textvariable=u, width=70, bd=0, bg='Yellow', fg='Maroon1', justify='center',relief=FLAT).grid(row=1, column=0)
ques_display = Entry(obj1, textvariable=s, width=35, bd=1, bg='White', fg='Black', justify='center',relief=FLAT).grid(row=2, column=0)
ans_display = Entry(obj1, textvariable=t, width=35, bd=1, bg='White', fg='Black', justify='center',relief=FLAT).grid(row=3, column=0)

Cs = Button(obj2a, height=5, width=2, bg='Black', fg='White', command=value_Cs).grid(row=0, column=0)
Ds = Button(obj2a, height=5, width=2, bg='Black', fg='White', command=value_Ds).grid(row=0, column=1)

Fs = Button(obj2b, height=5, width=2, bg='Black', fg='White', command=value_Fs).grid(row=0, column=3)
Gs = Button(obj2b, height=5, width=2, bg='Black', fg='White', command=value_Gs).grid(row=0, column=4)
As = Button(obj2b, height=5, width=2, bg='Black', fg='White', command=value_As).grid(row=0, column=5)

C = Button(obj3, height=9, width=2, bg='White', command=value_C).grid(row=1, column=0)
D = Button(obj3, height=9, width=2, bg='White', command=value_D).grid(row=1, column=1)
E = Button(obj3, height=9, width=2, bg="White", command=value_E).grid(row=1, column=2)
F = Button(obj3, height=9, width=2, bg='White', command=value_F).grid(row=1, column=3)
G = Button(obj3, height=9, width=2, bg='White', command=value_G).grid(row=1, column=4)
A = Button(obj3, height=9, width=2, bg='White', command=value_A).grid(row=1, column=5)
B = Button(obj3, height=9, width=2, bg='White', command=value_B).grid(row=1, column=6)


def start():
	note = learn.runactivity()
	u.set("Play following note")
	s.set(note)
	t.set("")

def submit():
	if s.get() == t.get():
		answer = 1
		t.set("Correct :)")
	else:
		answer = -1
		t.set("Wrong :(")
	reward = learn.update_learning(answer)
	learn.update_bandit_wts(reward)

start = Button(obj4, text='START', bg='Coral', fg='Black', command=start).grid(row=1, column=0)

submit = Button(obj4, text='SUBMIT', bg='Coral', fg='Black', command=submit).grid(row=1, column=3)

