from tkinter import *
import random
import tkinter.messagebox as msg

#Initialising the score variable
global score
score = 0

#------------------------------------------------functions------------------------------------ ---------------------------------#
#choosing a word to scramble it #
def choose():
    words=['QUESADILLA','POPSICLES','CROISSANTS','CORNFLAKES','MACARONS','CONDIMENT','TURDUCKEN','SKITTLES','SOUFFLE','DUMPLING','PAJAMA','PEEKABOO','BHANGRA','NIRVANA','AVATAR','MIKAELSON','CINDERELLA','SEYCHELLES','VENICE','STETHSCOPE','ANTARTICA','VIOLIN','TECHNOLOGY','PNEUMONIA','EXTRAVAGANT','EXPERIMENT','HUMOUR','CHIHUAHUA','PANTHER','SANCTUARY','COBWEB','SQUIRREL','PHENOMENON','COLONEL','EMBELLISHED','INNOVATIVE','MORNING','ZENITH','XYLOPHONE','SYNDROME','MESOPOTAMIA','CHRISTMAS','TRANSCRIPT','BUZZING','RICKSHAW','GAZEBO','VOLKSWAGEN','EMINEM','KAYAKING','AWKWARD','FIZZED','CONTRAST']
    pick = random.choice(words)
    return pick
#------------------------------------------------------scrambling word-------------------------------------------------------- #
def scramble(word):
    #print(word)
    random_word = random.sample(word, len(word))# it makes a string into a list by breaking ech letter 
    scrambled = ''.join(random_word)
    return scrambled
#-----------------------------------------------------Validating the word----------------------------------------------------- #
def validate():
    global count, picked_word, c1, c2, c3, c4, c5, show
    if check.get().upper() == picked_word:
        global score
        picked_word = choose()
        show = scramble(picked_word)
        check.set("")
        lbl.config(text=show)
        score += 1
        scoreLabel.config(text = "Your Score: " + str(score))
    else:
        if count == 1 and check.get().upper() != picked_word:
            count += 1
            canvas.delete(c1)
        elif count == 2 and check.get().upper() != picked_word:
            count += 1
            canvas.delete(c2)
        elif count == 3 and check.get().upper() != picked_word:
            count += 1
            canvas.delete(c3)
        elif count == 4 and check.get().upper() != picked_word:
            count += 1
            canvas.delete(c4)
        elif count == 5 and check.get().upper() != picked_word:
            count += 1
            canvas.delete(c5)
            msg.showwarning("Game Over", "Please Try Again...")
            #c1=canvas.create_line()
            c1=canvas.create_line(300,180,330,230,width=3) 
            c2=canvas.create_line(300,180,270,230,width=3)
            c3=canvas.create_line(300,105,330,155,width=3)
            c4=canvas.create_line(300,105,270,155,width=3)
            c5=canvas.create_line(300,100,300,180,width=3)
            quit()
                
                
        if count == 6:
            count = 1
            check.set("")
#-------------------------------------------PROCESSING TO VALIDATE------------------------------------------------------------ #
def process(event=""):
    global correct 
    if check.get().isalpha():
        correct = TRUE
        validate()
    else:
        correct = FALSE
        msg.showerror('Error','Please make use of only alphabets')


root=Tk()   #INSTANCE OF Tk()
width, height=500,550  #HEIGHT AND WIDTH OF THE CREATED WINDOW
#// means to divide the value and don't give the decimal value and called (FLOOR DIVISION)
#s_width=((root.winfo_screenwidth() // 2)-(width // 2))   #(WIDTH OF THE MONITOR DISPLAY)//2 - (WIDTH OF THE CREATED WINDOW)//2
#s_height=((root.winfo_screenheight() // 2)-(height //2))   #(HEIGHT OF THE MONITOR DISPLAY)//2 - (HEIGHT OF THE CREATED WINDOW)//2
#root.geometry(f'{width}x{height}+{s_width}+{s_height}')   #AFTER THE MONITOR DISPLAY HEIGHT AND WIDTH THE HEIGHT AND WIDTH OF THE CREATED WINDOW SHOULD COME TO CENTER IT
root.title("Hang-Man Game")  #TITLE OF THE WINDOW
width= root.winfo_screenwidth()
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
#root.resizable(0,0)   #WINDOW CAN'T BE RESIZED

#creating the figure of hangman
canvas=Canvas(root,width=500,height=260)   #CREATING A CANVAS ON WHICH WE CAN DRAW LINES AND SHAPES
canvas.pack(pady=30)   #PACKING  THE CANVAS TO BE DISPLAYED ON WINDOW
canvas.create_line(150,260,250,260,width=3)   #BASE LINE OF THE STAND
canvas.create_line(200,260,200,40,width=3)   #LINE OF THE STAND
canvas.create_line(200,90,250,40,width=3)   #SUPPORTER OF STAND
canvas.create_line(200,40,300,40,width=3)   #TOP LINE OF STAND
canvas.create_line(300,40,300,70,width=3)   #ROPE OF THE STAND
canvas.create_oval(280,70,320,100,width=3)   #HEAD OF THE MAN
c5=canvas.create_line(300,100,300,180,width=3)   #STOMACH OF THE MAN
c4=canvas.create_line(300,105,270,155,width=3)   #LEFT HAND OF THE MAN
c3=canvas.create_line(300,105,330,155,width=3)   #RIGHT HAND OF THE MAN
c2=canvas.create_line(300,180,270,230,width=3)   #lEFT LEG OF THE MAN
c1=canvas.create_line(300,180,330,230,width=3)   #RIGHT LEG OF THE MAN

#-------------------------variables-----------#
count = 1
picked_word = choose()
check = StringVar()
show = scramble(picked_word)
correct = NONE

#Creating the score keeper label
scoreLabel = Label(root, text = "Your Score: " + str(score), bg = "powder blue")
scoreLabel.place(x=100, y=100)



#-----------------------------------------------------------lAYOUT-------------------------------------------------------------#
lbl=Label(root,text= show,font=("Candara",25,"bold"))   #MAKING THE LABEL WHICH WILL SHOW YOU THE JUMBLE WORDS
lbl.pack()   #PACKING THE LABEL

txt=Entry(root,textvariable=check,font=("Candara",25,"bold"),justify=CENTER,relief=GROOVE,bd=2)   #IN THIS USER WILL ANSWER
txt.pack(pady=20)   #PACKING THE ENTRY WIDGET

btn=Button(root,text="SUBMIT",font=("Candara",25,"bold"),relief=GROOVE,bg="#E3FFDC",command=process)   #CLICK TO CHECK WHETHER THE ANSWER IS RIGHT OR WRONG
btn.pack(pady=20)   #PACKING THE BUTTON
root.bind('<Return>',process)

Button(root,text='Quit',command=root.destroy).pack()
root.mainloop()
 #THIS CREATES INFINITE LOOP UNTIL THE USER EXITS THE PROGRAM