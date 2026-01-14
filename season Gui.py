#season Gui

import tkinter as tk
from tkinter import messagebox

class SeasonApp:
    def __init__(self,root):
        self.root = root
        self.root.title("Season Finder")
        self.root.geometry("300x220")
        #month
        tk.Label(root,text = "Month(1-12):").pack(pady = 5)
        self.month_entry = tk.Entry(root)
        self.month_entry.pack()
        #Date
        tk.Label(root,text = "Date:").pack(pady = 5)
        self.date_entry = tk.Entry(root)
        self.date_entry.pack()
        #Button
        tk.Button(root,text = "Get Season",command = self.get_season).pack(pady = 10)
        #result
        self.result_label = tk.Label(root,text = "",font = ("Arial",12,"bold"))
        self.result_label.pack(pady = 5)
    def get_season(self):
        try:
            m = int(self.month_entry.get())
            d = int(self.date_entry.get())
            #check month if valid
            if m not in range(1,13):
                raise ValueError("Month must be between 1 and 12")
            max_date = self.get_max_date(m)
            # check date if valid
            if d not in range(1,max_date+1):
                raise ValueError("Invalid date for thr given month.")
            season = self.calculate_season(m,d)
            self.result_label.config(text = f"Season:{season}")
        except ValueError as e:
            messagebox.showerror("Input Error",str(e))
    def get_max_date(self, m):
        if m in (1, 3, 5, 7, 8, 10, 12):
            return 31
        elif m in (4, 6, 9, 11):
            return 30
        else:
            return 28

    def calculate_season(self, m, d):
        md = m * 100 + d

        if md >= 1216 or md <= 315:
            return "Winter"
        elif 316 <= md <= 615:
            return "Spring"
        elif 616 <= md <= 915:
            return "Summer"
        else:
            return "Fall"
def main():
    root = tk.Tk()
    app = SeasonApp(root)
    root.mainloop()
main()