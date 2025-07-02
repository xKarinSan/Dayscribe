from .generate_txt import *
from common.tools import get_date, precompute
def generate_with_fixed_range():
    # start_date_str = input("Start date: (DD/MM/YYYY)")
    start_date_str = "30/6/2025"
    start_date = get_date(start_date_str)
    if not start_date:
        exit()
        
    # end_date_str = input("End date: (DD/MM/YYYY)")
    end_date_str = "1/4/2026"
    end_date = get_date(end_date_str)
    if not end_date:
        exit()
        
    # check if end < start
    if end_date < start_date:
        print("Cannot be ealier than start date")
        exit()
    
    # precomputation
    precomputed_dates = precompute(start_date,end_date)
    create_files(precomputed_dates)
    
    if not precomputed_dates:
        print("Error processing.")
        exit()
        
if __name__ == "__main__":
    generate_with_fixed_range()