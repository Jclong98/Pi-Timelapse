import argparse, os, sched, time
from datetime import date, datetime, timedelta

from take_picture import take_picture
from generate_times import generate_times


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", default="./", help="Output directory")

    parser.add_argument("-dY", "--d-years",   type=int, default=0, help="duration in years")
    parser.add_argument("-dH", "--d-hours",   type=int, default=0, help="duration in hours")
    parser.add_argument("-dM", "--d-minutes", type=int, default=0, help="duration in minutes")
    parser.add_argument("-dS", "--d-seconds", type=int, default=0, help="duration in seconds")
    parser.add_argument("-dD", "--d-days",    type=int, default=0, help="duration in day")

    parser.add_argument("-iH", "--i-hours",   type=int, default=0, help="interval in hours")
    parser.add_argument("-iM", "--i-minutes", type=int, default=0, help="interval in minutes")
    parser.add_argument("-iS", "--i-seconds", type=int, default=0, help="interval in seconds")
    parser.add_argument("-iD", "--i-days",    type=int, default=0, help="interval in day")

    args = parser.parse_args()
    return args

def main():

    args = get_args()
    if not os.path.isdir(args.output):
        os.mkdir(args.output)

    start_time = datetime.now()

    duration_dict = {
        "days":    args.d_days,
        "hours":   args.d_hours,
        "minutes": args.d_minutes,
        "seconds": args.d_seconds,
    }
    duration = timedelta(**duration_dict) + timedelta(days=365) * args.d_years
    stop_time = start_time + duration

    # if no duration is given, set it for 100 years
    # I'll die before this program is done running 🤷‍♂️
    if stop_time == start_time:
        stop_time = start_time + timedelta(365) * 100

    interval_dict = {
        "days":    args.i_days,
        "hours":   args.i_hours,
        "minutes": args.i_minutes,
        "seconds": args.i_seconds,
    }

    # if no interval is given, set the default interval to 15 minutes
    if timedelta(seconds=1) > timedelta(**interval_dict):
        interval_dict = {"minutes": 15}

    # starting scheduling
    times = generate_times(
        start_time.timestamp(),
        stop_time.timestamp(),
        interval_dict
    )

    s = sched.scheduler(time.time, time.sleep)

    for i, t in enumerate(times):
        filename = f"{i}.jpg"
        s.enterabs(
            t, 
            0, 
            take_picture, 
            argument=(os.path.join(args.output, filename),)
        )

    print(f"Start Time:     {start_time}")
    print(f"Stop Time:      {stop_time}")
    print(f"Interval:       {timedelta(**interval_dict)}")
    print(f"Total Pictures: {len(times)}")

    s.run()

if __name__ == "__main__":
    main()
