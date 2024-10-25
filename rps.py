import customtkinter as ctk
import random

def main():
    root = ctk.CTk()
    root.title("Rock Paper Scissors")
    root.geometry("600x300")

    title_label = ctk.CTkLabel(root, text="Rock, Paper, Scissors", font=("Arial", 16))
    title_label.pack(pady=20)

    choices_frame = ctk.CTkFrame(root)
    choices_frame.pack(pady=20)

    rock_button = ctk.CTkButton(choices_frame, text="Rock", command=lambda: play("Rock"))
    rock_button.grid(row=0, column=0, padx=10)

    paper_button = ctk.CTkButton(choices_frame, text="Paper", command=lambda: play("Paper"))
    paper_button.grid(row=0, column=1, padx=10)

    scissors_button = ctk.CTkButton(choices_frame, text="Scissors", command=lambda: play("Scissors"))
    scissors_button.grid(row=0, column=2, padx=10)

    global result_label
    result_label = ctk.CTkLabel(root, text="", font=("Arial", 14))
    result_label.pack(pady=20)

    root.mainloop()

def play(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    result = determine_winner(user_choice, computer_choice)

    result_label.configure(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\nResult: {result}")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        return "You win!"
    else:
        return "You lose!"

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")  # options "blue", "green", etc.
main()
