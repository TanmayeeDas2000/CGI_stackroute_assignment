import datetime

def countdown_timer(target_date):
    while True:
        current_datetime = datetime.datetime.now()
        time_remaining = target_date - current_datetime

        if time_remaining.total_seconds() <= 0:
            print("Countdown expired!")
            break

        days, seconds = time_remaining.days, time_remaining.seconds
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)

        print(f"Time Remaining: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

        # You can adjust the update frequency as needed
        time.sleep(1)  # Sleep for 1 second

if __name__ == "__main__":
    target_date = datetime.datetime(2023, 12, 31, 23, 59, 59)  # Change this to your target date and time
    countdown_timer(target_date)