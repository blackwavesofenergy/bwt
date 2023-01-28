import tkinter as tk
import pickle
from datetime import datetime
from pathlib import Path

def on_press():
    current_date = datetime.now().strftime("%d %B, %Y")
    black_wave_dates.append("Black waves hit you on " + current_date)
    save_black_wave_dates()
    display_black_wave_dates()

def save_black_wave_dates():
    with open(black_wave_dates_file, "wb") as f:
        pickle.dump(black_wave_dates, f)

def load_black_wave_dates():
    if black_wave_dates_file.exists():
        with open(black_wave_dates_file, "rb") as f:
            return pickle.load(f)
    else:
        return []

def display_black_wave_dates():
    black_wave_text = "\n".join(black_wave_dates)
    text.delete(1.0, tk.END)
    text.insert(tk.END, black_wave_text)

root = tk.Tk()
root.title("Don't let the black waves get you.")
root.configure(bg='black')
root.geometry("400x400")

black_wave_dates_file = Path(__file__).parent / "pkl" / "black_wave_dates.pkl"
black_wave_dates = load_black_wave_dates()

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

button = tk.Button(frame, text="BLACK WAVE!", command=on_press, bg='black', fg='black', font=("Product Sans Light", 20))
button.pack()

text = tk.Text(frame, wrap=tk.WORD, bg='black', fg='white', font=("Product Sans Light", 20))
text.pack(expand=True, fill=tk.BOTH)

display_black_wave_dates()
root.mainloop()
