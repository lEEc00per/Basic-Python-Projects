import tkinter as tk
import webbrowser

def open_video():
    # Replace with the YouTube URL you want to open
    youtube_url = "https://www.youtube.com/watch?v=MM_PM7BPcSU"
    webbrowser.open(youtube_url)

# Create the main window
root = tk.Tk()
root.title("YouTube Video Button")

# Create the button
button = tk.Button(root, text="Watch Video", command=open_video, font=("Ubuntu", 16), bg="teal", fg="white")
button.pack(pady=70)

# Run the application
root.mainloop()