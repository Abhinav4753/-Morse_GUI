import RPi.GPIO as GPIO
import tkinter as tk
from tkinter import ttk
import time

# Define Morse code mappings
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': '/'
}

# GPIO setup
led_pin = 10  # Replace with your GPIO pin number
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)

# Function to blink LED in Morse code
def blink_morse_code(name):
    for char in name.upper():
        if char in morse_code_dict:
            morse_code = morse_code_dict[char]
            for symbol in morse_code:
                if symbol == '.':
                    GPIO.output(led_pin, GPIO.HIGH)  # Turn LED on for a dot
                    time.sleep(0.2)  # Dot duration
                    GPIO.output(led_pin, GPIO.LOW)  # Turn LED off
                    time.sleep(0.2)  # Gap between dots and dashes
                elif symbol == '-':
                    GPIO.output(led_pin, GPIO.HIGH)  # Turn LED on for a dash
                    time.sleep(0.6)  # Dash duration
                    GPIO.output(led_pin, GPIO.LOW)  # Turn LED off
                    time.sleep(0.2)  # Gap between dots and dashes
            time.sleep(0.4)  # Gap between characters
        else:
            time.sleep(0.8)  # Gap between words

# GUI setup
root = tk.Tk()
root.title("Name to Morse Code LED Blinker")

# Function to handle button click
def start_blinking():
    name = entry.get()
    blink_morse_code(name)

frame = ttk.Frame(root, padding=(20, 20), style="My.TFrame")
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)

label = ttk.Label(frame, text="Insert a name ", font=("Times New Roman", 20), foreground="blue")
label.grid(column=0, row=0, columnspan=2, pady=(0, 20))

entry = ttk.Entry(frame, width=20, font=("Arial", 20), background="lightgreen")
entry.grid(column=0, row=1, columnspan=2, pady=(0, 10))

button = ttk.Button(frame, text="Blink  ", command=start_blinking, style="TButton")
button.grid(column=0, row=2, columnspan=2, pady=(0, 20))

style = ttk.Style()
style.configure("TButton", background="blue", foreground="white", font=("Times New Roman", 20))
style.configure("My.TFrame", background="#F0F0F0")  # Light gray background

root.mainloop()

GPIO.cleanup()
