import pandas as pd
import numpy as np




def features_1 (df):
    columns_to_drop=['EmployeeID','EmployeeCount','Over18','StandardHours']
    df.drop(columns=columns_to_drop, inplace=True)
    df['JobRole']= df['JobRole'].replace({'Administrative':'Admin'})
    df['Shift'] = df['Shift'].astype('str')
    df['Education'] = df['Education'].astype('str')
    return df




def features_2 (df):
    columns_to_drop=['EmployeeID','EmployeeCount','Over18','PercentSalaryHike','PerformanceRating','HourlyRate','StandardHours']
    df.drop(columns=columns_to_drop, inplace=True)
    df['JobRole']= df['JobRole'].replace({'Administrative':'Admin'})
    df['Shift'] = df['Shift'].astype('str')
    df['Education'] = df['Education'].astype('str')
    return df


def features_3 (df):
    columns_to_drop=['EmployeeID','EmployeeCount','Gender','Over18','PercentSalaryHike','PerformanceRating','HourlyRate','MonthlyRate','StandardHours','YearsSinceLastPromotion']
    df.drop(columns=columns_to_drop, inplace=True)
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



def features_4 (df):
    columns_to_drop=['EmployeeID','EmployeeCount','Gender','MonthlyRate','HourlyRate','Over18','PercentSalaryHike','PerformanceRating','RelationshipSatisfaction','StandardHours']
    df.drop(columns=columns_to_drop, inplace=True)
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












def features_4 (df):
    columns_to_drop=['EmployeeID','EmployeeCount','Gender','Over18','PercentSalaryHike','PerformanceRating','RelationshipSatisfaction','StandardHours']
    df.drop(columns=columns_to_drop, inplace=True)
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