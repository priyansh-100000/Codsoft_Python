import tkinter as tk
import random
from tkinter import messagebox

choices = ["Rock", "Paper", "Scissors"]

user_score = 0
computer_score = 0

def determine_winner(user_choice):

    global user_score, computer_score

    computer_choice = random.choice(choices)
    result = ""

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    label_user_choice.config(text=f"Your Choice: {user_choice}")
    label_computer_choice.config(text=f"Computer's Choice: {computer_choice}")
    label_result.config(text=f"Result: {result}", fg="green" if "Win" in result else "red")
    label_score.config(text=f"Score ➔ You: {user_score} | Computer: {computer_score}")

def play_again():
    label_user_choice.config(text="Your Choice: ")
    label_computer_choice.config(text="Computer's Choice: ")
    label_result.config(text="Result: ")
  
def exit_game():
    confirm = messagebox.askyesno("Exit", "Are you sure you want to exit?")
    if confirm:
        root.destroy()

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("520x550")
root.config(bg="#f2f2f2")
root.resizable(False, False)

label_heading = tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 24, "bold"), bg="#f2f2f2", fg="#333")
label_heading.pack(pady=20)

frame_choices = tk.Frame(root, bg="#f2f2f2")
frame_choices.pack(pady=10)

btn_rock = tk.Button(frame_choices, text="Rock 🪨", font=("Arial", 14), width=12, command=lambda: determine_winner("Rock"))
btn_rock.grid(row=0, column=0, padx=10)

btn_paper = tk.Button(frame_choices, text="Paper 📄", font=("Arial", 14), width=12, command=lambda: determine_winner("Paper"))
btn_paper.grid(row=0, column=1, padx=10)

btn_scissors = tk.Button(frame_choices, text="Scissors ✂️", font=("Arial", 14), width=12, command=lambda: determine_winner("Scissors"))
btn_scissors.grid(row=0, column=2, padx=10)

label_user_choice = tk.Label(root, text="Your Choice: ", font=("Arial", 14), bg="#f2f2f2")
label_user_choice.pack(pady=10)

label_computer_choice = tk.Label(root, text="Computer's Choice: ", font=("Arial", 14), bg="#f2f2f2")
label_computer_choice.pack(pady=10)

label_result = tk.Label(root, text="Result: ", font=("Arial", 16, "bold"), bg="#f2f2f2")
label_result.pack(pady=20)

label_score = tk.Label(root, text="Score ➔ You: 0 | Computer: 0", font=("Arial", 14), bg="#f2f2f2", fg="#555")
label_score.pack(pady=10)

frame_bottom = tk.Frame(root, bg="#f2f2f2")
frame_bottom.pack(pady=20)

btn_play_again = tk.Button(frame_bottom, text="Play Again 🔁", font=("Arial", 12), width=15, command=play_again)
btn_play_again.grid(row=0, column=0, padx=10)

btn_exit = tk.Button(frame_bottom, text="Exit 🚪", font=("Arial", 12), width=15, command=exit_game)
btn_exit.grid(row=0, column=1, padx=10)

root.mainloop()
