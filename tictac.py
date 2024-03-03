import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text="", font=("Helvetica", 20), width=6, height=3,
                                                command=lambda row=i, col=j: self.make_move(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def make_move(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner(self.current_player):
                messagebox.showinfo("Winner!", f"{self.current_player} wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Draw!", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O":
                    self.ai_move()

    def ai_move(self):
        best_score = float("-inf")
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    self.board[i][j] = "O"
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = " "
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        row, col = best_move
        self.board[row][col] = "O"
        self.buttons[row][col].config(text="O")
        if self.check_winner("O"):
            messagebox.showinfo("Winner!", "AI wins!")
            self.reset_game()
        elif self.check_draw():
            messagebox.showinfo("Draw!", "It's a draw!")
            self.reset_game()
        else:
            self.current_player = "X"

    def minimax(self, board, depth, maximizing_player):
        if self.check_winner("O"):
            return 1
        elif self.check_winner("X"):
            return -1
        elif self.check_draw():
            return 0

        if maximizing_player:
            max_eval = float("-inf")
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        board[i][j] = "O"
                        eval = self.minimax(board, depth + 1, False)
                        board[i][j] = " "
                        max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float("inf")
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        board[i][j] = "X"
                        eval = self.minimax(board, depth + 1, True)
                        board[i][j] = " "
                        min_eval = min(min_eval, eval)
            return min_eval

    def check_winner(self, player):
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def check_draw(self):
        return all(cell != " " for row in self.board for cell in row)

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = " "
                self.buttons[i][j].config(text="")
        self.current_player = "X"

if __name__ == "__main__":
    game = TicTacToeGUI()
    game.root.mainloop()
