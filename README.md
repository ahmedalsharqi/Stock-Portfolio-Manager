Stock-Portifolio-Manager
This is a simple Stock Portfolio Manager application built in Python. It allows users to import stock data, manage their portfolio, and visualize performance over time through a Tkinter-based GUI. The project includes database integration, data processing, and dynamic chart generation.
=======
Stock Portfolio Manager
Author: Ahmed Alsharqi
Date: 2024-08-22

Project Description
    This project is a Python-based Stock Portfolio Manager that imports stock data from a JSON file, processes the data to calculate the value of each stock holding in a portfolio, stores the data in an SQLite database, and generates a line chart of portfolio values over time using matplotlib. The project also includes a Tkinter GUI, which allows users to interact with the application through a graphical interface.

Features
    Data Import and Processing:
    Imports stock data from a JSON file.
    Processes the data to calculate the value of each stock holding.
    Stores the processed data in an SQLite database.

Data Visualization:
    Generates a line chart of portfolio values over time, with each stock's value displayed as a line on the graph.
    Graphical User Interface (GUI):
    Allows users to load stock data and visualize the portfolio through a Tkinter-based GUI.
    Includes a header, footer, background image, and centered buttons for an engaging user experience.

Installation
    Prerequisites
    Python 3
    The following Python libraries:
    tkinter (usually comes pre-installed with Python)
    PIL (Pillow) for image handling
    pandas
    sqlite3
    matplotlib