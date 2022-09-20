#Importing all pertinent modules.
import tkinter 
from PIL import ImageTk,Image 
import tkinter.messagebox
import os


number = 0


def change_image(number):
    #Updating the image
    global lab
    lab.grid_forget()
    lab = tkinter.Label(image=im_list[number+1])
    lab.place(relx=0.5, rely=0.39, anchor="center")
    
    if number == 5:    #WHEN THE NUMBER OF TURNS ARE EXHAUSTED
        tkinter.messagebox.showinfo('Game Over.', message="The man was hung. Thank you for playing!")
        root.destroy() 
    number += 1
    return number
    

def check(button, no):
    global e2
    global number
    global lab
    
    text = button["text"]

    no = list(uppercase).count(text)
    print(no)

    if uppercase=='':
        tkinter.messagebox.showinfo(message="Make sure Player 1 enters a word first.")

    elif (no == 0): #Changes the image label when a mistake has been made
        number = change_image(number)

    else: #Updating list hangman and giving it to label (if the letter is in the input)
        for i in range(len(uppercase)):
            if uppercase[i] == text:
                hangman[i] = text
                
    #Deleting previous hangman label, printing the updated one 
    e2.grid_forget()
    e2 = tkinter.Label(root,text=' '.join(hangman).upper(), width=40, height=2, relief='sunken',borderwidth=5, font=("Rosewood Std Fill",15,"bold"))
    e2.place(relx=.09,rely=.09)

    button.destroy()

    if '_' not in hangman:
        tkinter.messagebox.showinfo(message="Awesome! You guessed the word!")
        root.destroy()
     
def obtain_destroy():
    global hangman
    global uppercase
    global e2
    #Obtaining the input from Player 1
    lo = e1.get()
    if len(lo) == 0:
        tkinter.messagebox.showinfo(message="You must enter something!")
        e1.delete(0,tkinter.END)
        return 0
    
    if lo.isalpha()==True or ' ' in lo:

            uppercase+=lo.upper()
            e2.destroy()
            e1.destroy()
            b1.destroy()
            hangman = ['_' if i!=' ' else ' ' for i in uppercase] 
            e2 = tkinter.Label(root,text=' '.join(hangman).upper(), width=40, height=2, relief='sunken',borderwidth=5, font=("Rosewood Std Fill",15,"bold"))
            e2.place(relx=.09,rely=.09)
    else:
        tkinter.messagebox.showinfo(message="Please only enter letters of the alphabet, please.")
        e1.delete(0,tkinter.END)
            

    print(lo)
    
#Creating the window for player 2
root = tkinter.Tk()
root.title("Hangman")
root.geometry("600x590")
root.configure(bg='#CBB3E4')
#Defining the label that displays completion of the word.
e2 = tkinter.Label(root) 

#Creating path such that any user may access said file
userpath = os.environ['USERPROFILE']

#Creating variables that point to the displayed images
im=ImageTk.PhotoImage(Image.open(f"{userpath}\Downloads\HangmanProject\WhatsApp Image 2022-01-12 at 7.24.31 PM.jpeg"))
im2=ImageTk.PhotoImage(Image.open(f'{userpath}\Downloads\HangmanProject\WhatsApp Image 2022-01-12 at 7.24.31 PM (1).jpeg'))
im3=ImageTk.PhotoImage(Image.open(f"{userpath}\Downloads\HangmanProject\WhatsApp Image 2022-01-12 at 7.24.31 PM (2).jpeg"))
im4=ImageTk.PhotoImage(Image.open(f'{userpath}\Downloads\HangmanProject\WhatsApp Image 2022-01-12 at 7.24.31 PM (3).jpeg'))
im5=ImageTk.PhotoImage(Image.open(f'{userpath}\Downloads\HangmanProject\WhatsApp Image 2022-01-12 at 7.24.31 PM (4).jpeg'))
im6=ImageTk.PhotoImage(Image.open(f'{userpath}\Downloads\HangmanProject\WhatsApp Image 2022-01-12 at 7.24.31 PM (5).jpeg'))
im7=ImageTk.PhotoImage(Image.open(f'{userpath}\Downloads\HangmanProject\WhatsApp Image 2022-01-12 at 7.24.31 PM (6).jpeg'))
#Creating a list of all the images to cycle through.
im_list = [im, im2, im3, im4, im5, im6, im7]
#Creating the frame of the images
lab = tkinter.Label(image=im_list[0], anchor=tkinter.CENTER)
lab.place(relx=.5, rely=.39, anchor="center")

#Defining an empty string to which the input string is appended.
uppercase = ''
#x allows Player 1 to input the word to be guessed.
x = tkinter.StringVar()
#Defining and placing the entry field as well as the submit button for Player 1.
e1 = tkinter.Entry(root,borderwidth=4,show='*',relief='sunken')
e1.place(relx=.36,rely=.09)
b1 = tkinter.Button(root,text="Submit", command=obtain_destroy)
b1.place(relx=.455, rely=.4)

#DEFINING OF VIRTUAL KEYBOARD OBJECTS. 

Q = tkinter.Button(root, width=2, height= 1, borderwidth=3, relief='raised', font=("Helvetica", "20"), text='Q', bg="#FCE8EA", command=lambda: check(Q, 0))
Q.place(relx=0.05, rely=0.6)

W = tkinter.Button(root, width=2, height= 1, relief='raised', font=("Helvetica", "20"), text='W', bg="#FCE8EA", borderwidth=3, command=lambda: check(W, 0))
W.place(relx=0.14, rely=0.6)

E = tkinter.Button(root, relief='raised', font=("Helvetica", "20"), text='E', bg="#FCE8EA", borderwidth=3, command=lambda: check(E, 0))
E.place(relx=0.23, rely=0.6)

R = tkinter.Button(root, relief='raised', font=("Helvetica", "20"), text='R', bg="#FCE8EA", borderwidth=3, command=lambda: check(R, 0))
R.place(relx=0.32, rely=0.6)

T = tkinter.Button(root, relief='raised', font=("Helvetica", "20"), text='T', bg="#FCE8EA", borderwidth=3, command=lambda: check(T, 0))
T.place(relx=0.41, rely=0.6) 

Y = tkinter.Button(root, relief='raised', font=("Helvetica", "20"), text='Y', bg="#FCE8EA", borderwidth=3, command=lambda: check(Y, 0))
Y.place(relx=0.5, rely=0.6) 

U = tkinter.Button(root, relief='raised', font=("Helvetica", "20"), text='U', bg="#FCE8EA", borderwidth=3, command=lambda: check(U, 0))
U.place(relx=0.59, rely=0.6) 

I = tkinter.Button(root, width=2, height= 1, relief='raised', font=("Helvetica", "20"), text='I', bg="#FCE8EA", borderwidth=3, command=lambda: check(I, 0))
I.place(relx=0.68, rely=0.6)

O = tkinter.Button(root, relief='raised',width=2, height= 1, font=("Helvetica", "20"), text='O', bg="#FCE8EA", borderwidth=3, command=lambda: check(O, 0))
O.place(relx=0.77, rely=0.6) 

P = tkinter.Button(root, relief='raised', width=2, height= 1, font=("Helvetica", "20"), text='P', bg="#FCE8EA", borderwidth=3, command=lambda: check(P, 0))
P.place(relx=0.86, rely=0.6) 

A = tkinter.Button(root, width=2, height= 1, relief='raised', font=("Helvetica", "20"), text='A', bg="#CFFED4", borderwidth=3, command=lambda: check(A, 0))
A.place(relx=0.09, rely=0.71) 

S = tkinter.Button(root, width=2, height= 1, relief='raised', font=("Helvetica", "20"), text='S', bg="#CFFED4", borderwidth=3, command=lambda: check(S, 0)) 
S.place(relx=0.18, rely=0.71) 

D = tkinter.Button(root, width=2, height= 1, relief='raised', font=("Helvetica", "20"), text='D', bg="#CFFED4", borderwidth=3, command=lambda: check(D, 0))
D.place(relx=0.27, rely=0.71)

F = tkinter.Button(root, width=2, height= 1, relief='raised', font=("Helvetica", "20"), text='F', bg="#CFFED4", borderwidth=3, command=lambda: check(F, 0))
F.place(relx=0.36, rely=0.71)

G = tkinter.Button(root, relief='raised', font=("Helvetica", "20"), text='G', bg="#CFFED4", borderwidth=3, command=lambda: check(G, 0))
G.place(relx=0.45, rely=0.71) 

H = tkinter.Button(root, width=2, height= 1, relief='raised', font=("Helvetica", "20"), text='H', bg="#CFFED4", borderwidth=3, command=lambda: check(H, 0))
H.place(relx=0.54, rely=0.71)

J = tkinter.Button(root, width=2, height= 1, relief='raised', font=("Helvetica", "20"), text='J', bg="#CFFED4", borderwidth=3, command=lambda: check(J, 0))
J.place(relx=0.63, rely=0.71)

K = tkinter.Button(root, width=2, height= 1, relief='raised', font=("Helvetica", "20"), text='K', bg="#CFFED4", borderwidth=3, command=lambda: check(K, 0))
K.place(relx=0.72, rely=0.71)

L = tkinter.Button(root, width=2, height= 1, relief='raised', font=("Helvetica", "20"), text='L', bg="#CFFED4", borderwidth=3, command=lambda: check(L, 0))
L.place(relx=0.81, rely=0.71)

Z = tkinter.Button(root, width=2, height= 1, relief='raised', font=("Helvetica", "20"), text='Z', bg="#CAF3F9", borderwidth=3, command=lambda: check(Z, 0))
Z.place(relx=0.18, rely=0.82)

X = tkinter.Button(root, width=2, height= 1, relief='raised', font=("Helvetica", "20"), text='X', bg="#CAF3F9", borderwidth=3, command=lambda: check(X, 0))
X.place(relx=0.27, rely=0.82)

C = tkinter.Button(root, width=2, height= 1, relief='raised', font=("Helvetica", "20"), text='C', bg="#CAF3F9", borderwidth=3, command=lambda: check(C, 0))
C.place(relx=0.36, rely=0.82)

V = tkinter.Button(root, width=2, height= 1, relief='raised', font=("Helvetica", "20"), text='V', bg="#CAF3F9", borderwidth=3, command=lambda: check(V, 0))
V.place(relx=0.45, rely=0.82)

B = tkinter.Button(root, width=2, height= 1, relief='raised', font=("Helvetica", "20"), text='B', bg="#CAF3F9", borderwidth=3, command=lambda: check(B, 0))
B.place(relx=0.54, rely=0.82)

N = tkinter.Button(root, width=2, height= 1, relief='raised', font=("Helvetica", "20"), text='N', bg="#CAF3F9", borderwidth=3, command=lambda: check(N, 0))
N.place(relx=0.63, rely=0.82)

M = tkinter.Button(root, width=2, height= 1, relief='raised', font=("Helvetica", "20"), text='M', bg="#CAF3F9", borderwidth=3, command=lambda: check(M, 0))
M.place(relx=0.72, rely=0.82)



root.mainloop() 