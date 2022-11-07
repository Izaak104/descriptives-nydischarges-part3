##import libraries
import pandas as pd
import numpy as np

##uploading the data
df = pd.read_csv('Hospital_Inpatient_Discharges__SPARCS_De-Identified___2016.csv')
df

##see columns
df.columns

##cleanup the columns
df.columns = df.columns.str.replace('[^A-Za-z0-9]+', '_')

##changing column names to all caps
df.columns = df.columns.str.upper()
df.columns

##counting the number of columns
df.shape

#keep chosen columns
hospital_data = df[['FACILITY_ID', 'FACILITY_NAME', 'TOTAL_CHARGES', 'TOTAL_COSTS', 'GENDER']]
hospital_data

##drop empty rows
hospital_data.dropna(inplace=True)
hospital_data

##check data types in the columns
hospital_data.dtypes

##changing datatypes
hospital_data['FACILITY_ID'] = hospital_data['FACILITY_ID'].astype('int')
hospital_data['FACILITY_NAME'] = hospital_data['FACILITY_NAME'].astype('category')
hospital_data['GENDER'] = hospital_data['GENDER'].astype('category')

##copy clean data to folder
hospital_data.to_csv('cleaned_data/new_data.csv')
