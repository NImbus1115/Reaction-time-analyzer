import tkinter as tk

root = tk.Tk()
root.attributes("-fullscreen", True)  # full screen
root.configure(bg="black")

label = tk.Label(
    root,
    text="Press SPACE to Start",
    font=("Arial", 40),
    fg="white",
    bg="black"
)

label.pack(expand=True)

def exit_app(event):
    root.destroy()

root.bind("<Escape>", exit_app)  # press ESC to exit

root.mainloop()