import tkinter as tk
from timer_class import Timer

# if the monitor goes to sleep, run stop on all (or whichever is active)
window = tk.Tk()


def create_timer():
    Timer(window)


def main():
    window.title('Stopwatch')
    create_button = tk.Button(window, text="Create New Timer", font=('calibri', 40), fg="blue",
                              command=create_timer)
    create_button.pack(side='top')
    tk.mainloop()


if __name__ == "__main__":
    main()
