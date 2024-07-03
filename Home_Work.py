from datetime import datetime
def get_days_from_today(date):
    try:
        now_date=datetime.today().date()
        input_date=datetime.strptime(date,"%Y-%m-%d").date()
        return int((input_date - now_date).days)
    except ValueError:
        print("Write date in format year-month-day")
