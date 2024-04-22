import tkinter as tk
from PIL import Image, ImageTk
import os

def open_virtual_assistant():
    os.system("python Assistant.py")

def open_gesture_control():
    os.system("python Gesture.py")

def toggle_dark_mode():
    if dark_mode.get():
        window.config(bg="#2c2c2c")
        heading_label.config(fg="white", font=("Montserrat", 36, "bold"), padx=20, pady=20, relief=tk.RAISED, bg="#404040")
        assistant_label.config(fg="white", font=("Roboto", 18))
        gesture_label.config(fg="white", font=("Roboto", 18))
        virtual_assistant_button.config(bg="#404040", fg="white", activebackground="#555555", activeforeground="white", font=("Montserrat", 18, "bold"), relief=tk.RAISED)
        gesture_control_button.config(bg="#404040", fg="white", activebackground="#555555", activeforeground="white", font=("Montserrat", 18, "bold"), relief=tk.RAISED)
        dark_mode_button.config(text="Light Mode", bg="#404040", fg="white", activebackground="#555555", activeforeground="white", font=("Roboto", 16), relief=tk.RAISED)
    else:
        window.config(bg="#f0f0f0")
        heading_label.config(fg="#2c2c2c", font=("Montserrat", 36, "bold"), padx=20, pady=20, relief=tk.RAISED, bg="#e0e0e0")
        assistant_label.config(fg="#2c2c2c", font=("Roboto", 18))
        gesture_label.config(fg="#2c2c2c", font=("Roboto", 18))
        virtual_assistant_button.config(bg="#e0e0e0", fg="#2c2c2c", activebackground="#d0d0d0", activeforeground="#2c2c2c", font=("Montserrat", 18, "bold"), relief=tk.RAISED)
        gesture_control_button.config(bg="#e0e0e0", fg="#2c2c2c", activebackground="#d0d0d0", activeforeground="#2c2c2c", font=("Montserrat", 18, "bold"), relief=tk.RAISED)
        dark_mode_button.config(text="Dark Mode", bg="#e0e0e0", fg="#2c2c2c", activebackground="#d0d0d0", activeforeground="#2c2c2c", font=("Roboto", 16), relief=tk.RAISED)

# Create the main window
window = tk.Tk()
window.title("IntelliGest Desktop Commander")
window.geometry("800x600")

# Heading at the top
heading_label = tk.Label(window, text="IntelliGest Desktop Commander", font=("Montserrat", 36, "bold"), padx=20, pady=20, relief=tk.RAISED, bg="#e0e0e0", fg="#2c2c2c")
heading_label.pack(pady=20)

# Load the original icons
current_dir = os.path.dirname(_file_)
assistant_img_path = os.path.join(current_dir, "Assistant_img.jpeg")
gesture_control_img_path = os.path.join(current_dir, "Gesture_img.jpeg")

if not os.path.exists(assistant_img_path):
    print("Error: Assistant_img.jpg not found!")
    exit()

if not os.path.exists(gesture_control_img_path):
    print("Error: Gesture_control_img.jpg not found!")
    exit()

original_virtual_assistant_icon = Image.open(assistant_img_path)
original_gesture_control_icon = Image.open(gesture_control_img_path)

# Resize the images to the desired square size, for example, 200x200 pixels
resized_virtual_assistant_icon = original_virtual_assistant_icon.resize((200, 200), Image.LANCZOS)
resized_gesture_control_icon = original_gesture_control_icon.resize((200, 200), Image.LANCZOS)

# Convert the resized images to PhotoImage
virtual_assistant_icon = ImageTk.PhotoImage(resized_virtual_assistant_icon)
gesture_control_icon = ImageTk.PhotoImage(resized_gesture_control_icon)

# Create the main frame and the two child frames
main_frame = tk.Frame(window, bg="#2c2c2c")
main_frame.pack(fill=tk.BOTH, expand=True)

left_frame = tk.Frame(main_frame, bg="#2c2c2c")
left_frame.pack(side=tk.LEFT, padx=50, pady=50, fill=tk.BOTH, expand=True)

right_frame = tk.Frame(main_frame, bg="#2c2c2c")
right_frame.pack(side=tk.RIGHT, padx=50, pady=50, fill=tk.BOTH, expand=True)

# Virtual Assistant section
virtual_assistant_button = tk.Button(left_frame, image=virtual_assistant_icon, text="Assistant", compound="top", font=("Montserrat", 18, "bold"), command=open_virtual_assistant, bg="#404040", fg="white", activebackground="#555555", activeforeground="white", relief=tk.RAISED, padx=20, pady=20)
virtual_assistant_button.pack(side=tk.TOP, pady=20)

assistant_label = tk.Label(left_frame, text="Launch the Virtual Assistant", font=("Roboto", 18), bg="#2c2c2c", fg="white")
assistant_label.pack(side=tk.TOP, pady=10)

# Gesture Control section
gesture_control_button = tk.Button(right_frame, image=gesture_control_icon, text="Gesture Control", compound="top", font=("Montserrat", 18, "bold"), command=open_gesture_control, bg="#404040", fg="white", activebackground="#555555", activeforeground="white", relief=tk.RAISED, padx=20, pady=20)
gesture_control_button.pack(side=tk.TOP, pady=20)

gesture_label = tk.Label(right_frame, text="Launch the Gesture Control System", font=("Roboto", 18), bg="#2c2c2c", fg="white")
gesture_label.pack(side=tk.TOP, pady=10)

# Add a dark mode toggle
dark_mode = tk.BooleanVar(window, False)
dark_mode_button = tk.Checkbutton(window, text="Dark Mode", variable=dark_mode, command=toggle_dark_mode, font=("Roboto", 16), bg="#2c2c2c", fg="white", activebackground="#404040", activeforeground="white", relief=tk.RAISED)
dark_mode_button.pack(side=tk.BOTTOM, pady=20)

# Run the main loop
window.mainloop()
