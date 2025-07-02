from datetime import datetime, timedelta
def get_date(date_str): 
    try:
        day, month, year = date_str.split("/")
        return datetime(int(year),int(month),int(day))
    except:
        print("Invalid date format!")
        return None


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