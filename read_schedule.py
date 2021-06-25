import json
from datetime import datetime, timedelta

def parse_time(time_string:str) -> timedelta:
    """
    Take a string formatted like "%H:%M:%S" and return a timedelta object
    """
    dt = datetime.strptime(time_string, "%H:%M:%S")
    td = timedelta(hours=dt.hour, minutes=dt.minute, seconds=dt.second)
    return td


def read_schedule(path:str) -> list[datetime]:
    """
    reads a json file with the following structure:

    {
        {
            "duration": {
                "years": 1,
                "days": 0
            },
            "times": [
                "08:00:00",
                "12:00:00",
                "16:00:00",
                "20:00:00"
            ]
        }
    }

    Returns a list of times in unix timestamp format

    """
    with open(path) as f:
        schedule = json.load(f)

    start = datetime.now()
    # getting beginning of day
    start = start.replace(hour=0, minute=0, second=0)

    duration_dict = schedule['duration']
    years = duration_dict.pop('years')
    duration = timedelta(**duration_dict) + timedelta(days=365) * years
    stop = start + duration

    total_days = (stop - start).days

    times_of_day = schedule['times']
    times_of_day = [parse_time(t) for t in times_of_day]

    times = []
    for day_num in range(total_days):
        for t in times_of_day:
            times.append((start + timedelta(days=day_num) + t).timestamp())

    return times

if __name__ == "__main__":
    import argparse
    from pprint import pprint

    parser = argparse.ArgumentParser()
    parser.add_argument("path")

    args = parser.parse_args()

    times = read_schedule(args.path)
    for i, t in enumerate(times):
        print(i, t.strftime("%Y-%m-%d %I:%M:%S %p"))