from datetime import datetime
import pytz
import dateutil.parser

def reformat_datetime(alerttime):
    """
    Reformat of datetime to humand readable.
    """
    time_tam = dateutil.parser.parse(alerttime)
    data_time = time_tam.strftime('%Y-%m-%d %H:%M:%S')
    datatime = datetime.strptime(data_time, '%Y-%m-%d %H:%M:%S')
    utc = pytz.timezone('UTC')
    localtz = pytz.timezone('Asia/Ho_Chi_Minh')
    utctime = utc.localize(datatime)
    data = localtz.normalize(utctime.astimezone(localtz))
    timedate = data.strftime('%Y-%m-%d %H:%M:%S')
    return timedate

a = reformat_datetime('2022-09-29T03:00:23.606Z')
print(a)
print(type(a))




def reformat_datetime(alerttime):
    """
    Reformat of datetime to humand readable.
    """
    time_tam = dateutil.parser.parse(alerttime)
    data_time = time_tam.strftime('%Y-%m-%d %H:%M:%S')
    datatime = datetime.strptime(data_time, '%Y-%m-%d %H:%M:%S')
    utc = pytz.timezone('UTC')
    localtz = pytz.timezone('Asia/Ho_Chi_Minh')
    utctime = utc.localize(datatime)
    data = localtz.normalize(utctime.astimezone(localtz))
    time = data.strftime('%Y-%m-%d %H:%M:%S')
    return time

reformat_datetime('2022-09-29T03:00:23.606Z')

def reformat(datetime):
    """
    Reformat of datetime to humand readable.
    """
    datetime = datetime.split('T')
    date = datetime[0]
    time = datetime[1].split('.')[0]
    print(date)
    print(type(date))
    print(time)
    print(type(time))
    return date + " " + time

reformat('2022-09-29T03:00:23.606Z')
