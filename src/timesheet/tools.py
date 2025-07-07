from datetime import datetime
from ..common.const import base_path, months_arr
from agents import function_tool

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
    
    
    with open(timesheet_path, "r") as f:
        lines = f.readlines()
        
    updated = False
    with open(timesheet_path, "w") as f:
        for line in lines:
            if line.startswith(day_string):
                if '-' not in line:
                    clock_out = input('Type "Y" to clock out. Anything else to cancel: ')
                    if clock_out.lower() != "y":
                        return
                    line = line.strip() + f"-{hour_minute}\n"
                    print("Clock-out recorded.")
                    updated = True
            f.write(line)
            
        if not updated:
            clock_in = input('Type "Y" to clock in. Anything else to cancel: ')
            if clock_in.lower() != "y":
                return
            f.write(f"{day_string} {hour_minute}\n")
            print("Clock-in recorded (new entry).")
        
    
# =============== AGENT TEST
@function_tool
def clock_in_out(clock_in:bool):
    """
    Clock the user in or out for today.
    - If it's the user's first action today:
        • Accepts clock-in, creates the file if needed.
        • Rejects clock-out (no prior clock-in).
    - If already clocked in today:
        • Rejects duplicate clock-in.
        • Accepts clock-out and updates the same line.
    - If already clocked out:
        • Rejects additional clock-out.
    """
    
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
        if not clock_in:
            return "[timesheet dont exist] Cannot clock in"
        with open(timesheet_path, "w") as f:
            f.write(f"{day_string} {hour_minute}\n")
        return "[timesheet dont exist] Clock-in recorded (new file)."
    
    with open(timesheet_path, "r") as f:
        lines = f.readlines()
        
    updated = False
    with open(timesheet_path, "w") as f:
        for line in lines:
            if line.startswith(day_string):
                if '-' not in line:
                    if clock_in:
                        return "[timesheet exist] Cannot clock out"
                    line = line.strip() + f"-{hour_minute}\n"
                    updated = True
            f.write(line)
        if updated:
            return "[timesheet exist] Clock-out recorded."

        if not clock_in:
            return "[timesheet exist] Cannot clock in"
        f.write(f"{day_string} {hour_minute}\n")
        return "[timesheet exist] Clock-in recorded (new entry)."

if __name__ == "__main__":
    clock()