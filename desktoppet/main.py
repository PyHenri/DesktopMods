import tkinter as tk
import time
import random
import pyautogui

window = tk.Tk()
SWidth = window.winfo_screenwidth()
SHeight = window.winfo_screenheight()
window.config(highlightbackground="black")
window.overrideredirect(True)
window.attributes("-topmost", True)
window.wm_attributes("-transparentcolor", "black")

class pet:
    def __init__(self):
        impath = "resources\\"

        self.idle = [tk.PhotoImage(file=impath + "idle.gif",format = "gif -index %i" %(i)) for i in range(5)]# idle gif
        self.idle_to_sleep = [tk.PhotoImage(file=impath + "idle_to_sleep.gif",format = "gif -index %i" %(i)) for i in range(8)]# idle to sleep gif
        self.sleep = [tk.PhotoImage(file=impath + "sleep.gif",format = "gif -index %i" %(i)) for i in range(3)]# sleep gif
        self.sleep_to_idle = [tk.PhotoImage(file=impath + "sleep_to_idle.gif",format = "gif -index %i" %(i)) for i in range(8)]# sleep to idle gif
        self.walk_positive = [tk.PhotoImage(file=impath + "walking_positive.gif",format = "gif -index %i" %(i)) for i in range(8)]# walk to left gif
        self.walk_negative = [tk.PhotoImage(file=impath + "walking_negative.gif",format = "gif -index %i" %(i)) for i in range(8)]# walk to right gif

        self.frame_index = 0
        self.img = self.idle[self.frame_index]

        self.label = tk.Label(window, bd=0, bg="black")
        self.pos = [0,SHeight-140]
        window.geometry(f"100x100+{self.pos[0]}+{self.pos[1]}")
        self.label.configure(image=self.img)
        self.label.pack()

        self.activity = random.choice(["idle", "walk_positive", "walk_negative", "sleep"])
        self.timestamp = time.time()

    def update(self):
        if time.time() > self.timestamp + 0.05:
            self.timestamp = time.time()
        
        if self.activity == "walk_positive" and self.pos[0] + 5 <= SWidth - 100:
            self.pos[0] += 5

        elif self.activity == "walk_negativ" and self.pos[0] - 5 >= 0:
            self.pos[0] -= 5
            
        if self.activity == "idle":
            self.frame_index = (self.frame_index + 1) % len(self.idle)
            self.img = self.idle[self.frame_index]

        elif self.activity == "walk_positive":
            self.frame_index = (self.frame_index + 1) % len(self.walk_positive)
            self.img = self.walk_positive[self.frame_index]

        elif self.activity == "walk_negative":
            self.frame_index = (self.frame_index + 1) % len(self.walk_negative)
            self.img = self.walk_negative[self.frame_index]

        elif self.activity == "sleep":
            self.frame_index = (self.frame_index + 1) % len(self.sleep)
            self.img = self.sleep[self.frame_index]
        
        window.geometry(f"100x100+{self.pos[0]}+{self.pos[1]}")

        self.label.configure(image=self.img)
        self.label.pack()

        # call update after 10ms
        window.after(300, self.update)

        

cat = pet()
window.after(0, cat.update)
window.mainloop()