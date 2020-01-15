# Fucg smok

This repository holds python code which checks air quality forecast and optionally send email if the forecast is not optimistic.

## How to use it

You need to have python 3.x (tested only on 3.7.5).
Fucg smok uses Airly API, so you need to create account there and copy a token.
Install all requirements: `pip install -r requirements.txt`
Arguments can be checked with `python main.py -h`

```
usage: main.py [-h] [--percent PERCENT] [--receiver RECEIVER]
               [--subject SUBJECT] [--body BODY] [--time TIME]
               token

positional arguments:
  token                 airly token used to authenticate Airly API calls

optional arguments:
  -h, --help            show this help message and exit
  --percent PERCENT, -p PERCENT
                        percent threshold above which one raise alarm
  --receiver RECEIVER, -r RECEIVER
                        email's receiver
  --subject SUBJECT, -s SUBJECT
                        email's subject
  --body BODY, -b BODY  email's body
  --time TIME, -t TIME  time when script should check forecast, default is 14:00
``` 

Example use:

```
python main.py token -p 150 -r dupa@dupa.pl -s 'HO for the tomorrow' -b 'Due to hostile conditions I will work from home tomorrow -t 13:00'
```

### Future plans

Plans how to enhance functionalities of this script:

1. Add possibility to register as windows service, and schedule check
2. Remove hardcoded Cracow's location in airly request
3. Add more email providers


