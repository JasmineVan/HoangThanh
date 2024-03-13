import requests
import time
from GradientFrame import GradientFrame
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import ttk
from tkinter import Tk, Button, Frame, messagebox 

def get_data_from(url):
    if url != "":
        try:
            response = requests.get(url)
            response.raise_for_status()  
        except requests.exceptions.RequestException as e:
            print(f"Error: An error occurred while fetching the website: {e}")
            exit()
    soup = BeautifulSoup(response.content, 'html.parser')
    # time.sleep(10)
    print(soup)
    all_links = soup.find_all('h3', class_='title-news')
    link_data = []
    link_data.append(['No', 'Title'])
    counter = 1
    for link in all_links:
        print(link)
        link_text = link.text.strip()
        link_url = link.get('href')

        tempList = []
        tempList.append(counter)
        tempList.append(link_text)
        counter += 1

        link_data.append(tempList) 
    return link_data

def create_table(data):
    # Create a Treeview widget for the table
    print(data)

    table = ttk.Treeview(window, columns=data[0], show="headings", height=10)
    style = ttk.Style(window)
    style.theme_use("clam")
    style.configure("Treeview.Heading", background="#31363F", foreground="#EEEEEE")
    table.pack(padx=20, pady=20, side=TOP)
    table.place()
    table.column("# 1",anchor=CENTER, stretch=NO, width=100)
    table.column("# 2", anchor="sw", stretch=NO, width=max_width)
    table.pack(expand=True)
    # Define headings for each column
    for col_index, col_name in enumerate(data[0]):
        table.heading(col_index, text=col_name)

    # Add data rows
    for row_data in data[1:]:
        table.insert("", END, values=row_data)

def button_clicked():
  # Get the text from the input field
  text = entry.get()
  # Handle
  print(f"You entered: {text}")
  print(f"{max_width, max_height}")
  print(type(data))
  # Clear
  result = get_data_from(text)
  create_table(result)
  entry.delete(0, END)

def close_button_clicked():
  if messagebox.askyesno("Close App", "Are you sure to close application?"):
    window.destroy()

def minimize_button_clicked():
  window.wm_iconify()

def fullscreen_button_clicked():
  window.attributes('-fullscreen', not window.attributes('-fullscreen'))    

# Create the main window
window = Tk()
# Gradient
# gf = GradientFrame(window, colors = ("yellow", "black"), width = 800, height = 600)
# gf.config(direction = gf.left2right)
# gf.pack()

window.attributes('-fullscreen', True)
window.title("Hoang Thanh Application")
max_width = window.winfo_screenwidth()
max_height = window.winfo_screenheight()
# Scroll bar

# Button frame
button_frame = Frame(window)
button_frame.pack(fill=X, side=TOP) 

# Close button
close_button = ttk.Button(button_frame, text="X", command=close_button_clicked) 
close_button.pack(side=RIGHT) 

# Full screen button
fullscreen_button = ttk.Button(button_frame, text="◻️", command=fullscreen_button_clicked) 
fullscreen_button.pack(side=RIGHT)  

# Minimize button
minimize_button = ttk.Button(button_frame, text="-", command=minimize_button_clicked)
minimize_button.pack(side=RIGHT)

# Create a label with some text
my_label = Label(
    window,
    text="Enter URL to crawl data!",
    foreground="#007F73",
    font=("Arial", 28, "bold"),
    )
my_label.pack(padx=20, pady=20)

# Create a label with some text
my_label2 = Label(
    window,
    text="Simple crawling tool from - Thuong Trinh Van <3",
    foreground="#31363F",
    font=("Arial", 13, "bold"),
    )
my_label2.pack()

# Input field
entry = Entry(window, width=100)
entry.pack(padx=20, pady=20)

# Create the button
button = Button(
    window,
    text="Crawl",
    command=button_clicked,
    bg="#007F73",
    fg="#ffffff",
    font=("Arial", 13),
    border=4)

button.pack()

window.geometry("300x150+300+300")  # Adjust width, height, x-offset, and y-offset as needed

# Sample data for the table
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "London"],
]

# Display
window.mainloop()
