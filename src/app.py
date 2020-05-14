import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
# Load libraries
import pandas as pd
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics #Import scikit-learn metrics module for accuracy calculation

app = Flask(__name__)
model = pickle.load(open('model_red.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    final = pd.read_csv("final.csv")

    feature_cols = ["bd","num_unq","total_secs"]
    X = final[feature_cols] # Features
    y = final.is_churn # Target variable

# Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% test


    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    # print(final_features)
    # print(type(final_features))    
    data = {'bd' : [final_features[0][0]], 'num_unq' : [final_features[0][1]] , 'total_secs' : [final_features[0][2]]}
    df = pd.DataFrame(data)
    print(df)
    print(type(df))
    prediction = model.predict(df)
    print(prediction)
    final = prediction[0]

    if final == 1:
        return render_template('index.html', prediction_text='User will Churn :(')
    else:
        return render_template('index.html', prediction_text="User won't Churn! Yayy")

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)