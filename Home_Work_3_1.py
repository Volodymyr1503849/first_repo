from datetime import datetime
def get_days_from_today(date):
    try:
        now_date=datetime.today().date()
        input_date=datetime.strptime(date,"%Y-%m-%d").date()
        return f"Залишилось днів : {int((input_date - now_date).days)}"
    except ValueError:
        print("Write date in format year-month-day")
print(get_days_from_today("2024-12-12"))