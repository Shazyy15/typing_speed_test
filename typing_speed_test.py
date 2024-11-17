import tkinter as tk
from tkinter import messagebox
import random
import time

# List of sample texts
sample_texts = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is an amazing programming language.",
    "Artificial intelligence is the future of technology.",
    "Typing fast requires consistent practice and focus.",
    "A journey of a thousand miles begins with a single step.",
    "The only limit to our realization of tomorrow is our doubts of today."
]

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("700x500")
        self.root.resizable(False, False)
        self.root.config(bg="#f0f8ff")
        
        self.start_time = None
        self.text_to_type = ""
        
        # Header
        tk.Label(root, text="Typing Speed Test", font=("Arial", 24, "bold"), bg="#f0f8ff", fg="#000080").pack(pady=10)
        
        # Instructions
        tk.Label(root, text="Type the text below as fast as you can:", font=("Arial", 14), bg="#f0f8ff").pack(pady=5)
        
        # Text to be typed
        self.text_label = tk.Label(root, text="", font=("Arial", 12, "italic"), wraplength=600, justify="center", bg="#f0f8ff", fg="#333333")
        self.text_label.pack(pady=10)
        
        # Typing entry box
        self.text_entry = tk.Text(root, font=("Arial", 12), height=5, width=60, wrap="word", relief="solid", bd=2)
        self.text_entry.pack(pady=10)
        
        # Buttons
        button_frame = tk.Frame(root, bg="#f0f8ff")
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="Start Test", command=self.start_test, font=("Arial", 12, "bold"), bg="#32cd32", fg="white", width=12).pack(side="left", padx=10)
        tk.Button(button_frame, text="Submit", command=self.calculate_speed, font=("Arial", 12, "bold"), bg="#4682b4", fg="white", width=12).pack(side="right", padx=10)
        
        # Results
        self.result_label = tk.Label(root, text="", font=("Arial", 14), fg="purple", bg="#f0f8ff")
        self.result_label.pack(pady=20)
        
        # Developer credit
        tk.Label(root, text="Developed by Shazil Shahid", font=("Arial", 10, "italic"), bg="#f0f8ff", fg="#555555").pack(side="bottom", pady=5)
    
    def start_test(self):
        self.text_to_type = random.choice(sample_texts)
        self.text_label.config(text=self.text_to_type)
        self.text_entry.delete(1.0, tk.END)
        self.start_time = time.time()
        self.result_label.config(text="")
    
    def calculate_speed(self):
        if not self.start_time:
            messagebox.showerror("Error", "Click 'Start Test' to begin.")
            return
        
        typed_text = self.text_entry.get(1.0, tk.END).strip()
        end_time = time.time()
        
        # Calculate time taken and words per minute
        time_taken = end_time - self.start_time
        word_count = len(typed_text.split())
        words_per_minute = (word_count / time_taken) * 60
        
        # Accuracy calculation
        correct_words = sum(1 for a, b in zip(typed_text.split(), self.text_to_type.split()) if a == b)
        accuracy = (correct_words / len(self.text_to_type.split())) * 100
        
        self.result_label.config(
            text=f"Time Taken: {time_taken:.2f} seconds\nWords Per Minute: {words_per_minute:.2f} WPM\nAccuracy: {accuracy:.2f}%"
        )

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()
