import tkinter as tk
import requests
import pyperclip

def shorten_url():
    long_url = long_url_entry.get()
    api_url = f"http://tinyurl.com/api-create.php?url={long_url}"
    response = requests.get(api_url)
    if response.status_code == 200:
        short_url = response.text
        short_url_label.configure(text=short_url)
        pyperclip.copy(short_url)
        copy_button.configure(state=tk.NORMAL)
    else:
        short_url_label.configure(text="Error: Unable to shorten URL")
        copy_button.configure(state=tk.DISABLED)

def copy_to_clipboard():
    short_url = short_url_label.cget("text")
    pyperclip.copy(short_url)

# GUI setup
window = tk.Tk()
window.title("URL Shortener")

long_url_label = tk.Label(window, text="Enter URL:")
long_url_label.pack()

long_url_entry = tk.Entry(window, width=50)
long_url_entry.pack()

shorten_button = tk.Button(window, text="Shorten URL", command=shorten_url)
shorten_button.pack()

short_url_label = tk.Label(window, text="")
short_url_label.pack()

copy_button = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard, state=tk.DISABLED)
copy_button.pack()

window.mainloop()
