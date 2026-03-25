#  AI-Powered Phishing URL Detection System

## Overview

This project is a simple Machine Learning-based system that helps identify whether a URL is **safe or phishing**. With the rise of fake websites and online scams, the goal of this project is to provide a quick and easy way to check if a link looks suspicious.

Instead of relying on complex tools, this project uses basic URL patterns and a trained model to give instant predictions.

---

##  Features

*  Extracts useful information from URLs (length, symbols, HTTPS, keywords)
*  Uses a Random Forest model for prediction
*  Fast performance using saved model (Pickle)
*  Simple command-line interface
*  Instant result: Safe or Phishing

---

##  How It Works

1. You enter a URL
2. The system breaks it into meaningful features
3. These features are sent to the trained model
4. The model predicts whether the URL is safe or suspicious

---

##  Tech Stack

* Python
* Pandas
* Scikit-learn
* NumPy

---

## Project Structure

phishing-url-detector/
│── main.py
│── model.pkl
│── data.csv
│── requirements.txt
│── README.md

---

##  How to Run

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Run the project:

```
python main.py
```

3. Enter a URL and get the result instantly

---

##  Future Improvements

*  Build a web interface using Flask
*  Use more advanced features for better accuracy
*  Train on a larger dataset
*  Convert into a browser extension

---

##  What I Learned

* Basics of Machine Learning
* How to convert real-world data into features
* Training and using a model
* Saving and loading models using Pickle

---

##  Description

This project shows how Machine Learning can be used in a practical way to detect phishing websites. It focuses on simplicity, speed, and real-world usability, making it a great beginner-friendly project with real impact 

Author 
SOURABH AWASTHI 
