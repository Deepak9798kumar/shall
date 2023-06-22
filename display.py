from flask import Flask
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

    # Capture the screen (optional, requires pyautogui)
    # screen = pyautogui.screenshot()

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
    # Use a production WSGI server instead of the development server
    from waitress import serve
    serve(app, host='0.0.0.0', port=5000)





