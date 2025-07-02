from common.const import months_arr, base_path
import os


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
        timesheet_path =  f"{record_path}/timesheet.txt"
        with open(timesheet_path,"w") as timesheet:
            timesheet.close()
        
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

