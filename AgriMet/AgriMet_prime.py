#edited by riley brogan 2016-17
import os
import sys
import optparse
import datetime


def get_startup_info():

    parser = optparse.OptionParser()
    parser.add_option('-s', '--station', dest="station", default="")
    parser.add_option('-b', '--begin_date', dest="begin_date_str", default="")
    parser.add_option('-e', '--end_date', dest="end_date_str", default="")
    args, remainder = parser.parse_args()

    if args.station not in ['ABEI', 'CHVO', 'FOGO', 'HRMO',
                            'MRSO', 'PMAI', 'PICI', 'TWFI']:
        sys.exit("Error: Invalid station code")

    # Allow end date to default to start date
    if args.end_date_str == "":
        args.end_date_str = args.begin_date_str

    # Dates must be legal and formatted as 'yyyy/mm/dd' or 'yyyy-mm-dd'
    begin_date = args.begin_date_str.replace('/', '-')
    try:
        begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    except ValueError:
        sys.exit("Error: Invalid begin date")

    end_date = args.end_date_str.replace('/', '-')
    try:
        end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        sys.exit("Error: Invalid end date")

    # Check for reasonable ranges
    if begin_date > datetime.datetime.today():
        sys.exit("Error: Beginning date is later than today")
    elif end_date > datetime.datetime.today():
        sys.exit("Error: Ending date is later than today")
    elif begin_date > end_date:
        sys.exit("Error: Beginning date is later than ending date")

    return [args.station, begin_date, end_date]


station, begin_date, end_date = get_startup_info()

the_begin_date = str(begin_date)
the_end_date = str(end_date)

# NOTE: the program 'AgriMet04_15.py' is the right one to call
os.system("python AgriMet05_01.py -s " + station + " -b " + the_begin_date + " -e " + the_end_date)
#os.system("python AgriMet_after.py -s " + station + " -b " + the_begin_date + " -e " + the_end_date)