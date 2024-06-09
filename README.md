# Heart Disease Prediction App

This project is a desktop application developed to predict heart disease using the Tkinter library for the GUI and MySQL for the database.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Database Setup](#database-setup)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The Heart Disease Prediction App is designed to provide a simple interface for predicting the likelihood of heart disease based on user input. The application uses a machine learning model trained on a dataset of heart disease indicators and employs Tkinter for the graphical user interface and MySQL for data storage and management.

## Features
- User-friendly interface created with Tkinter.
- Prediction of heart disease based on input parameters.
- Storage of user data and prediction results in a MySQL database.
- Easy to set up and use.

## Requirements
- Python 3.x
- Tkinter
- MySQL Server
- MySQL Connector for Python
- scikit-learn (for the machine learning model)
- pandas (for data handling)

## Installation
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/LawalIbraheem19/heart-disease-prediction-app.git
    cd heart-disease-prediction-app
    ```

2. **Install Required Python Packages**:
    ```bash
    pip install tkinter mysql-connector-python scikit-learn pandas
    ```

3. **Set Up MySQL Database**:
    Follow the instructions in the [Database Setup](#database-setup) section to set up your MySQL database.

## Usage
1. **Run the Application**:
    ```bash
    python app.py
    ```

2. **Use the Interface**:
    - Enter the required medical parameters.
    - Click on the "Predict" button to get the prediction results.
    - The results will be displayed on the screen and saved in the MySQL database.

## Database Setup
1. **Start MySQL Server** and log in:
    ```bash
    mysql -u root -p
    ```

2. **Create Database**:
    ```sql
    CREATE DATABASE heart_disease_db;
    ```

3. **Create User** (optional but recommended):
    ```sql
    CREATE USER 'app_user'@'localhost' IDENTIFIED BY 'your_password';
    GRANT ALL PRIVILEGES ON heart_disease_db.* TO 'app_user'@'localhost';
    FLUSH PRIVILEGES;
    ```

4. **Create Table**:
    ```sql
    USE heart_disease_db;

    CREATE TABLE predictions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        age INT,
        sex INT,
        cp INT,
        trestbps INT,
        chol INT,
        fbs INT,
        restecg INT,
        thalach INT,
        exang INT,
        oldpeak FLOAT,
        slope INT,
        ca INT,
        thal INT,
        prediction INT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    ```

5. **Update Database Configuration** in your `app.py`:
    ```python
    import mysql.connector

    db = mysql.connector.connect(
        host="localhost",
        user="app_user",
        password="your_password",
        database="heart_disease_db"
    )
    ```

## Contributing
Contributions are welcome! Please create an issue or submit a pull request for any changes or enhancements.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
