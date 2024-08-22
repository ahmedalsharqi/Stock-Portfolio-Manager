"""
 Author: Ahmed Alsharqi
 Date: 2024-08-08
 Updated: 2024-08-22
 Description: This script imports stock data from a JSON file, processes the data to calculate
 the value of each stock holding in a portfolio, stores the data in an SQLite database,
 and generates a line chart of portfolio values over time using matplotlib. 
 The script now includes a Tkinter GUI that allows the user to load the JSON file, 
 process the data, and visualize the portfolio value over time. 
 The GUI features a header, footer, background image, and centered buttons for a more engaging experience.
"""
# import statements
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk  
import json
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# This is a function to process the JSON file and store data in SQLite
def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            stocks_data = json.load(file)

        portfolio_df = pd.DataFrame(stocks_data)
        portfolio_df['Close'] = pd.to_numeric(portfolio_df['Close'], errors='coerce')
        portfolio_df['Date'] = pd.to_datetime(portfolio_df['Date'], format='%d-%b-%y')

        # Calculating the portfolio value
        portfolio_df['Shares'] = portfolio_df.groupby('Symbol')['Close'].transform('count')
        portfolio_df['value'] = portfolio_df['Close'] * portfolio_df['Shares']
        portfolio_df = portfolio_df.dropna(subset=['value'])

        # Storing the data in SQLite database
        conn = sqlite3.connect('stocks_portfolio.db')
        portfolio_df.to_sql('portfolio', conn, if_exists='replace', index=False)
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", "Stock data loaded and processed successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
#This is a function to visualize portfolio data
def visualize_data():
    try:
        conn = sqlite3.connect('stocks_portfolio.db')
        df = pd.read_sql_query("SELECT * FROM portfolio", conn)
        conn.close()

        plt.figure(figsize=(10, 6))
        for symbol, group in df.groupby('Symbol'):
            plt.plot(group['Date'], group['value'], label=symbol)

        plt.xlabel('Date')
        plt.ylabel('Portfolio Value')
        plt.title('Portfolio Value Over Time')
        plt.legend()
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while visualizing the data: {e}")

# This is a function to load the JSON file
def load_file():
    file_path = filedialog.askopenfilename(title="Open JSON File", filetypes=(("JSON Files", "*.json"),))
    if file_path:
        process_file(file_path)

# Initializing the main window
root = tk.Tk()
root.title("Stock Portfolio Manager")
root.geometry("800x600")

# Seting a background image
background_image = Image.open("backgroud.jpg")
background_photo = ImageTk.PhotoImage(background_image)

background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)

# Creating a frame for centering content
frame = tk.Frame(root, bg='#ffffff', bd=5)
frame.place(relx=0.5, rely=0.5, anchor='center')

# Header Label
header_label = tk.Label(root, text="Stock Portfolio Manager", font=("Helvetica", 20), bg='lightblue', fg='black')
header_label.pack(side='top', fill='x')

# Load Data Button
load_button = tk.Button(frame, text="Load Stock Data", command=load_file, font=("Helvetica", 14))
load_button.pack(pady=10)

# Button to vizualize 
visualize_button = tk.Button(frame, text="Visualize Portfolio", command=visualize_data, font=("Helvetica", 14))
visualize_button.pack(pady=10)

# Footer Label
footer_label = tk.Label(root, text="Developed by Ahmed Alsharqi - 2024", font=("Helvetica", 10), bg='lightblue', fg='black')
footer_label.pack(side='bottom', fill='x')

# Starting the Tkinter event loop
root.mainloop()
