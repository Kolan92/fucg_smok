#!/usr/bin/env python3
from airly_client.airly_client import AirlyClient
from mail_sender.outlook_sender import OutlookSender
import argparse
from validate_email import validate_email
import schedule
import time

def job(token: str, percent: int, receiver: str, subject: str, body: str):
    print("I'm working...")
    airly = AirlyClient(token, percent)
    hours = airly.get_hours_above_limit_in_next_day()

    message = "In the next 24h there will be {} hours with air pollution above {}% WHO limit".format(hours, percent)
    print(message)

    if hours and receiver and validate_email(receiver):
        sender = OutlookSender()
        subject = subject if subject else "Air pollution will be above limit tomorrow"
        body = body if body else message

        sender.send_email(receiver, subject, body)
    else:
        if not receiver:
            print("Will not send an email, because receiver is not defined")
        if not validate_email(receiver):
            print("Will not send an email, because receiver email is malformed: {}".format(receiver))
        elif not hours:
            print("Will not send an email, because air quality is ok")

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("token", type=str, help="airly token used to authenticate Airly API calls")
    parser.add_argument("--percent", "-p", type=int, help="percent threshold above which one raise alarm")
    parser.add_argument("--receiver", "-r", type=str,  help="email's receiver")
    parser.add_argument("--subject", "-s", type=str,  help="email's subject")
    parser.add_argument("--body", "-b", type=str,  help="email's body")
    parser.add_argument("--time", "-t", type=str,  help="time when script should check forecast, default is 14:00")
    parser.add_argument("--now", "-n", type=bool,  help="executes once and exit the script")

    args = parser.parse_args()
    percent = args.percent if args.percent else 200
    runTime = args.time if args.time else "14:00"

    if args.now:
        job(args.token, percent, args.receiver, args.subject, args.body)
        return

    print("Periodic check of air quality will run every day at {}".format(runTime))

    (schedule.every().day.at(runTime)
        .do(job, token=args.token, percent=percent, receiver=args.receiver, subject=args.subject, body=args.body))


    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == '__main__':
    main()
