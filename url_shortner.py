import tkinter as tk
from tkinter import ttk
import pyshorteners

def shorten_url():
    s = pyshorteners.Shortener()
    url = entry.get()
    try:
        short_url = s.tinyurl.short(url)
        result_label.config(text=short_url)
    except Exception as e:
        result_label.config(text="Error: " + str(e))

root = tk.Tk()
root.title("URL Shortener")
root.geometry("400x300")

entry_label = ttk.Label(root, text="Enter the URL:")
entry_label.pack()

entry = ttk.Entry(root, width=30)
entry.pack()

button = ttk.Button(root, text="Shorten URL", command=shorten_url)
button.pack()

result_label = ttk.Label(root, text="")
result_label.pack()

root.mainloop()