from flask import render_template, request, jsonify,Flask
import flask
import numpy as np
import traceback #allows you to send error to user
import pickle
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler


def features (df):
                columns_to_drop=['EmployeeID','EmployeeCount','Gender','MonthlyRate','HourlyRate','Over18','PercentSalaryHike','PerformanceRating','RelationshipSatisfaction','StandardHours']
                df.drop(columns=columns_to_drop, inplace=True)
                df['BusinessTravel'] = np.where(df['BusinessTravel'] == 'Travel_Frequently', 1, 0)
                df['Education']= np.where(df['Education'] == 5, 1, 0)
                df['EducationField'] = np.where((df['EducationField'] == "Life Sciences") | (df['EducationField'] == "Medical") | (df['EducationField'] == "Other"), 1, 0)
                df['EnvironmentSatisfaction'] = np.where(df['EnvironmentSatisfaction'] == 1, 1, 0)
                df['JobInvolvement'] = np.where((df['JobInvolvement'] == 1)|(df['JobInvolvement'] == 2), 1, 0)
                df['JobLevel'] = np.where(df['JobLevel'] == 1, 1, np.where(df['JobLevel'] == 2, 2, np.where(df['JobLevel'] == 4, 2, 0)))
                df['JobRole'] = np.where((df['JobRole'] == 'Nurse') | (df['JobRole']== "Other") , 1, 0)
                df['MaritalStatus']= np.where((df['MaritalStatus'] == 'Single'), 1, 0)
                df['Shift']= np.where((df['Shift'] == 0) | (df['Shift']== 3) , 1, 0)
                df['WorkLifeBalance']= np.where(df['WorkLifeBalance'] == 1, 1, 0)
                df['OverTime']= df['OverTime'].replace({'No':0,'Yes':1})
                return df

# App definition
app = Flask(__name__)

# importing models
with open('model.p', 'rb') as f:
   model = pickle.load (f)

with open('columns.p', 'rb') as f:
   model_columns = pickle.load (f)

#webpage

@app.route('/')
def welcome():
   return "Welcome! Use this Flask App for Healthcare Attrition Prediction"

@app.route('/predict', methods=['POST','GET'])
def predict():

   if flask.request.method == 'GET':
       return "Prediction page. Try using post with params to get specific prediction."

   if flask.request.method == 'POST':
       
    try:
        json_ = request.json # '_' since 'json' is a special word
        print(json_)

        query = pd.DataFrame(json_)

        features(query)
           
        # Select numerical and categorical features
        numerical_features = query.select_dtypes(include='number').columns
        categorical_features = query.select_dtypes(include='object').columns

        # Define the column transformer
        preprocessor = ColumnTransformer(
                    transformers=[
                        ('num', StandardScaler(), numerical_features),  # Apply StandardScaler to numerical columns
                        ('cat', OneHotEncoder(), categorical_features),
                    ]
                )

        # Fit and transform the data using the preprocessor
        transformed_data = preprocessor.fit_transform(query)

        # Get the feature names after transformation
        numerical_feature_names = list(numerical_features)
        categorical_feature_names = list(preprocessor.named_transformers_['cat'].get_feature_names_out())
        feature_names = numerical_feature_names + categorical_feature_names

    
        # Convert the transformed data to a DataFrame with column labels
        query = pd.DataFrame(transformed_data, columns=feature_names)

        query = query.reindex(columns = model_columns, fill_value= 0)
               
        prediction = list(model.predict(query))

        return jsonify({
               "prediction":str(prediction)
           })

    except:
           return jsonify({
               "trace": traceback.format_exc()
               })
    
if __name__ == "__main__":
    app.run()