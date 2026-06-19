import tkinter as tk
from tkinter import messagebox

from task3 import BG_COLOR

# App Settings
window_width, window_height = 700, 800
root = tk.Tk()
root.title("Neon Tic-Tac-Toe AI")
root.geometry(f"{window_width}x{window_height}")
root.configure(bg="black")
root.resizable(False, False)

# Game State & Colors
board = [""] * 9
player, ai = "X", "O"
buttons = []
bg_color, GRID_COLOR, TEXT_COLOR, CYAN_COLOR = "black", "#ff3030", "#66ff66", "#00ffff"

# Start Screen Layout
start_frame = tk.Frame(root, bg=bg_color)
start_frame.pack(fill="both", expand=True)

title_label = tk.Label(start_frame, text="YOU VS AI TIC-TAC-TOE", bg=bg_color, fg=GRID_COLOR, font=("Arial", 30, "bold"))
title_label.pack(pady=(180, 20))

ready_label = tk.Label(start_frame, text="Ready To Play?", bg=bg_color, fg="white", font=("Arial", 20))
ready_label.pack(pady=10)

def hover_enter(event): play_button.config(bg="#33ffff")
def hover_leave(event): play_button.config(bg=CYAN_COLOR)
def start_game():
    start_frame.pack_forget()
    create_game_screen()

play_button = tk.Button(start_frame, text="PLAY GAME", width=15, height=2, bg=CYAN_COLOR, fg="black", font=("Arial", 16, "bold"), command=start_game)
play_button.pack(pady=40)
play_button.bind("<Enter>", hover_enter)
play_button.bind("<Leave>", hover_leave)

def create_game_screen():
    global game_frame, status_label
    game_frame = tk.Frame(root, bg=bg_color)
    game_frame.pack(fill="both", expand=True)

    status_label = tk.Label(game_frame, text="Your Turn (X)", bg=bg_color, fg=CYAN_COLOR, font=("Arial", 18, "bold"))
    status_label.pack(pady=20)

    board_frame = tk.Frame(game_frame, bg=GRID_COLOR)
    board_frame.pack(pady=20)

    for row in range(3):
        for col in range(3):
            index = row * 3 + col
            btn = tk.Button(board_frame, text="", width=6, height=3, bg=bg_color, fg=TEXT_COLOR,
                            activebackground=bg_color, activeforeground=TEXT_COLOR, font=("Arial", 28, "bold"),
                            bd=3, relief="solid", highlightbackground=GRID_COLOR, highlightcolor=GRID_COLOR,
                            highlightthickness=2, command=lambda i=index: player_move(i))
            btn.grid(row=row, column=col, padx=3, pady=3)
            buttons.append(btn)

    restart_button = tk.Button(game_frame, text="RESTART", width=15, height=2, bg=CYAN_COLOR, fg="black", font=("Arial", 14, "bold"), command=reset_game)
    restart_button.pack(pady=20)
#conditions to check for winner
def check_winner(current_board):
    winning_positions = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for combo in winning_positions:
        a, b, c = combo
        if current_board[a] != "" and current_board[a] == current_board[b] and current_board[b] == current_board[c]:
            return current_board[a]
    return "Draw" if "" not in current_board else None

def reset_game():
    global board
    board = [""] * 9
    status_label.config(text="Your Turn (X)")
    for btn in buttons:
        btn.config(text="", state="normal")

def disable_board():
    for btn in buttons:
        btn.config(state="disabled")

def player_move(index):
    if board[index] != "": return
    board[index] = player
    buttons[index].config(text=player, state="disabled")
    winner = check_winner(board)
    if winner:
        end_game(winner)
        return
    status_label.config(text="AI Thinking...")
    root.after(500, ai_move)
# mimmax algorithm for AI move
def minimax(board_state, is_maximizing):
    winner = check_winner(board_state)
    if winner == ai: return 1
    if winner == player: return -1
    if winner == "Draw": return 0

    if is_maximizing:
        best_score = -100
        for i in range(9):
            if board_state[i] == "":
                board_state[i] = ai
                score = minimax(board_state, False)
                board_state[i] = ""
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = 100
        for i in range(9):
            if board_state[i] == "":
                board_state[i] = player
                score = minimax(board_state, True)
                board_state[i] = ""
                best_score = min(score, best_score)
        return best_score
#AI code to win this game in higher possibilities
def ai_move():
    best_score = -100
    best_move = None
    for i in range(9):
        if board[i] == "":
            board[i] = ai
            score = minimax(board, False)
            board[i] = ""
            if score > best_score:
                best_score = score
                best_move = i
    if best_move is not None:
        board[best_move] = ai
        buttons[best_move].config(text=ai, state="disabled")
    winner = check_winner(board)
    if winner:
        end_game(winner)
        return
    status_label.config(text="Your Turn (X)")

def end_game(winner):
    msg = "It's a Draw!" if winner == "Draw" else f"{winner} Wins!"
    messagebox.showinfo("Game Over" if winner == "Draw" else "Winner", msg)
    disable_board()

root.mainloop()
