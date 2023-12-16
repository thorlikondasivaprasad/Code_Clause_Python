import pyttsx3 as pyt
import wikipedia
import tkinter as tk

def search_wikipedia():
    query = entry.get()
    try:
        result = wikipedia.summary(query, sentences=3)
        print(result)  # Print the retrieved data on the terminal
        text.delete(1.0, tk.END)  # Clear previous text
        text.insert(tk.END, result)
        speak(result)
    except wikipedia.exceptions.PageError:
        text.delete(1.0, tk.END)
        text.insert(tk.END, "No Wikipedia page found for the given query.")
        speak("No Wikipedia page found for the given query.")

def speak(text):
    voice = pyt.init()
    voice.say(text)
    voice.runAndWait()

# GUI setup
root = tk.Tk()
root.title("Wikipedia Search")
root.geometry("500x500")  # Set the window size
root.configure(bg="#32a8a2")  # Set background color

# Entry for user input
entry = tk.Entry(root, width=50)
entry.pack(padx=10, pady=10)

# Button to trigger search
search_button = tk.Button(root, text="Search", command=search_wikipedia, bg="#4CAF50", fg="white")
search_button.pack(pady=5)

# Text widget to display results
text = tk.Text(root, width=50, height=10, wrap=tk.WORD)
text.pack(padx=10, pady=10)

root.mainloop()
