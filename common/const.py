import os
from dotenv import load_dotenv
load_dotenv()
folder_name = os.environ.get("FOLDER_NAME") or "records"
base_path = os.path.join("base", folder_name)


months_arr = [
    "N/A",
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec"
]
