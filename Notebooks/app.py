from flask import render_template, request, jsonify,Flask
import flask
import numpy as np
import traceback #allows you to send error to user
import pickle
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
import FeaturesF as fe



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
        # print(json_)

        query = pd.DataFrame(json_)

        
        query = fe.features_5(query)
        
           
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
        variable= jsonify({
               "prediction":str(prediction)
               })
        


        return variable

    except:
           return jsonify({
               "trace": traceback.format_exc()
               })
    
if __name__ == "__main__":
    app.run()