import tkinter
root = tkinter.Tk()
root.title("CALCULATOR")
expression = "" 

def press(num):
	global expression
	expression= expression + str(num)
	lable_result.config(text=expression)

def clear() :
	global expression
	expression=""
	lable_result.config(text=expression)

def calculate():
    global expression
    result = ""
    if expression != "":
        try:
            result = eval(expression)
        except:
            result = "error"
            expression = ""
    lable_result.config(text=result)

lable_result=tkinter.Label(root, text="")
lable_result.grid(row=0 , column=0 ,columnspan=3)

one_1=tkinter.Button(root, text="1" , fg="black" ,bg="red" ,width=7,height=1 , command= lambda : press(1))
one_1.grid(row=2,column=0)

two_2=tkinter.Button(root, text="2" , fg="black" ,bg="red" ,width=7,height=1 , command= lambda : press(2))
two_2.grid(row=2,column=1)

three_3=tkinter.Button(root, text="3" , fg="black" ,bg="red" ,width=7,height=1 , command= lambda : press(3))
three_3.grid(row=2,column=2)

four_4=tkinter.Button(root, text="4" , fg="black" ,bg="red" ,width=7,height=1 , command= lambda : press(1))
four_4.grid(row=3,column=0)

five_5=tkinter.Button(root, text="5" , fg="black" ,bg="red" ,width=7,height=1 , command= lambda : press(5))
five_5.grid(row=3,column=1)

six_6=tkinter.Button(root, text="6" , fg="black" ,bg="red" ,width=7,height=1 , command= lambda : press(6))
six_6.grid(row=3,column=2)

seven_7=tkinter.Button(root, text="7" , fg="black" ,bg="red" ,width=7,height=1 , command= lambda : press(7))
seven_7.grid(row=4,column=0)

eight_8=tkinter.Button(root, text="8" , fg="black" ,bg="red" ,width=7,height=1 , command= lambda : press(8))
eight_8.grid(row=4,column=1)

nine_9=tkinter.Button(root, text="9" , fg="black" ,bg="red" ,width=7,height=1 , command= lambda : press(9))
nine_9.grid(row=4,column=2)

zero_0=tkinter.Button(root, text="0" , fg="black" ,bg="red" ,width=7,height=1 , command= lambda : press(0))
zero_0.grid(row=5,column=0)

add_=tkinter.Button(root, text="+" , fg="black" ,bg="red" ,width=7,height=1 , command= lambda : press("+"))
add_.grid(row=5,column=1)

sub_=tkinter.Button(root, text="-" , fg="black" ,bg="red" ,width=7,height=1 , command= lambda : press("-"))
sub_.grid(row=5,column=2)

multiple_=tkinter.Button(root, text="*" , fg="black" ,bg="red" ,width=7,height=1 , command= lambda : press("*"))
multiple_.grid(row=6,column=0)

divide_=tkinter.Button(root, text="/" , fg="black" ,bg="red" ,width=7,height=1 , command= lambda : press("/"))
divide_.grid(row=6,column=1)

dot_=tkinter.Button(root, text="." , fg="black" ,bg="red" ,width=7,height=1 , command= lambda : press("."))
dot_.grid(row=6,column=2)

equal_=tkinter.Button(root, text="=" , fg="black" ,bg="red" ,width=7,height=1 , command= lambda : calculate())
equal_.grid(row=7,column=0 , columnspan=3)

root.mainloop()
