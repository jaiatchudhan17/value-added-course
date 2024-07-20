import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("400x400")
        
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        
        self.canvas = tk.Canvas(self.window, width=400, height=400)
        self.canvas.pack()
        
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        
        self.draw_board()
        
        self.window.mainloop()
    
    def draw_board(self):
        self.canvas.create_line(0, 133, 400, 133, width=4)
        self.canvas.create_line(0, 266, 400, 266, width=4)
        self.canvas.create_line(133, 0, 133, 400, width=4)
        self.canvas.create_line(266, 0, 266, 400, width=4)
    
    def draw_X(self, x, y):
        self.canvas.create_line(x - 50, y - 50, x + 50, y + 50, width=4, fill='blue')
        self.canvas.create_line(x - 50, y + 50, x + 50, y - 50, width=4, fill='blue')
    
    def draw_O(self, x, y):
        self.canvas.create_oval(x - 50, y - 50, x + 50, y + 50, width=4, outline='red')
    
    def on_canvas_click(self, event):
        row, col = event.y // 133, event.x // 133
        if self.board[row][col] == "" and not self.check_winner():
            self.board[row][col] = self.current_player
            x, y = col * 133 + 67, row * 133 + 67
            if self.current_player == "X":
                self.draw_X(x, y)
            else:
                self.draw_O(x, y)
            
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.is_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
    
    def check_winner(self):
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != "":
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False
    
    def is_draw(self):
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "":
                    return False
        return True
    
    def reset_board(self):
        self.canvas.delete("all")
        self.draw_board()
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

if __name__ == "__main__":
    TicTacToe()
