#!/usr/bin/env python3
from airly_client.airly_client import AirlyClient
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("token", help="airly token used to authenticate Airly API calls")
    parser.add_argument("--percent", "-p", type=int, help="percent threshold above which one raise alarm")
    args = parser.parse_args()
    print(args.token)
    percent = args.percent if args.percent else 200
    airly = AirlyClient(args.token, percent)
    hours = airly.get_hours_above_limit_in_next_day()
    print("In the next 24h there will be {} hours with air pollution above {}% WHO limit".format(hours, percent))
    
if __name__ == '__main__':
    main()
