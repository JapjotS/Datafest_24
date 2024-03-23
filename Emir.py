## confidence score
import pandas as pd
import numpy as np

##just take the student_id construct, response  and respone column
df = pd.read_csv('Random Sample of Data Files_03_04/checkpoints_eoc.csv')
df = df[['student_id', 'response', 'correct']]

#filter the construct for just the values of "expectancy" and "Course cost"

df = df[df['construct'].isin(['expectancy', 'course_cost'])]
#disregard the NA values
df.dropna(inplace=True)




