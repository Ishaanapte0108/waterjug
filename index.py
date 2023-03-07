from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd, re

def employee_attrition_number(**kwargs):
    
    #check if arguments are equal to 1 or 2
    if len(kwargs) == 0 or len(kwargs) > 2:
        raise TypeError("employee_attrition_number() takes exactly 1 or 2 keyword arguments")
        
    department = kwargs.get('department')
    review_date = kwargs.get('review_date')

    #check if arguments are valid
    if department is None and review_date is None:
        raise TypeError("employee_attrition_number() requires at least one keyword argument")
    
    #check if review_date has been passed
    if not review_date:
        raise TypeError("employee_attrition_number() must be passed a valid date")
      
    #check if given date is quater end date
    try:
      
      dates = review_date.split('-')
      refined = list(map(lambda x: int(re.sub("^0+(?!$)", '', x)),dates))
      a = pd.Timestamp(refined[2], refined[1], refined[0])
      if a.is_quarter_end:
        #subtract three months from review date
        date_obj = datetime.strptime(review_date, "%d-%m-%Y")
        new_date_obj = date_obj - relativedelta(months=3)
        reporting_date = new_date_obj.strftime("%d-%m-%Y")
        print(reporting_date)
      else:
         print('Date is not a quater end date')
         return
      
    except Exception as e:
       print(e)
    
  
employee_attrition_number(department = 'Finance', review_date = '2023-06-30')


