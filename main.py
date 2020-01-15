#!/usr/bin/env python3
from airly_client.airly_client import AirlyClient
from mail_sender.outlook_sender import OutlookSender
import argparse
from validate_email import validate_email

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("token", type=str, help="airly token used to authenticate Airly API calls")
    parser.add_argument("--percent", "-p", type=int, help="percent threshold above which one raise alarm")
    parser.add_argument("--to", "-t", type=str,  help="email's receiver")
    parser.add_argument("--subject", "-s", type=str,  help="email's subject")
    parser.add_argument("--body", "-b", type=str,  help="email's body")
    
    args = parser.parse_args()
    percent = args.percent if args.percent else 200
    
    airly = AirlyClient(args.token, percent)
    hours = airly.get_hours_above_limit_in_next_day()

    message = "In the next 24h there will be {} hours with air pollution above {}% WHO limit".format(hours, percent)
    print(message)

    if hours and args.to and validate_email(args.to):
        sender = OutlookSender()
        subject = args.subject if args.subject else "Air pollution will be above limit tomorrow"
        body = args.body if args.body else message

        sender.send_email(args.to, subject, body)
    else:
        if (not args.to) or (not validate_email(args.to)):
            print("Will not send an email, because receiver is not defined or in incorrect format")
        elif not hours:
            print("Will not send an email, because air quality is ok")

    
if __name__ == '__main__':
    main()
