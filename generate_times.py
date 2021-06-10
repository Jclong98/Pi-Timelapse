from datetime import datetime, timedelta

def generate_times(start_time:float, stop_time:float, interval:dict={ "minutes": 15 }) -> list:
    """
    Returns a list of times in unix timestamp format

    Parameters:
        start_time (float): a unix time to start from
        stop_time (float): a unix time to stop at
        interval (dict): a dictionary of kwargs to pass into a timedelta object
            default: { "minutes": 15 }

    Returns:
        times (list<float>): list of unix timestamps separated by an interval

    """

    times = []
    
    current_time = datetime.fromtimestamp(start_time)
    while current_time < datetime.fromtimestamp(stop_time):
        times.append(current_time.timestamp())
        current_time += timedelta(**interval)

    return times

if __name__ == "__main__":
    start_time = datetime.now()
    stop_time = start_time + timedelta(minutes=3)
    interval = {
        "hours": 0,
        "minutes": 0,
        "seconds": 30
    }

    times = generate_times(
        start_time.timestamp(), 
        stop_time.timestamp(), 
        interval
    )
    for t in times:
        print(datetime.fromtimestamp(t))