import tkinter as tk
import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "You lose."

def play(choice):
    global wins, losses, ties

    user_choice.set(choice.capitalize())
    comp = get_computer_choice()
    computer_choice.set(comp.capitalize())

    result = determine_winner(choice, comp)
    result_text.set(result)

    if result == "You win!":
        wins += 1
    elif result == "You lose.":
        losses += 1
    else:
        ties += 1

    score_text.set(f"{wins} 🏆 | {losses} ❌ | {ties} 🤝")

def reset():
    user_choice.set("")
    computer_choice.set("")
    result_text.set("")
    score_text.set(f"{wins} 🏆 | {losses} ❌ | {ties} 🤝")

root = tk.Tk()
root.title("Rock Paper Scissors - Stylish UI")
root.geometry("420x500")
root.configure(bg="#1e1e2f")


wins = losses = ties = 0
user_choice = tk.StringVar()
computer_choice = tk.StringVar()
result_text = tk.StringVar()
score_text = tk.StringVar(value="0 🏆 | 0 ❌ | 0 🤝")


def make_label(text, size=12, bold=False, fg="#ffffff", pady=5):
    font = ("Segoe UI", size, "bold" if bold else "normal")
    return tk.Label(root, text=text, font=font, fg=fg, bg="#1e1e2f", pady=pady)

def make_button(text, command):
    return tk.Button(
        button_frame,
        text=text,
        width=12,
        height=2,
        font=("Segoe UI", 10, "bold"),
        bg="#2d2d44",
        fg="#ffffff",
        activebackground="#444466",
        activeforeground="white",
        command=command,
        bd=0,
        relief="ridge"
    )

make_label("Rock, Paper, Scissors", 18, bold=True, fg="#ffcc00", pady=10).pack()

make_label("Your Choice:").pack()
tk.Label(root, textvariable=user_choice, font=("Segoe UI", 14), fg="#00acee", bg="#1e1e2f").pack()

make_label("Computer's Choice:").pack()
tk.Label(root, textvariable=computer_choice, font=("Segoe UI", 14), fg="#ff4444", bg="#1e1e2f").pack()

make_label("", pady=2).pack()
tk.Label(root, textvariable=result_text, font=("Segoe UI", 14, "bold"), fg="#33ff77", bg="#1e1e2f").pack()

make_label("Score", bold=True).pack()
tk.Label(root, textvariable=score_text, font=("Segoe UI", 13), fg="#ffffff", bg="#1e1e2f").pack()

button_frame = tk.Frame(root, bg="#1e1e2f")
button_frame.pack(pady=30)

make_button("🪨 Rock", lambda: play("rock")).grid(row=0, column=0, padx=10)
make_button("📄 Paper", lambda: play("paper")).grid(row=0, column=1, padx=10)
make_button("✂️ Scissors", lambda: play("scissors")).grid(row=0, column=2, padx=10)

tk.Button(
    root,
    text="🔁 Play Again",
    font=("Segoe UI", 10, "bold"),
    width=20,
    bg="#444466",
    fg="white",
    activebackground="#666688",
    command=reset
).pack(pady=10)


root.mainloop()
