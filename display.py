from flask import Flask, render_template
import tkinter as tk
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Create and configure the Tkinter root window
    root = tk.Tk()
    root.attributes("-fullscreen", True, "-topmost", True)
    root.overrideredirect(True)

    # Hide the cursor
    root.config(cursor="none")


    label = tk.Label(root)
    label.place(x=0, y=0, relwidth=1, relheight=1)

    # Add "Hello Moto" label in the center
    hello_label = tk.Label(root, text="Hello Moto", font=("Arial", 24))
    hello_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    time_interrupt = 100000  # Time screen is active in milliseconds
    root.after(time_interrupt, root.destroy)

    root.mainloop()

if __name__ == '__main__':
    # Set the display environment variable
    os.environ['DISPLAY'] = ':0'

    app.run(host='0.0.0.0', port=5000)


