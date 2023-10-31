import tkinter

root = tkinter.Tk()
l1 = tkinter.Variable(value=""*20)
l2 = tkinter.Variable(value=""*20)
l3 = tkinter.Variable(value=""*20)
currentLine = 0
lines = l1, l2, l3

def main():
    texts = tkinter.Canvas(root)
    texts.grid(row=0, column=0)
    line1 = tkinter.Label(texts, textvariable=l1)
    line2 = tkinter.Label(texts, textvariable=l2)
    line3 = tkinter.Label(texts, textvariable=l3)
    line1.grid(row=0, column=0)
    line2.grid(row=1, column=0)
    line3.grid(row=2, column=0)

    buttons = tkinter.Canvas(root)
    buttons.grid(row=1, column=0)

    button1 = tkinter.Button(buttons, text="1", padx=20, pady=20, command=lambda: addText("1"))
    button2 = tkinter.Button(buttons, text="2", padx=20, pady=20, command=lambda: addText("2"))
    button3 = tkinter.Button(buttons, text="3", padx=20, pady=20, command=lambda: addText("3"))
    button4 = tkinter.Button(buttons, text="4", padx=20, pady=20, command=lambda: addText("4"))
    button5 = tkinter.Button(buttons, text="5", padx=20, pady=20, command=lambda: addText("5"))
    button6 = tkinter.Button(buttons, text="6", padx=20, pady=20, command=lambda: addText("6"))
    button7 = tkinter.Button(buttons, text="7", padx=20, pady=20, command=lambda: addText("7"))
    button8 = tkinter.Button(buttons, text="8", padx=20, pady=20, command=lambda: addText("8"))
    button9 = tkinter.Button(buttons, text="9", padx=20, pady=20, command=lambda: addText("9"))
    button0 = tkinter.Button(buttons, text="0", padx=20, pady=20, command=lambda: addText("0"))
    button1.grid(row=0, column=0)
    button2.grid(row=0, column=1)
    button3.grid(row=0, column=2)
    button4.grid(row=1, column=0)
    button5.grid(row=1, column=1)
    button6.grid(row=1, column=2)
    button7.grid(row=2, column=0)
    button8.grid(row=2, column=1)
    button9.grid(row=2, column=2)
    button0.grid(row=3, column=1)

    root.mainloop()


def addText(text):
    originalText = lines[currentLine].get()
    new = originalText + text
    lines[currentLine].set(new)


if __name__ == '__main__':
    main()
