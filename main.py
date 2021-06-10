import argparse, os, sched, time
from datetime import datetime, timedelta

from take_picture import take_picture
from generate_times import generate_times


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", default="./", help="Output directory")
    
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

    duration = {
        "days":    args.d_days,
        "hours":   args.d_hours,
        "minutes": args.d_minutes,
        "seconds": args.d_seconds,
    }

    interval = {
        "days":    args.i_days,
        "hours":   args.i_hours,
        "minutes": args.i_minutes,
        "seconds": args.i_seconds,
    }

    start_time = datetime.now()
    stop_time = start_time + timedelta(**duration)
    
    times = generate_times(
        start_time.timestamp(),
        stop_time.timestamp(),
        interval
    )

    s = sched.scheduler(time.time, time.sleep)

    for t in times:
        filename = os.path.join(args.output, f"{datetime.now().timestamp()}.jpg")
        s.enterabs(t, 0, take_picture, argument=(filename,))

    print(f"Start Time:     {start_time}")
    print(f"Stop Time:      {stop_time}")
    print(f"Total Pictures: {len(times)}")

    s.run()

if __name__ == "__main__":
    main()
