import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report
import joblib

df = pd.read_csv("weatherDataset.csv")

X = df.drop('RainTomorrow',axis=1)
y = df['RainTomorrow']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)

model = GaussianNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy: ",accuracy_score(y_test, y_pred))
print(classification_report(y_test,y_pred))

sample = [[13.4, 22.1, 0.0, 65.0, 48.0, 0]]   
pred = model.predict(sample)
print("Will it rain tomorrow? ", "Yes" if pred[0]==1 else "No")

joblib.dump(model, 'NBTmodel.joblib')



'''
Accuracy:  0.8012674921239651


              precision    recall  f1-score   support

         0.0       0.85      0.90      0.88     21295
         1.0       0.56      0.46      0.50      6003

    accuracy                           0.80     27298
   macro avg       0.71      0.68      0.69     27298
weighted avg       0.79      0.80      0.79     27298
'''