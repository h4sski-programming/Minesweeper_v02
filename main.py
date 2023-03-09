import tkinter as tk
eE
from settings import Settings
from mine_matrix import Mine_matrix

class Main():
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title('Minesweeper v02')
        
        self.mine_matrix = Mine_matrix()
        
        self.top_frame()
        self.mine_frame()
        self.bottom_frame()
        
        self.root.mainloop()
    
    
    def top_frame(self):
        self.top_frame = tk.Frame(self.root)
        
        title_label = tk.Label(self.top_frame, text='Minesweeper v02', font=('Arial', 22))
        title_label.pack()
        
        self.top_frame.pack(padx=10, pady=10)
        
        
    def mine_frame(self):
        self.mine_frame = tk.Frame(self.root)
        
        for i in range(Settings.size_x):
            self.mine_frame.columnconfigure(i, weight=1)
        
        for i in range(Settings.size_y):
            for j in range(Settings.size_x):
                btn = tk.Button(master=self.mine_frame, text='')
                btn.grid(row=i, column=j)
        
        self.mine_frame.pack(padx=10, pady=10)
    
    
    def bottom_frame(self):
        self.bottom_frame = tk.Frame(self.root)
        
        footer_label = tk.Label(self.bottom_frame, text='Coded by h4sski', font=('Arial', 10))
        footer_label.pack()
        
        self.bottom_frame.pack(padx=10, pady=5)
    
    
Main()