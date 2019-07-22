#sudo pip3 install pandas
import pandas as pd
import numpy as np 
salary_data = pd.read_csv("salary_data.csv") 

salary_data['Hours Worked'] = salary_data['Hours Worked'].str.replace("$", "")

salary_dict = {}

for row in salary_data: 
	employee = salary_data["Name"]
	if salary_data['Hours Worked'] <= 40: 
		salary = salary_data['Pay Rate'] * salary_data['Hours Worked']
	else:
		salary = (salary_data['Pay Rate'] * 40) + ((salary_data['Hours Worked'] -40) * (salary_data['Pay Rate'] * 1.5))
	salary_dict.update({employee : salary})
	
print(salary_dict)