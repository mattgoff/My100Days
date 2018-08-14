'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''
from datetime import datetime
import os
import urllib.request
import pdb

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = 'log'
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()

def convert_to_datetime(line):
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object. 
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''
    dateTimeText = (line.split(" "))[1]
    dto = datetime.strptime(dateTimeText, '%Y-%m-%dT%H:%M:%S')
    return dto
    

def time_between_shutdowns(loglines):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the 
       timedelta between the first and last one. 
       Return this datetime.timedelta object.'''
    shut_downs = [line for line in loglines if SHUTDOWN_EVENT in line]
    shut_down_time = [convert_to_datetime(event) for event in shut_downs]
    return (max(shut_down_time) - min(shut_down_time))


print(time_between_shutdowns(loglines))

