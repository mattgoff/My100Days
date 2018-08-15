from datetime import datetime

b_friday = datetime(2018, 11, 23, 00, 00, 00)

def count_days():
    t_now = datetime.now()
    cd_days = (b_friday - t_now).days
    cd_hours, remainder = divmod((b_friday - t_now).seconds, 3600)
    cd_minutes, cd_seconds = divmod(remainder, 60)
    print("{} Days, {}:{}:{}".format(cd_days, cd_hours, cd_minutes, cd_seconds))

count_days()
