import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Крестики-нолики")
        self.current = "X"
        self.board = [None]*9
        self.buttons = []
        for i in range(9):
            btn = tk.Button(root, text="", width=8, height=4, font=(None, 24), command=lambda i=i: self.move(i))
            btn.grid(row=i//3, column=i%3)
            self.buttons.append(btn)
    def move(self, i):
        if self.board[i] or self.check_winner():
            return
        self.board[i] = self.current
        self.buttons[i]["text"] = self.current
        if self.check_winner():
            messagebox.showinfo("Победа!", f"Победил {self.current}")
        elif None not in self.board:
            messagebox.showinfo("Ничья", "Ничья!")
        self.current = "O" if self.current == "X" else "X"
    def check_winner(self):
        wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
        for a,b,c in wins:
            if self.board[a] and self.board[a]==self.board[b]==self.board[c]:
                return True
        return False

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
