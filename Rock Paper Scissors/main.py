# Import the necessary modules
import tkinter as tk  # Import the tkinter module for creating the GUI
import random  # Import the random module for generating random choices for the computer

class RockPaperScissorsGame:
    def __init__(self, root):
        # Initialize the main window and set the title
        self.root = root
        self.root.title("Rock Paper Scissors Game")
        
        # Initialize scores for user, computer, and ties
        self.user_score = 0
        self.computer_score = 0
        self.tie_score = 0
        
        # Create and arrange GUI widgets
        self.create_widgets()
        
    def create_widgets(self):
        # Create a label to instruct the user
        self.label = tk.Label(self.root, text="Choose Rock, Paper or Scissors", font=("Helvetica", 18, "bold"))
        self.label.grid(row=0, column=0, columnspan=3, pady=20)
        
        # Create buttons for Rock, Paper, and Scissors
        self.rock_button = tk.Button(self.root, text="Rock", font=("Helvetica", 14), width=10, command=lambda: self.play_game("Rock"))
        self.rock_button.grid(row=1, column=0, padx=20, pady=10)
        
        self.paper_button = tk.Button(self.root, text="Paper", font=("Helvetica", 14), width=10, command=lambda: self.play_game("Paper"))
        self.paper_button.grid(row=1, column=1, padx=20, pady=10)
        
        self.scissors_button = tk.Button(self.root, text="Scissors", font=("Helvetica", 14), width=10, command=lambda: self.play_game("Scissors"))
        self.scissors_button.grid(row=1, column=2, padx=20, pady=10)
        
        # Create a label to display the result of each game
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 16))
        self.result_label.grid(row=2, column=0, columnspan=3, pady=20)
        
        # Create a label to display the scores
        self.score_label = tk.Label(self.root, text="Scores\nUser: 0\nComputer: 0\nTies: 0", font=("Helvetica", 16))
        self.score_label.grid(row=3, column=0, columnspan=3, pady=20)
        
        # Create a button to reset the scores
        self.reset_button = tk.Button(self.root, text="Reset Scores", font=("Helvetica", 14), command=self.reset_scores)
        self.reset_button.grid(row=4, column=0, columnspan=3, pady=10)
    
    def play_game(self, user_choice):
        # Generate the computer's choice randomly
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        
        # Determine the result of the game
        if user_choice == computer_choice:
            result = "It's a tie!"
            self.tie_score += 1
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            result = "You win!"
            self.user_score += 1
        else:
            result = "Computer wins!"
            self.computer_score += 1
        
        # Update the result label with the choices and result
        self.result_label.config(text=f"User: {user_choice}\nComputer: {computer_choice}\n{result}")
        
        # Update the scores
        self.update_scores()
        
    def update_scores(self):
        # Update the score label with the current scores
        self.score_label.config(text=f"Scores\nUser: {self.user_score}\nComputer: {self.computer_score}\nTies: {self.tie_score}")
    
    def reset_scores(self):
        # Reset the scores to zero
        self.user_score = 0
        self.computer_score = 0
        self.tie_score = 0
        
        # Update the scores and clear the result label
        self.update_scores()
        self.result_label.config(text="")
        
if __name__ == "__main__":
    # Create the main Tkinter window
    root = tk.Tk()
    
    # Create an instance of the game
    game = RockPaperScissorsGame(root)
    
    # Run the Tkinter main loop to display the GUI and handle user interactions
    root.mainloop()
