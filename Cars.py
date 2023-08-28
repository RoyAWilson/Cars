'''
Foloow along with Pandas Tutorial on Youtube using a cars dataset sourced at Kaggle.

'''

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

# Read in the dataset.
car_Data = pd.read_csv('./Data/car details v4.csv')
ColNames = car_Data.columns
car_Data2 = car_Data.rename(columns = {
    'Fuel Type':'Fuel_Type', 'Seller Type':'Seller_Type','Max Power':'Max_Power', 'Max Torque':'Max_Torque',
    'Seating Capacity':"Seating", 'Fuel Tank Capacity':'Max_Fuel'
    }
)
# Deal with missing values: 1. Drop those values and 2 impute those values:
# Drop values:
car_Data_Drop_Null = car_Data.dropna(how = 'any')
# how = any - removes rows where any field has a null value, however how = all will only reomve
# null records.  Important distinction.

car_Data_Drop_Null.isnull().sum()

# 2. Impute Values:

Eng_Mode = car_Data2['Engine'].mode()
car_Data2['Engine'] = car_Data2['Engine'].fillna(str(car_Data2['Engine'].mode()))
car_Data2['Max_Power'] = car_Data2['Max_Power'].fillna(str(car_Data2['Max_Power'].mode()))
car_Data2['Max_Torque'] = car_Data2['Max_Torque'].fillna(str(car_Data2['Max_Torque'].mode()))
car_Data2['Drivetrain'] = car_Data2['Drivetrain'].fillna(str(car_Data2['Drivetrain'].mode()))
car_Data2['Length'] = car_Data2['Length'].fillna(str(car_Data2['Length'].mode()))
car_Data2['Width'] = car_Data2['Width'].fillna(str(car_Data2['Width'].mode()))
car_Data2['Height'] = car_Data2['Height'].fillna(str(car_Data2['Height'].mode()))
car_Data2['Max_Fuel'] = car_Data2['Max_Fuel'].fillna(str(car_Data2['Max_Fuel'].mean()))
car_Data2['Seating'] = car_Data2['Seating'].fillna(str(car_Data2['Seating'].mode()))