from datetime import datetime
from common.const import base_path, months_arr
import os

def clock():
    current_date = datetime.now()
    # get the year month
    day = current_date.day
    month = current_date.month
    year = current_date.year
    
    hour_minute = current_date.strftime("%H:%M:%S")
    year_month = f"{months_arr[month]} {year}"
    day_string = f"{day}/{month}/{year}"
    
    record_path = f"{base_path}/{year_month}"
    os.makedirs(record_path, exist_ok=True)
    timesheet_path = os.path.join(record_path, "timesheet.txt")

    if not os.path.exists(timesheet_path):
        clock_in = input('Type "Y" to clock in. Anything else to cancel: ')
        if clock_in.lower() != "y":
            return
        with open(timesheet_path, "w") as f:
            f.write(f"{day_string} {hour_minute}\n")
        print("Clock-in recorded (new file).")
        return
    
    clock_out = input('Type "Y" to clock out. Anything else to cancel: ')
    if clock_out.lower() != "y":
        return
    
    with open(timesheet_path, "r") as f:
        lines = f.readlines()
        
    updated = False
    with open(timesheet_path, "w") as f:
        for line in lines:
            if line.startswith(day_string):
                if '-' not in line:
                    line = line.strip() + f"-{hour_minute}\n"
                    print("Clock-out recorded.")
                    updated = True
            f.write(line)
            
        if not updated:
            f.write(f"{day_string} {hour_minute}\n")
            print("Clock-in recorded (new entry).")
        
    


if __name__ == "__main__":
    clock()