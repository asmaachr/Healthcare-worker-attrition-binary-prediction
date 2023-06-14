import pandas as pd
import numpy as np

def features (df):
    df['BusinessTravel'] = df['BusinessTravel'].apply(lambda x:1 if x == 'Travel_Frequently' else 0)
    df['Education'] = df['Education'].apply(lambda x:1 if x == 5 else 0)
    df['EducationField'] = df['EducationField'].apply(lambda x: 1 if x in ["Life Sciences", "Medical", "Other"] else 0)
    df['EnvironmentSatisfaction'] = df['EnvironmentSatisfaction'].apply(lambda x: 1 if x == 1 else 0)
    df['JobInvolvement'] = df['JobInvolvement'].apply(lambda x: 1 if x in [1, 2] else 0)
    df['JobLevel'] = df['JobLevel'].apply(lambda x: 1 if x == 1 else (2 if x == 2 or x == 4 else 0))
    df['JobRole'] = df['JobRole'].apply(lambda x: 1 if x in ['Nurse', 'Other'] else 0)
    df['MaritalStatus'] = df['MaritalStatus'].apply(lambda x: 1 if x == 'Single' else 0)
    df['Shift'] = df['Shift'].apply(lambda x: 1 if x in [0, 3] else 0)
    df['WorkLifeBalance'] = df['WorkLifeBalance'].apply(lambda x: 1 if x == 1 else 0)
    df['OverTime']= df['OverTime'].replace({'No':0,'Yes':1})
    return df