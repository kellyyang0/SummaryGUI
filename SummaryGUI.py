import tkinter as tk
import requests
from bs4 import BeautifulSoup
from tkinter import messagebox

# Define the function that is called when the user clicks the "Summarize" button
def summarize_article():
    # Get the topic entered by the user
    topic = topic_entry.get()

    # Define the URL of the Wikipedia page to scrape
    url = f"https://en.wikipedia.org/wiki/{topic}"

    # Send an HTTP request to the URL and store the response
    response = requests.get(url)

    # Parse the HTML content of the response
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract the first paragraph of the article
    first_paragraph = soup.find("table").text
 
    # Display the summary in a message box
    messagebox.showinfo("Summary", first_paragraph)

# Create the GUI window
root = tk.Tk()
root.geometry("400x200")
root.title("Wikipedia Summary")

# Add a label and text entry box for the topic
topic_label = tk.Label(root, text="Enter a topic:")
topic_label.grid(row=0, column=0, sticky="W")
topic_entry = tk.Entry(root)
topic_entry.grid(row=0, column=1)

# Add a button to summarize the article
summarize_button = tk.Button(root, text="Summarize", command=summarize_article)
summarize_button.grid(row=1, column=0, columnspan=2)

# Start the GUI event loop
root.mainloop()
