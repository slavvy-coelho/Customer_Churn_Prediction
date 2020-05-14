from flask import Flask, render_template, request
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    output = 2
    return render_template('index.html')

@app.route('/',methods=['POST'])
def getvalue():
    new = pd.read_csv('polarity.csv')
    new['ID'] = new['ID'].astype(str)
    uid = request.form['uid']
    pos = new.loc[new['ID'] == uid, 'polarity']
    pol = float(pos.values[0])
    if -1.0 <= pol <= -0.5:
        rec = pd.read_csv('-10to-5.csv')
        #print("You generally like songs with polarity ", pol)
        #print("Here's a list recommended for you: ")
        df1 = rec[['Song Name','Artist Name']]

    if -0.5 <= pol <= 0.00:
        rec = pd.read_csv('-5to0.csv')
        #print("You generally like songs with polarity ", pol)
        #print("Here's a list recommended for you: ")
        df1 = rec[['Song Name','Artist Name']]

    if 0.0 <= pol <= 0.5:
        rec = pd.read_csv('0to5.csv')
        #print("You generally like songs with polarity ", pol)
        #print("Here's a list recommended for you: ")
        df1 = rec[['Song Name','Artist Name']]
    if 0.5 <= pol <= 1.00:
        rec = pd.read_csv('5to10.csv')
        #print("You generally like songs with polarity ", pol)
        #print("Here's a list recommended for you: ")
        df1 = rec[['Song Name','Artist Name']]

    return ((df1).to_string())

if __name__ == "__main__":
    app.run(debug=True)