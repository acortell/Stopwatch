import tkinter as tk
from datetime import datetime, timedelta
from pop_up import pop_up


class Timer:
    def __init__(self, parent):
        self.parent = parent
        self.active = False
        self.elapsed = timedelta(0)
        self.time_start = datetime.now()
        self.frame = tk.Frame(parent)
        self.after_id = self.parent.after(1, None)
        self.frame.pack(side='top')
        self.entry = tk.Entry(self.frame, width=10)
        self.entry.pack(side='left')
        self.label = tk.Label(self.frame, text="0:00:00")
        self.label.pack(side='left')
        self.delete_button = tk.Button(self.frame, text="Delete", command=self.delete)
        self.delete_button.pack(side='right')
        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset)
        self.reset_button.pack(side='right')
        self.stop_button = tk.Button(self.frame, text="Stop", command=self.stop)
        self.stop_button.pack(side='right')
        self.start_button = tk.Button(self.frame, text="Start", command=self.start)
        self.start_button.pack(side='right')

    def delete(self):
        if self.active:
            self.parent.after_cancel(self.after_id)
        self.frame.destroy()

    def stop(self):
        if self.active:
            self.active = False
            self.parent.after_cancel(self.after_id)
            self.elapsed = datetime.now() - self.time_start + self.elapsed
            self.label.config(text=str(self.elapsed).split('.')[0])

    def reset(self):
        self.active = False
        self.parent.after_cancel(self.after_id)
        self.elapsed = timedelta(0)
        self.label.config(text="0:00:00")

    def start(self):
        if not self.active:
            self.time_start = datetime.now()
            self.active = True
            self.refresh_label()

    def refresh_label(self):
        now = datetime.now()
        if self.active:
            if now - self.time_start > timedelta(seconds=2):
                self.stop()
                pop_up(self.entry.get())
            else:
                self.elapsed = now - self.time_start + self.elapsed
                self.time_start = now
                self.label.config(text=str(self.elapsed).split('.')[0])
                self.after_id = self.parent.after(1000, self.refresh_label)
