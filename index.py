# from datetime import datetime
# from dateutil.relativedelta import relativedelta
# import pandas as pd, re
# import frappe

# def employee_attribution_number(**kwargs):
    
#     #check if arguments are equal to 1 or 2
#     if len(kwargs) == 0 or len(kwargs) > 2:
#         raise TypeError("employee_attrition_number() takes exactly 1 or 2 keyword arguments")
        
#     department = kwargs.get('department')
#     review_date = kwargs.get('review_date')

#     #check if arguments are valid
#     if department is None and review_date is None:
#         raise TypeError("employee_attrition_number() requires at least one keyword argument")
    
#     #check if review_date has been passed
#     if not review_date:
#         raise TypeError("employee_attrition_number() must be passed a valid date")
    
#     if department:
#        queryWord = department
#     else:
#        queryWord = 'Company'

#     #check if given date is quater end date
#     #review and reporting date are assumed to be synonymous
#     try:
      
#       dates = review_date.split('-')
#       refined = list(map(lambda x: int(re.sub("^0+(?!$)", '', x)),dates))
#       a = pd.Timestamp(refined[0], refined[1], refined[2])
#       if a.is_quarter_end:
#         #subtract three months from review date
#         begin_date = a - pd.offsets.QuarterEnd()
#         begin_date = begin_date.strftime("%Y-%m-%d")

#       else:
#          raise TypeError("employee_attrition_number() must be passed a quater end date only")
      
#       #   obtain employee strngth at period begin and period end
#       k = frappe.db.sql(f"SELECT period_begin_team_size, period_end_team_size, employee_leaving, name FROM `tabEmployee Attrition` where reporting_date = '{review_date}' and {'department' if department else 'level'} = '{queryWord}'")
      
#       period_begin_team_size = k[0][0]
#       period_end_team_size = k[0][1]
#       employees_who_left = k[0][2]
#       name = k[0][3]
#       deleteQuery = f"DELETE FROM `tabEmployee Attrition` where name = '{name}'"
#       addQuery = f"INSERT INTO employee_attribution_number (name,begin_period_date,period_begin_team_size,period_end_team_size,employees_who_left,updated_by) values ('{name}', '{begin_date}', '{period_begin_team_size}', '{period_end_team_size}', '{employees_who_left}', 'Ishaan')"

#       result = {
#          "name": name,
#          "Begin period date": begin_date,
#          "Employee strength at period beginnin": period_begin_team_size,
#          "Employee strength at period end": period_end_team_size,
#          "Number of employees who left": employees_who_left,
#          "Delete query": deleteQuery,
#          "Add Query": addQuery
#       }
#       return result

#     except Exception as e:
#        print(e)


# def updateAttritionTables(addQuery, deleteQuery):
  
#   #create table if not exists
#   frappe.db.sql("CREATE TABLE IF NOT EXISTS employee_attribution_number (name VARCHAR(50), begin_period_date VARCHAR(10), period_begin_team_size VARCHAR(10), period_end_team_size VARCHAR(10), employees_who_left VARCHAR(10), updated_by VARCHAR(50));")
#   # #delete query
#   # frappe.db.sql(deleteQuery)
#   #add query
#   frappe.db.sql("INSERT INTO employee_attribution_number (name,begin_period_date,period_begin_team_size,period_end_team_size,employees_who_left,updated_by) values ('EA_2023-06-30_Company2', '2023-03-31', '12', '10', '2', 'Ishaan')")

# # example input 
# # employee_attribution_number(department = 'Dispatch', review_date = '2023-03-31')
# # employee_attribution_number(review_date = '2023-03-31')
# # updateAttritionTables(addQuery, deleteQuery)

# import frappe

# def getEmployeeAttrition():
# 		# def records(row):
# 		# 	pass
# 		# try:
      
# 		# 	dates = reporting_date.split('-')
# 		# 	refined = list(map(lambda x: int(re.sub("^0+(?!$)", '', x)),dates))
# 		# 	a = pd.Timestamp(refined[0], refined[1], refined[2])
			
# 		# 	if a.is_quarter_end:
# 		# 		# get previous quater end date
# 		# 		begin_date = a - pd.offsets.QuarterEnd()
# 		# 		begin_date = begin_date.strftime("%Y-%m-%d")
# 		# 		#get period begin team size, period end team size and employee leaving
# 		# 		data = frappe.db.sql(f"SELECT department,COUNT(CASE WHEN status = 'active' and date_of_joining <='{begin_date}' THEN 1 ELSE NULL END) AS 'Period Begin Team Size',COUNT(CASE WHEN status = 'active' and date_of_joining <='{reporting_date}' THEN 1 ELSE NULL END) AS 'Period End Team Size',COUNT(CASE WHEN status = 'left' and relieving_date > '{begin_date}' and relieving_date <= '{reporting_date}' THEN 1 ELSE NULL END) AS 'Employees Leaving' FROM `tabEmployee` GROUP BY department;")
# 		# 		#put receieved data into pandas dataframe for further processing
# 		# 		df = pd.DataFrame(data, columns=['Department', 'Period Begin Team Size', 'Period End Team size', 'Employee Leaving'])
# 		# 		#calculate the total
# 		# 		company_row = pd.DataFrame(df.sum(axis = 0), columns=['Company']).T
# 		# 		company_row['Department'] = 'Company'
# 		# 		df = df.append(company_row, ignore_index = True)
# 		# 		df.apply(records, axis = 1)
# 		# 		print(df)
		
# 		# except Exception as e:
# 		# 	print(e)

# 		#insert a new doc
# 		try:
# 			# user = frappe.get_doc(doctype='Employee Attrition', level = 'Department', department = 'Dispatch',reporting_date = '2023-03-31', period_begin_team_size = 56, period_end_team_size = 50, employee_leaving = 6)
# 			# user.insert()
# 			# user.save()
# 			doc = frappe.new_doc('Employee Attrition')
# 			doc.level = 'Department'
# 			doc.department = 'Dispatch'
# 			doc.reporting_date = '2023-03-31'
# 			doc.period_begin_team_size = 56
# 			doc.period_end_team_size = 50
# 			doc.employee_leaving = 6
# 			doc.insert()			
# 		except Exception as e:
# 			print(e)