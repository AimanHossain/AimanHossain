import tkinter as tk
from random import choice, shuffle
from time import time

class WordGuessApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Word Guess Game")

        self.words = ["python", "programming", "developer", "tkinter", "computer", "coding", "algorithm", "variable"]
        self.shuffle_word = ""
        self.score = 0
        self.time_start = 0
        self.level = 1

        self.label_info = tk.Label(self.master, text="Guess the word:")
        self.label_info.pack(pady=10)

        self.label_word = tk.Label(self.master, text="")
        self.label_word.pack(pady=20)

        self.entry_guess = tk.Entry(self.master)
        self.entry_guess.pack(pady=10)

        self.button_guess = tk.Button(self.master, text="Submit Guess", command=self.check_guess)
        self.button_guess.pack(pady=10)

        self.label_score = tk.Label(self.master, text="Score: 0")
        self.label_score.pack(pady=10)

        self.label_timer = tk.Label(self.master, text="Time left: ")
        self.label_timer.pack(pady=10)

        self.label_level = tk.Label(self.master, text=f"Level: {self.level}")
        self.label_level.pack(pady=10)

        self.start_game()

    def start_game(self):
        self.shuffle_word = self.get_shuffled_word()
        self.label_word.config(text=self.shuffle_word)
        self.entry_guess.delete(0, tk.END)
        self.time_start = time()
        self.update_timer()
        self.update_level()

    def update_timer(self):
        elapsed_time = round(time() - self.time_start, 2)
        remaining_time = max(0, 10 - elapsed_time)  # Set time limit to 10 seconds
        self.label_timer.config(text=f"Time left: {remaining_time} s")

        if remaining_time > 0:
            self.master.after(100, self.update_timer)
        else:
            self.label_info.config(text="Time's up! Try again.")
            self.start_game()

    def update_level(self):
        if self.score % 5 == 0 and self.score != 0:
            self.level += 1
            self.label_level.config(text=f"Level: {self.level}")

    def get_shuffled_word(self):
        word = choice(self.words)
        word_list = list(word)
        shuffle(word_list)
        return "".join(word_list)

    def check_guess(self):
        user_guess = self.entry_guess.get().lower()
        if user_guess == self.words[0]:
            self.score += 1
            self.label_score.config(text=f"Score: {self.score}")
            self.label_info.config(text="Correct! Well done.")
        else:
            self.label_info.config(text="Try again!")

        self.start_game()

if __name__ == "__main__":
    root = tk.Tk()
    app = WordGuessApp(root)
    root.mainloop()
