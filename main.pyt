from tkinter import *

# Function to handle button clicks
def button_click(number):
    global operator
    operator = operator + str(number)
    input_value.set(operator)

# Function to clear the display
def button_clear():
    global operator
    operator = ""
    input_value.set("")

# Function to calculate the result
def button_equal():
    global operator
    result = str(eval(operator))
    input_value.set(result)
    operator = ""

# Main window setup
main = Tk()
main.title("Calculator")

operator = ""
input_value = StringVar()

# Display screen setup
display_text = Entry(main, font=('arial', 20, 'bold'), textvariable=input_value, 
                     bd=30, insertwidth=4, bg="powder blue", justify='right')
display_text.grid(columnspan=4)

# --- Row 1: Buttons 7, 8, 9, + ---
btn7 = Button(main, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="7", command=lambda: button_click(7)).grid(row=1, column=0)
btn8 = Button(main, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="8", command=lambda: button_click(8)).grid(row=1, column=1)
btn9 = Button(main, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="9", command=lambda: button_click(9)).grid(row=1, column=2)
Addition = Button(main, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="+", command=lambda: button_click("+")).grid(row=1, column=3)

# --- Row 2: Buttons 4, 5, 6, - ---
btn4 = Button(main, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="4", command=lambda: button_click(4)).grid(row=2, column=0)
btn5 = Button(main, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="5", command=lambda: button_click(5)).grid(row=2, column=1)
btn6 = Button(main, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="6", command=lambda: button_click(6)).grid(row=2, column=2)
Subtraction = Button(main, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="-", command=lambda: button_click("-")).grid(row=2, column=3)

# --- Row 3: Buttons 1, 2, 3, * ---
btn1 = Button(main, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="1", command=lambda: button_click(1)).grid(row=3, column=0)
btn2 = Button(main, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="2", command=lambda: button_click(2)).grid(row=3, column=1)
btn3 = Button(main, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="3", command=lambda: button_click(3)).grid(row=3, column=2)
Multiply = Button(main, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="*", command=lambda: button_click("*")).grid(row=3, column=3)

# --- Row 4: Buttons 0, Clear, Equal, / ---
btn0 = Button(main, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="0", command=lambda: button_click(0)).grid(row=4, column=0)
btnClear = Button(main, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="C", command=button_clear).grid(row=4, column=1)
btnEqual = Button(main, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="=", command=button_equal).grid(row=4, column=2)
Division = Button(main, padx=16, bd=8, fg="black", font=('arial', 20, 'bold'),
              text="/", command=lambda: button_click("/")).grid(row=4, column=3)

main.mainloop()