import tkinter as tk
from timer_class import Timer

# TODO: when the window gets bigger because you click Create New, make sure it stays on the screen


def main() -> None:
    window = tk.Tk()
    window.title('Stopwatch')
    create_button = tk.Button(window, text="Create New Timer", command=lambda: Timer(window))
    create_button.pack(side='top')
    tk.mainloop()


if __name__ == "__main__":
    main()
