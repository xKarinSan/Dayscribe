from datetime import datetime, timedelta
from const import months_arr, base_path
import os

def precompute(start_date: datetime,end_date:datetime):
    try:
        delta = end_date - start_date
        all_dates = []
        for i in range(delta.days + 1):
            current_date = start_date + timedelta(days=i)
            if current_date.weekday() < 5:
                all_dates.append(current_date)
        return all_dates        
    except:
        return None

def create_files(precomputed_dates):
    if not precomputed_dates:
        return
    year_month_dict = {
        
    }
    for current_date in precomputed_dates:
        day = current_date.day
        month = current_date.month
        year = current_date.year
        
        year_month = f"{months_arr[month]} {year}"
        year_month_dict[year_month] = year_month_dict.get(year_month,[])
        year_month_dict[year_month].append(f"{year}.{month}.{day}")
    
    for year_month in year_month_dict:
        record_path = f"{base_path}/{year_month}"
        os.makedirs(record_path, exist_ok=True)
        for date_str in year_month_dict[year_month]:
            txt_path = f"{record_path}/{date_str}.txt"
            with open(txt_path,"w") as file:
                file.write(
                    "Done:\n"
                    " - accomplishment1\n"
                    " - accomplishment2\n"
                    " - accomplishment3\n\n"
                    "To Do:\n"
                    " - task1\n"
                    " - task2\n"
                    " - task3\n"
                )    

def get_date(date_str): 
    try:
        day, month, year = date_str.split("/")
        return datetime(int(year),int(month),int(day))
    except:
        print("Invalid date format!")
        return None
