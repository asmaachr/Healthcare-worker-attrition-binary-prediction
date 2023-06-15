## Python test file for flask to test locally
import requests as r
import pandas as pd
import json

base_url = 'http://127.0.0.1:5000/' #base url local host

json_ = [
    {
    "EmployeeID" : 1699288,
    "Age" : 30,
    "BusinessTravel" : "Travel_Rarely",
    "DailyRate" : 1358,
    "Department" : "Maternity",
    "DistanceFromHome" : 24,
    "Education" : 1,
    "EducationField" : "Life Sciences",
    "EmployeeCount" : 1,
    "EnvironmentSatisfaction" :4,
    "Gender" : "Male",
    "HourlyRate" : 67,
    "JobInvolvement" : 3,
    "JobLevel": 1,
    "JobRole" : "Nurse",
    "JobSatisfaction" : 3,
    "MaritalStatus" : "Divorced",
    "MonthlyIncome" : 2693,
    "MonthlyRate" : 13335,
    "NumCompaniesWorked" : 1,
    "Over18" : "Y",
    "OverTime" : "No",
    "PercentSalaryHike" : 22,
    "PerformanceRating" : 4,
    "RelationshipSatisfaction" : 2,
    "StandardHours"  : 80,
    "Shift" : 1,
    "TotalWorkingYears" : 1,
    "TrainingTimesLastYear" : 2,
    "WorkLifeBalance" : 3,
    "YearsAtCompany" : 1,
    "YearsInCurrentRole" : 0,
    "YearsSinceLastPromotion" : 0,
    "YearsWithCurrManager" :0,

       }
]



# Get Response
# response = r.get(base_url)
response = r.post(base_url + "predict", json = json_)


if response.status_code == 200:
    print('...')
    print('request successful')
    print('...')
    print(response.json())
else:
    print(response.json())
    print('request failed')
