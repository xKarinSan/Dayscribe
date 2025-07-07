from agents import Agent, Runner, function_tool
from src.scribe.generate_txt import generate_at_date
from src.timesheet.tools import clock_in_out
from datetime import datetime, timedelta

@function_tool
def generate_from_keyword(day_keyword: str):
    """
    Generate a log file based on a relative date keyword.

    - Accepts: "today", "tomorrow", or "yesterday"
    - Converts to a specific date and creates a daily log file.
    """
    now = datetime.now()

    keyword = day_keyword.lower().strip()
    if keyword == "today":
        target_date = now
    elif keyword == "tomorrow":
        target_date = now + timedelta(days=1)
    elif keyword == "yesterday":
        target_date = now - timedelta(days=1)
    else:
        print("Invalid keyword. Please use 'today', 'tomorrow', or 'yesterday'.")
        return

    generate_at_date(target_date.year, target_date.month, target_date.day)

agent = Agent(
    name="Main Assistant",
    instructions="""
        You are a helpful assistant. Based on the user's input, decide whether to:
        - Clock in or clock out for today.
        - Generate a daily log template for a specific date (including 'today', 'yesterday', or 'tomorrow').
        - Write or update something in a log (if supported).
        - Retrieve or view past entries (if supported).

        Choose the appropriate function tool based on the user's intent and the parameters provided.
        
        IMPORTANT:
        - When calling a function tool, your response **must be the exact string returned by the tool**.
        - Do not rephrase, interpret, summarize, or modify the tool’s response.
        - If the tool returns a message, return it as-is to the user.
    """,
    model = "o3-mini",
    tools = [generate_from_keyword, generate_at_date, clock_in_out]
)

def main():
    while True:
        command = input("Please say something: ")
        res = Runner.run_sync(agent,command)
        print("res",res)
        print(res.final_output)
        print(res.raw_responses)
        to_continue = input("Do you still want to continue?(Type y to continue, anything else to stop.)").lower()
        if to_continue != "y":
            break

if __name__ == "__main__":
    main()

