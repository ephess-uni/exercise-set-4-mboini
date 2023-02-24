""" ex_4_3.py """
import os
from datetime import datetime, timedelta

try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def time_between_shutdowns(logfile):

    shutdowns = get_shutdown_events(logfile)

    first_shutdown = shutdowns[0]

    last_shutdown = shutdowns[-1]

    first_shutdown_datetime = logstamp_to_datetime(first_shutdown['date'])

    last_shutdown_datetime = logstamp_to_datetime(last_shutdown['date'])

    time_difference = last_shutdown_datetime - first_shutdown_datetime

    return time_difference


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
