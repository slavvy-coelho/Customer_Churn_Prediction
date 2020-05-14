Overview:
Churn rate, in its broadest sense, is a measure of the decline in the amount of users using
a certain service over a specific period. It is one of the major factors that determine the
steady-state level of customers a business will support.
In this project, we aim to work on the KKBOX, Asia’s leading music service dataset to
analyze the data, determine the factors that will affect the churning of the uses, and finally
predict the user churn behavior. These insights can be helpful to make efforts towards
customer retention.
We also intend on extending the problem statement to perform sentiment analysis to
predict churn based on user reviews about their experience with the service.

Data:
xtrain.csv: user id and is_churn(Whether the user has churned)
members.csv: user information like city, birthdate, gender, registration details,
service expiration details
transcation.csv: payment method details, plan details, price, auto_renewal value
user_logs.csv: Details of the users service usage (Number of songs played and
the amount of time the service was used)
reviews.csv: Customer reviews about the service

Technology Stack:
Numpy, pandas, seaborn, matplotlib, TextBlob(NLP)



1) EDA

Telco.ipynb
Data: members_v3.csv, transactions.csv, user_logs_v2.csv, train.csv
source: https://www.kaggle.com/c/kkbox-churn-prediction-challenge/data

2) Prediction

TelcoPrediction.ipynb
Data: members_v3.csv, transactions.csv, user_logs_v2.csv, train.csv
source: https://www.kaggle.com/c/kkbox-churn-prediction-challenge/data

3) Recommendation

Recommendation.ipynb
Data: Polarity.csv, -10to-5.csv, -5to0.csv, 0to5.csv, 5to10.csv
source: Uploaded on git

4) Spark Implementation

spark.ipynb
Data: final.csv
source: Created by TelcoPrediction.ipynb

5) Front End for Prediction

app.py
Data: final.csv
source: Created by TelcoPrediction.ipynb
(Include corresponding index.html file in a folder called templates and style.css file in a folder static/css along with the image okay.jpg )

6) Front End for Recommendation

demo.py
Data: Polarity.csv, -10to-5.csv, -5to0.csv, 0to5.csv, 5to10.csv
source: Uploaded on git
(Include corresponding index.html file in a folder called templates and style.css file in a folder static/css along with the image okay.jpg )
