import tkinter
from fractions import Fraction

r=tkinter.Tk()
img =tkinter.PhotoImage(file='calculator.ico')
r.iconphoto(False, img)                         # to place the icon image
r.title("CALCULATOR")

r.geometry("260x350")
r.config(bg="#3b3b3b")                          # to set the background window colour

exp=""                                          # to hold the expression
f=True                                          # to check the status of result either fraction or decimal, use in the key S<>D
calculated=False                                # to control some keys or error

                                   # function to calculate #
                                   #=======================#

def calculate():
    global calculated
    global exp
    
    if screenvar.get()=="":                                     # if screen is empty (=) key will not work, so simply return
        return
    
    try:                                                        # using exception handling to handle error in case of wrong expression input
        tmpexp=eval(exp)
        exp=str(Fraction(tmpexp).limit_denominator())           # limit the denominator.Result will initially show in fraction form 
        #print(exp)
        screenvar.set(exp)                                      # print the exp result on screen if no error
        calculated=True
    except:
        screenvar.set("ERROR PRESS C")                          # show error message on screen if wrong input

        
                               # function to convert fraction to decimal and decimal to fraction #
                               #=================================================================#
def frac():
    global calculated
    global exp
    global f

    if calculated==1:                # if 1 means (=) key has presses and result is on screen.(S<>D) key can work now to convert frac to dec and dec to frac
        tmpexp=Fraction(exp)
        if f==0:                     # exp is in decimal form, change it to fraction form
            #print(exp)
            exp=str(tmpexp)
            screenvar.set(exp)
            f=1                      # change it to 1 so the next time change it to decimal form could work
            
        else:                        # exp is in fraction form, change it to decimal form
            #print(exp)
            screenvar.set(str(tmpexp.numerator/tmpexp.denominator))
            f=0                      # change it to 1 so the next time change it to fraction form could work

            
                                   # function to clear the screen #
                                   #==============================#
def clear():
    global exp
    global f
    global calculated
                                    # clear the screen and all the global variables
    screenvar.set("")              
    exp=""
    calculated=0
    f=1

                                      # function to add numbers and operator in expression #
                                      #====================================================#
def numoperator(t):
    global exp
    global f
    global calculated
    if calculated==1:                                # the previous answer is on screen,
        screenvar.set("ANS")                         # show previous result in "ANS" if further calculation is continue without clear the screen
        
        if t.isdigit():                              # if previous result is 2 we cannot simply add the number like 1 in the expression otherwise it will become 21, First add the operator for further clculation
            exp+=".."                                # in case of direct adding the number without operator, we have to make the expression wrong by adding .. points
        calculated=0                                 # if it is operator after the "ANS" then ok, now we can add the num and operators in expression
        
    screenvar.set(screenvar.get()+t)                 # show result on screen like:   ANS+5
    
    if t=="÷":                                       # add / sign in exp
        exp+="/"
        return
    if t=="×":                                       # add * sign in exp
        exp+="*"
        return
    exp+=t                                           # add any number and operator in expression except / and * , we have already defined them

                                          # event function for button press #
                                          #=================================#
def click(event):
    global exp
    global f

    t=event.widget.cget("text")
    if screenvar.get()!="ERROR PRESS C":                     # if error pop up no button can be pressed except C clear button
        
        if t=="C":                                           # to clear the screen
            clear()                                            
        
        elif t=="%":                                         # to add % sign in expression
            screenvar.set(screenvar.get()+t)
            exp+="/100"
        
        elif t=="S<>D":                                      # to convert fraction to decimal and decimal to fraction
            frac()
        
        elif t=="=":                                         # to calculate 
            calculate()
    
        else:                                                # to add numbers and operators
            numoperator(t)

    else:                                                    # this will run if error pop up
        if t == "C":                                         # key that should be press after error pop up on screen is the clear screen C.Otherwise message will stay on screen
            clear()

#_________________________________________________________________________________________________________________________________________________________#
            
                                        # frame f1 for logo stringvar and entry widget #      
f1=tkinter.Frame(r,bg="black")

img =tkinter.PhotoImage(file='images.png')                   # take the image by PhotoImage
img2=img.subsample(5)                                        # minimize the image size
heading=tkinter.Label(f1,image=img2,bg="black")              # paste the image with the help of label 
heading.pack(fill="x")

screenvar=tkinter.StringVar()                                # create the stringvar for screen input
screenentry=tkinter.Entry(f1,width=30,text=screenvar,fg="black",bg="#e5f2e5",font=("Eurostile",15,"bold"),justify="right",state="readonly")  # create the entry widget as screen and attach the screenvar with it
screenentry.pack(fill="x")

l=tkinter.Label(f1,bg="black")                               # one label for simple desing in the botton of screen to cover the screen with black colour
l.pack()
f1.pack(fill="x")                                            # pack the frame f1



                                     # frame f2 for buttons #
f2=tkinter.Frame(r,bg="#3b3b3b")
button=tkinter.Button(f2,text="OFF",height=1,width=4,fg="white",bg="black",font=("Arial",10,"bold"),command=quit)   # OFF button close the program
button.grid(row=0,column=0,padx=8,pady=8)
button=tkinter.Button(f2,text="S<>D",height=1,width=4,fg="white",bg="black",font=("Arial",10,"bold"))               # S<>D to convert fraction to decimal and decimal to fraction
button.grid(row=0,column=1,padx=8,pady=8)
button.bind("<Button-1>",click)
button=tkinter.Button(f2,text="%",height=1,width=4,fg="white",bg="black",font=("Arial",10,"bold"))                  # for precentage sign             
button.grid(row=0,column=2,padx=8,pady=8)
button.bind("<Button-1>",click)
button=tkinter.Button(f2,text="÷",height=1,width=4,fg="white",bg="black",font=("Arial",10,"bold"))                  # for devide sign
button.grid(row=0,column=3,padx=8,pady=8)
button.bind("<Button-1>",click)

button=tkinter.Button(f2,text="7",height=1,width=4,fg="white",bg="#D3D3D3",font=("Arial",10,"bold"))                # for 7            
button.grid(row=1,column=0,padx=8,pady=8)
button.bind("<Button-1>",click)
button=tkinter.Button(f2,text="8",height=1,width=4,fg="white",bg="#D3D3D3",font=("Arial",10,"bold"))                # for 8
button.grid(row=1,column=1,padx=8,pady=8)
button.bind("<Button-1>",click)
button=tkinter.Button(f2,text="9",height=1,width=4,fg="white",bg="#D3D3D3",font=("Arial",10,"bold"))                # for 9
button.grid(row=1,column=2,padx=8,pady=8)
button.bind("<Button-1>",click)
button=tkinter.Button(f2,text="×",height=1,width=4,fg="white",bg="black",font=("Arial",10,"bold"))                 # for multiply sign
button.grid(row=1,column=3,padx=8,pady=8)
button.bind("<Button-1>",click)

button=tkinter.Button(f2,text="4",height=1,width=4,fg="white",bg="#D3D3D3",font=("Arial",10,"bold"))                # for 4
button.grid(row=2,column=0,padx=8,pady=8)
button.bind("<Button-1>",click)
button=tkinter.Button(f2,text="5",height=1,width=4,fg="white",bg="#D3D3D3",font=("Arial",10,"bold"))                # for 5
button.grid(row=2,column=1,padx=8,pady=8)
button.bind("<Button-1>",click)
button=tkinter.Button(f2,text="6",height=1,width=4,fg="white",bg="#D3D3D3",font=("Arial",10,"bold"))                # for 6
button.grid(row=2,column=2,padx=8,pady=8)
button.bind("<Button-1>",click)
button=tkinter.Button(f2,text="-",height=1,width=4,fg="white",bg="black",font=("Arial",10,"bold"))                  # for minus sign
button.grid(row=2,column=3,padx=8,pady=8)
button.bind("<Button-1>",click)
button=tkinter.Button(f2,text="1",height=1,width=4,fg="white",bg="#D3D3D3",font=("Arial",10,"bold"))                # for 1
button.grid(row=3,column=0,padx=8,pady=8)
button.bind("<Button-1>",click)
button=tkinter.Button(f2,text="2",height=1,width=4,fg="white",bg="#D3D3D3",font=("Arial",10,"bold"))                # for 2
button.grid(row=3,column=1,padx=8,pady=8)
button.bind("<Button-1>",click)
button=tkinter.Button(f2,text="3",height=1,width=4,fg="white",bg="#D3D3D3",font=("Arial",10,"bold"))                # for 3
button.grid(row=3,column=2,padx=8,pady=8)
button.bind("<Button-1>",click)
button=tkinter.Button(f2,text="+",height=1,width=4,fg="white",bg="black",font=("Arial",10,"bold"))                  # for plus sign
button.grid(row=3,column=3,padx=8,pady=8)
button.bind("<Button-1>",click)

button=tkinter.Button(f2,text="C",height=1,width=4,fg="white",bg="orange",font=("Arial",10,"bold"))                 # for clear
button.grid(row=4,column=0,padx=8,pady=8)
button.bind("<Button-1>",click)
button=tkinter.Button(f2,text="0",height=1,width=4,fg="white",bg="#D3D3D3",font=("Arial",10,"bold"))                # for 0
button.grid(row=4,column=1,padx=8,pady=8)
button.bind("<Button-1>",click)
button=tkinter.Button(f2,text=".",height=1,width=4,fg="white",bg="#D3D3D3",font=("Arial",10,"bold"))                # for point/dot
button.grid(row=4,column=2,padx=8,pady=8)
button.bind("<Button-1>",click)
button=tkinter.Button(f2,text="=",height=1,width=4,fg="white",bg="black",font=("Arial",10,"bold"))                  # for isequal to = sign
button.grid(row=4,column=3,padx=8,pady=8)
button.bind("<Button-1>",click)
f2.pack(pady=15)




r.mainloop()

