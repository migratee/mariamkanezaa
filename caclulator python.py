import tkinter as tk
import math

def click(button):
    global expression
    if button == "AC":
        expression = ""
    elif button == "=":
        try:
            expression = expression.replace("x","*")
            expression = str(eval(expression))
        except:
            expression = "Error" 
    elif button == "√":
        try:    
            expression = str(math.sqrt(float(expression)))
        except:
            expression = "Error"

    else:                 
        expression += str(button)
    label.config(text=expression)
root = tk.Tk()
root.title("Python Calculator")

expression = ""
label = tk.Label(root, text="0", anchor="e", font=("Arial", 20), bg="black", fg="white", width=20)
label.grid(row=0, column=0, columnspan=4)
           
buttons = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]


for r, row in enumerate(buttons):
    for c, btn in enumerate(row):
        action = lambda x=btn: click(x)
        if btn in ["AC", "+/-", "%"]:
            color = "white"
        elif btn in ["÷", "×", "-", "+", "="]:
            color = "yellow"
        else:
            color = "grey"
        tk.Button(root, text=btn, width=5, height=2, bg=color, fg="black", relief="flat", command=action).grid(row=r+1, column=c)

root.mainloop()