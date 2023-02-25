""" ex_4_3.py """
import os

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


from datetime import timedelta

def time_between_shutdowns(logfile):
    events = get_shutdown_events(logfile)
    if len(events) >= 2:
        last_shutdown = logstamp_to_datetime(events[-1])
        prev_shutdown = logstamp_to_datetime(events[-2])
        return last_shutdown - prev_shutdown
    else:
        return timedelta()



# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')
