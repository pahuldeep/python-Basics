import tkinter as tk

def calc():
    # Get the values from the text boxes
    a = textbox1.get()
    b = textbox2.get()

    # Calculate the sum
    c = int(a) + int(b)

    # Display the result in the result text box
    textbox3.delete(0, "end")
    textbox3.insert(0, c)

# Create the main window
root = tk.Tk()
root.title("Addition Calculator")
root.geometry("800x400")

# Create labels and text boxes
label1 = tk.Label(root, text="Value:")
label1.grid(padx=10, pady=10, row=0, column=0)

textbox1 = tk.Entry(root)
textbox1.grid(row=0, column=1)

label2 = tk.Label(root, text="Value:")
label2.grid(padx=10, pady=10, row=1, column=0)

textbox2 = tk.Entry(root)
textbox2.grid(row=1, column=1)

label3 = tk.Label(root, text="Result:")
label3.grid(padx=10, pady=10, row=2, column=0)

textbox3 = tk.Entry(root)
textbox3.grid(row=2, column=1)

# Create a button to calculate the sum
button = tk.Button(root, text="Calculate Sum", command=calc)
button.grid(row=3, column=1)

# Start the mainloop
root.mainloop()
