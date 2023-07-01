from flask import Flask
from threading import Thread
import tkinter as tk

app = Flask(__name__)

def run_tkinter_app():
    root = tk.Tk()
    root.attributes("-fullscreen", True, "-topmost", True)
    root.overrideredirect(True)

    root.config(cursor="none")

    label = tk.Label(root)
    label.place(x=0, y=0, relwidth=1, relheight=1)

    hello_label = tk.Label(root, text="Hello Moto", font=("Arial", 24))
    hello_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    time_interrupt = 100000  # Time screen is active in milliseconds
    root.after(time_interrupt, root.destroy)

    root.mainloop()

@app.route('/')
def index():
    return 
if __name__ == '__main__':
    tkinter_thread = Thread(target=run_tkinter_app)
    tkinter_thread.daemon = True
    tkinter_thread.start()

    app.run(host='0.0.0.0', port=5000)











