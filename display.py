from flask import Flask, render_template
import gevent.pywsgi
import tkinter as tk

app = Flask(__name__)

@app.route('/')
def index():
    # Create and configure the Tkinter root window
    root = tk.Tk()
    root.attributes("-fullscreen", True, "-topmost", True)
    root.overrideredirect(True)

    # Hide the cursor
    root.config(cursor="none")

    # Disable mouse events
    root.bind('<Motion>', lambda event: root.event_generate('<<Motion>>', when='tail'))
    root.bind('<Button>', lambda event: root.event_generate('<<Button>>', when='tail'))
    root.bind('<Double-Button>', lambda event: root.event_generate('<<Double-Button>>', when='tail'))
    root.bind('<Triple-Button>', lambda event: root.event_generate('<<Triple-Button>>', when='tail'))
    root.bind('<B1-Motion>', lambda event: root.event_generate('<<B1-Motion>>', when='tail'))
    root.bind('<B2-Motion>', lambda event: root.event_generate('<<B2-Motion>>', when='tail'))
    root.bind('<B3-Motion>', lambda event: root.event_generate('<<B3-Motion>>', when='tail'))
    root.bind('<Enter>', lambda event: root.event_generate('<<Enter>>', when='tail'))
    root.bind('<Leave>', lambda event: root.event_generate('<<Leave>>', when='tail'))
    root.bind('<MouseWheel>', lambda event: root.event_generate('<<MouseWheel>>', when='tail'))
    root.bind('<KeyPress>', lambda event: root.event_generate('<<KeyPress>>', when='tail'))
    root.bind('<KeyRelease>', lambda event: root.event_generate('<<KeyRelease>>', when='tail'))

    # Capture the screen


    # Create a label with the captured screen image
    label = tk.Label(root)
    label.place(x=0, y=0, relwidth=1, relheight=1)

    # Add "Hello Moto" label in the center
    hello_label = tk.Label(root, text="Hello Moto", font=("Arial", 24))
    hello_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    time_interrupt = 100000  # Time screen is active in milliseconds
    root.after(time_interrupt, root.destroy)

    root.mainloop()

if __name__ == '__main__':
    server = gevent.pywsgi.WSGIServer(('0.0.0.0', 5000), app)
    server.serve_forever()

