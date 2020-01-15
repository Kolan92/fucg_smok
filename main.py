#!/usr/bin/env python3
from airly_client.airly_client import AirlyClient
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("token", help="airly token used to authenticate Airly API calls")
    args = parser.parse_args()
    print(args.token)
    airly = AirlyClient(args.token)
    airly.get_forecast()
    
if __name__ == '__main__':
    main()
