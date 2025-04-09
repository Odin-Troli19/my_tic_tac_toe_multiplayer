import tkinter as tk
from tkinter import messagebox
import random

class TicTacToeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("400x500")
        self.root.minsize(300, 400)
        self.root.resizable(True, True)

        # Game variables
        self.player1 = {"name": "", "color": "", "symbol": "X", "score": 0}
        self.player2 = {"name": "", "color": "", "symbol": "O", "score": 0}
        self.current_player = 1
        self.board = [None] * 9
        self.game_over = False
        self.playing_vs_computer = False

        # Main frame
        self.main_frame = tk.Frame(root, padx=20, pady=20)
        self.main_frame.pack(fill="both", expand=True)

        # Setup frame
        self.setup_frame = tk.Frame(self.main_frame)
        self.setup_frame.pack(fill="both", expand=True)

        # Game frame (hidden at first)
        self.game_frame = tk.Frame(self.main_frame)

        # UI
        self.create_setup_ui()

    def create_setup_ui(self):
        tk.Label(self.setup_frame, text="Player 1 Setup", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))

        tk.Label(self.setup_frame, text="Name:").grid(row=1, column=0, sticky="w", pady=5)
        self.player1_name_entry = tk.Entry(self.setup_frame, width=20)
        self.player1_name_entry.grid(row=1, column=1, sticky="w", pady=5)

        tk.Label(self.setup_frame, text="Color:").grid(row=2, column=0, sticky="w", pady=5)
        self.player1_color_frame = tk.Frame(self.setup_frame)
        self.player1_color_frame.grid(row=2, column=1, sticky="w", pady=5)
        self.player1_red_btn = tk.Button(self.player1_color_frame, text="Red", width=6, bg="lightgray",
                                          command=lambda: self.select_color(1, "red"))
        self.player1_red_btn.pack(side="left", padx=(0, 5))
        self.player1_blue_btn = tk.Button(self.player1_color_frame, text="Blue", width=6, bg="lightgray",
                                           command=lambda: self.select_color(1, "blue"))
        self.player1_blue_btn.pack(side="left")

        # Opponent choice
        self.vs_computer = tk.IntVar()
        self.vs_computer_check = tk.Checkbutton(self.setup_frame, text="Play vs Computer", variable=self.vs_computer, command=self.toggle_computer)
        self.vs_computer_check.grid(row=3, column=0, columnspan=2, pady=(10, 5))

        # Player 2 setup
        self.player2_label = tk.Label(self.setup_frame, text="Player 2 Setup", font=("Arial", 12, "bold"))
        self.player2_label.grid(row=4, column=0, columnspan=2, sticky="w", pady=(10, 10))

        tk.Label(self.setup_frame, text="Name:").grid(row=5, column=0, sticky="w", pady=5)
        self.player2_name_entry = tk.Entry(self.setup_frame, width=20)
        self.player2_name_entry.grid(row=5, column=1, sticky="w", pady=5)

        tk.Label(self.setup_frame, text="Color:").grid(row=6, column=0, sticky="w", pady=5)
        self.player2_color_frame = tk.Frame(self.setup_frame)
        self.player2_color_frame.grid(row=6, column=1, sticky="w", pady=5)

        self.player2_red_btn = tk.Button(self.player2_color_frame, text="Red", width=6, bg="lightgray",
                                          command=lambda: self.select_color(2, "red"))
        self.player2_red_btn.pack(side="left", padx=(0, 5))
        self.player2_blue_btn = tk.Button(self.player2_color_frame, text="Blue", width=6, bg="lightgray",
                                           command=lambda: self.select_color(2, "blue"))
        self.player2_blue_btn.pack(side="left")

        self.start_button = tk.Button(self.setup_frame, text="Start Game", command=self.start_game, state="disabled")
        self.start_button.grid(row=7, column=0, columnspan=2, sticky="ew", pady=(20, 0))

        # Bind entries
        self.player1_name_entry.bind("<KeyRelease>", lambda e: self.check_start_button())
        self.player2_name_entry.bind("<KeyRelease>", lambda e: self.check_start_button())

    def toggle_computer(self):
        if self.vs_computer.get():
            self.playing_vs_computer = True
            self.player2_name_entry.delete(0, tk.END)
            self.player2_name_entry.insert(0, "Computer")
            self.player2_name_entry.config(state="disabled")
        else:
            self.playing_vs_computer = False
            self.player2_name_entry.config(state="normal")
            self.player2_name_entry.delete(0, tk.END)
        self.check_start_button()

    def select_color(self, player, color):
        buttons = {
            1: (self.player1_red_btn, self.player1_blue_btn),
            2: (self.player2_red_btn, self.player2_blue_btn)
        }
        if player == 1:
            self.player1["color"] = color
        else:
            self.player2["color"] = color

        red_btn, blue_btn = buttons[player]
        red_btn.config(bg="red" if color == "red" else "lightgray", fg="white" if color == "red" else "black")
        blue_btn.config(bg="blue" if color == "blue" else "lightgray", fg="white" if color == "blue" else "black")

        if color == "red":
            other_btn = buttons[2 if player == 1 else 1][0]
            other_btn.config(state="disabled")
            buttons[2 if player == 1 else 1][1].config(state="normal")
        else:
            other_btn = buttons[2 if player == 1 else 1][1]
            other_btn.config(state="disabled")
            buttons[2 if player == 1 else 1][0].config(state="normal")

        self.check_start_button()

    def check_start_button(self):
        if (self.player1_name_entry.get() and
            self.player2_name_entry.get() and
            self.player1["color"] and self.player2["color"]):
            self.start_button.config(state="normal")
        else:
            self.start_button.config(state="disabled")

    def start_game(self):
        name1 = self.player1_name_entry.get()
        name2 = self.player2_name_entry.get()

        if name1 == name2:
            messagebox.showwarning("Invalid Setup", "Players must have different names.")
            return

        self.player1["name"] = name1
        self.player2["name"] = name2

        self.setup_frame.pack_forget()
        self.create_game_ui()
        self.game_frame.pack(fill="both", expand=True)

        # Trigger computer if it starts
        if self.current_player == 2 and self.playing_vs_computer:
            self.root.after(500, self.computer_move)

    def create_game_ui(self):
        score_frame = tk.Frame(self.game_frame)
        score_frame.pack(fill="x", pady=(0, 10))

        self.player1_label = tk.Label(score_frame, text=f"{self.player1['name']} (X): {self.player1['score']}",
                                      font=("Arial", 10, "bold"), fg=self.player1["color"])
        self.player1_label.pack(side="left")

        self.player2_label = tk.Label(score_frame, text=f"{self.player2['name']} (O): {self.player2['score']}",
                                      font=("Arial", 10, "bold"), fg=self.player2["color"])
        self.player2_label.pack(side="right")

        self.current_player_label = tk.Label(self.game_frame, text=f"Current turn: {self.player1['name']} (X)",
                                             font=("Arial", 10), fg=self.player1["color"])
        self.current_player_label.pack(pady=(0, 10))

        board_frame = tk.Frame(self.game_frame)
        board_frame.pack()

        self.cells = []
        for i in range(3):
            for j in range(3):
                index = i * 3 + j
                cell = tk.Button(board_frame, width=5, height=2, font=("Arial", 24, "bold"),
                                 command=lambda idx=index: self.cell_click(idx))
                cell.grid(row=i, column=j, padx=2, pady=2, sticky="nsew")
                self.cells.append(cell)

        control_frame = tk.Frame(self.game_frame)
        control_frame.pack(fill="x", pady=(15, 0))

        tk.Button(control_frame, text="New Game", command=self.reset_game).pack(side="left", fill="x", expand=True, padx=5)
        tk.Button(control_frame, text="Reset Scores", command=self.reset_scores).pack(side="left", fill="x", expand=True, padx=5)
        tk.Button(control_frame, text="Quit", command=self.root.quit).pack(side="right", fill="x", expand=True, padx=5)

    def cell_click(self, index):
        if self.board[index] is not None or self.game_over:
            return

        self.make_move(index)

        if self.playing_vs_computer and not self.game_over and self.current_player == 2:
            self.root.after(500, self.computer_move)

    def make_move(self, index):
        symbol = "X" if self.current_player == 1 else "O"
        color = self.player1["color"] if self.current_player == 1 else self.player2["color"]
        self.board[index] = symbol
        self.cells[index].config(text=symbol, fg=color)

        winner, win_pattern = self.check_winner()
        if winner:
            self.game_over = True
            if winner == "tie":
                messagebox.showinfo("Game Over", "It's a tie!")
            else:
                name = self.player1["name"] if winner == "X" else self.player2["name"]
                if winner == "X":
                    self.player1["score"] += 1
                    self.player1_label.config(text=f"{self.player1['name']} (X): {self.player1['score']}")
                else:
                    self.player2["score"] += 1
                    self.player2_label.config(text=f"{self.player2['name']} (O): {self.player2['score']}")
                for idx in win_pattern:
                    self.cells[idx].config(bg="lightgreen")
                messagebox.showinfo("Game Over", f"{name} wins!")
        else:
            self.current_player = 2 if self.current_player == 1 else 1
            symbol = "X" if self.current_player == 1 else "O"
            name = self.player1["name"] if self.current_player == 1 else self.player2["name"]
            color = self.player1["color"] if self.current_player == 1 else self.player2["color"]
            self.current_player_label.config(text=f"Current turn: {name} ({symbol})", fg=color)

    def computer_move(self):
        empty = [i for i, val in enumerate(self.board) if val is None]
        if empty:
            move = random.choice(empty)
            self.make_move(move)

    def check_winner(self):
        wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
        for a, b, c in wins:
            if self.board[a] and self.board[a] == self.board[b] == self.board[c]:
                return self.board[a], [a, b, c]
        if None not in self.board:
            return "tie", []
        return None, []

    def reset_game(self):
        self.board = [None] * 9
        for cell in self.cells:
            cell.config(text="", bg="SystemButtonFace")
        self.game_over = False
        self.current_player = 1
        self.current_player_label.config(text=f"Current turn: {self.player1['name']} (X)", fg=self.player1["color"])
        if self.playing_vs_computer and self.current_player == 2:
            self.root.after(500, self.computer_move)

    def reset_scores(self):
        self.player1["score"] = 0
        self.player2["score"] = 0
        self.player1_label.config(text=f"{self.player1['name']} (X): 0")
        self.player2_label.config(text=f"{self.player2['name']} (O): 0")

def main():
    root = tk.Tk()
    TicTacToeGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
