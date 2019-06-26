import sys
import optparse
import urllib
#import urllib2
import urllib.request as urllib2
import datetime
import string
import re
# changed the website to https - December 12, 2016 - fev
# edited and reformatted - 2016 - riley brogan
##
#                         T O   R U N
##
#   Example:
#
#   C:> python AgriMet.py -s ABEI -b 2012/10/12 -e 2012/10/13 > D:\Data\rawdata\Agrimet
#
# AGRIMET_WEBSITE = 'http://www.usbr.gov/pn-bin/day3.pl' old replace with agrimet.pl
#Access Denied - Missing Query String. at /data/web/sites/www.usbr.gov/cgi-files/pn-bin/agrimet.pl line 32.

AGRIMET_WEBSITE = 'https://www.usbr.gov/pn-bin/instant.pl'

##
#   This dictionary has the specific dates and times when daylight time
#   begins or ends for each station.
#
#   NOTE: Data for Fall, 2012 and thereafter will need to be inserted and/or verified.
##
daylight_datetimes = {
    '2011_ABEI_Spring': '2011-03-13 02:00:00',
    '2011_CHVO_Spring': '2011-03-13 01:30:00',
    '2011_FOGO_Spring': '2011-03-13 02:00:00',
    '2011_HRMO_Spring': '2011-03-13 02:00:00',
    '2011_MRSO_Spring': '2011-03-13 02:00:00',
    '2011_PMAI_Spring': '2011-03-13 02:00:00',
    '2011_PICI_Spring': '2011-03-13 02:00:00',
    '2011_TWFI_Spring': '2011-03-13 02:00:00',
    '2011_ABEI_Fall'  : '2011-11-06 01:00:00',
    '2011_CHVO_Fall'  : '2011-11-06 01:00:00',
    '2011_FOGO_Fall'  : '2011-11-06 01:00:00',
    '2011_HRMO_Fall'  : '2011-11-06 01:00:00',
    '2011_MRSO_Fall'  : '2011-11-06 01:00:00',
    '2011_PMAI_Fall'  : '2011-11-06 01:00:00',
    '2011_PICI_Fall'  : '2011-11-06 01:00:00',
    '2011_TWFI_Fall'  : '2011-11-06 01:00:00',
    '2012_ABEI_Spring': '2012-03-11 01:55:00',
    '2012_CHVO_Spring': '2012-03-11 01:30:00',
    '2012_FOGO_Spring': '2012-03-11 02:00:00',
    '2012_HRMO_Spring': '2012-03-11 01:30:00',
    '2012_MRSO_Spring': '2012-03-11 02:00:00',
    '2012_PMAI_Spring': '2012-03-11 01:30:00',
    '2012_PICI_Spring': '2012-03-11 01:30:00',
    '2012_TWFI_Spring': '2012-03-11 01:30:00',
    '2012_ABEI_Fall'  : '2012-11-04 01:00:00',
    '2012_CHVO_Fall'  : '2012-11-04 01:00:00',
    '2012_FOGO_Fall'  : '2012-11-04 01:00:00',
    '2012_HRMO_Fall'  : '2012-11-04 01:00:00',
    '2012_MRSO_Fall'  : '2012-11-04 01:00:00',
    '2012_PMAI_Fall'  : '2012-11-04 01:00:00',
    '2012_PICI_Fall'  : '2012-11-04 01:00:00',
    '2012_TWFI_Fall'  : '2012-11-04 01:00:00',
    '2013_ABEI_Spring': '2013-03-10 01:55:00',
    '2013_CHVO_Spring': '2013-03-10 01:30:00',
    '2013_FOGO_Spring': '2013-03-10 01:30:00',
    '2013_HRMO_Spring': '2013-03-10 01:30:00',
    '2013_MRSO_Spring': '2013-03-10 01:30:00',
    '2013_PMAI_Spring': '2013-03-10 02:30:00',
    '2013_PICI_Spring': '2013-03-10 02:30:00',
    '2013_TWFI_Spring': '2013-03-10 02:30:00',
    '2013_ABEI_Fall'  : '2013-11-03 01:00:00',
    '2013_CHVO_Fall'  : '2013-11-03 01:00:00',
    '2013_FOGO_Fall'  : '2013-11-03 01:00:00',
    '2013_HRMO_Fall'  : '2013-11-03 01:00:00',
    '2013_MRSO_Fall'  : '2013-11-03 01:00:00',
    '2013_PMAI_Fall'  : '2013-11-03 01:00:00',
    '2013_PICI_Fall'  : '2013-11-03 01:00:00',
    '2013_TWFI_Fall'  : '2013-11-03 01:00:00',
    '2014_ABEI_Spring': '2014-03-09 01:55:00',
    '2014_CHVO_Spring': '2014-03-09 01:30:00',
    '2014_FOGO_Spring': '2014-03-09 01:30:00',
    '2014_HRMO_Spring': '2014-03-09 01:30:00',
    '2014_MRSO_Spring': '2014-03-09 01:30:00',
    '2014_PMAI_Spring': '2014-03-09 02:30:00',
    '2014_PICI_Spring': '2014-03-09 02:30:00',
    '2014_TWFI_Spring': '2014-03-09 02:30:00',
    '2014_ABEI_Fall'  : '2014-11-02 01:00:00',
    '2014_CHVO_Fall'  : '2014-11-02 01:00:00',
    '2014_FOGO_Fall'  : '2014-11-02 01:00:00',
    '2014_HRMO_Fall'  : '2014-11-02 01:00:00',
    '2014_MRSO_Fall'  : '2014-11-02 01:00:00',
    '2014_PMAI_Fall'  : '2014-11-02 01:00:00',
    '2014_PICI_Fall'  : '2014-11-02 01:00:00',
    '2014_TWFI_Fall'  : '2014-11-02 01:00:00',
    '2015_ABEI_Spring': '2015-03-08 01:55:00',
    '2015_CHVO_Spring': '2015-03-08 01:30:00',
    '2015_FOGO_Spring': '2015-03-08 01:30:00',
    '2015_HRMO_Spring': '2015-03-08 01:30:00',
    '2015_MRSO_Spring': '2015-03-08 01:30:00',
    '2015_PMAI_Spring': '2015-03-08 02:30:00',
    '2015_PICI_Spring': '2015-03-08 02:30:00',
    '2015_TWFI_Spring': '2015-03-08 02:30:00',
    '2015_ABEI_Fall'  : '2015-11-08 01:00:00',
    '2015_CHVO_Fall'  : '2015-11-08 01:00:00',
    '2015_FOGO_Fall'  : '2015-11-08 01:00:00',
    '2015_HRMO_Fall'  : '2015-11-08 01:00:00',
    '2015_MRSO_Fall'  : '2015-11-08 01:00:00',
    '2015_PMAI_Fall'  : '2015-11-08 01:00:00',
    '2015_PICI_Fall'  : '2015-11-08 01:00:00',
    '2015_TWFI_Fall'  : '2015-11-08 01:00:00',
    '2016_ABEI_Spring': '2016-03-13 01:55:00',
    '2016_CHVO_Spring': '2016-03-13 01:30:00',
    '2016_FOGO_Spring': '2016-03-13 01:30:00',
    '2016_HRMO_Spring': '2016-03-13 01:30:00',
    '2016_MRSO_Spring': '2016-03-13 01:30:00',
    '2016_PMAI_Spring': '2016-03-13 02:30:00',
    '2016_PICI_Spring': '2016-03-13 02:30:00',
    '2016_TWFI_Spring': '2016-03-13 02:30:00',
    '2016_ABEI_Fall'  : '2016-11-06 01:00:00',
    '2016_CHVO_Fall'  : '2016-11-06 01:00:00',
    '2016_FOGO_Fall'  : '2016-11-06 01:00:00',
    '2016_HRMO_Fall'  : '2016-11-06 01:00:00',
    '2016_MRSO_Fall'  : '2016-11-06 01:00:00',
    '2016_PMAI_Fall'  : '2016-11-06 01:00:00',
    '2016_PICI_Fall'  : '2016-11-06 01:00:00',
    '2016_TWFI_Fall'  : '2016-11-06 01:00:00',
    '2017_ABEI_Spring': '2017-03-12 01:55:00',
    '2017_CHVO_Spring': '2017-03-12 01:30:00',
    '2017_FOGO_Spring': '2017-03-12 01:30:00',
    '2017_HRMO_Spring': '2017-03-12 01:30:00',
    '2017_MRSO_Spring': '2017-03-12 01:30:00',
    '2017_PMAI_Spring': '2017-03-12 02:30:00',
    '2017_PICI_Spring': '2017-03-12 02:30:00',
    '2017_TWFI_Spring': '2017-03-12 02:30:00',
    '2017_ABEI_Fall'  : '2017-11-05 01:00:00',
    '2017_CHVO_Fall'  : '2017-11-05 01:00:00',
    '2017_FOGO_Fall'  : '2017-11-05 01:00:00',
    '2017_HRMO_Fall'  : '2017-11-05 01:00:00',
    '2017_MRSO_Fall'  : '2017-11-05 01:00:00',
    '2017_PMAI_Fall'  : '2017-11-05 01:00:00',
    '2017_PICI_Fall'  : '2017-11-05 01:00:00',
    '2017_TWFI_Fall'  : '2017-11-05 01:00:00',
    '2018_ABEI_Spring': '2018-03-11 01:55:00',
    '2018_CHVO_Spring': '2018-03-11 01:30:00',
    '2018_FOGO_Spring': '2018-03-11 01:30:00',
    '2018_HRMO_Spring': '2018-03-11 01:30:00',
    '2018_MRSO_Spring': '2018-03-11 01:30:00',
    '2018_PMAI_Spring': '2018-03-11 02:30:00',
    '2018_PICI_Spring': '2018-03-11 02:30:00',
    '2018_TWFI_Spring': '2018-03-11 02:30:00',
    '2018_ABEI_Fall'  : '2018-11-04 01:00:00',
    '2018_CHVO_Fall'  : '2018-11-04 01:00:00',
    '2018_FOGO_Fall'  : '2018-11-04 01:00:00',
    '2018_HRMO_Fall'  : '2018-11-04 01:00:00',
    '2018_MRSO_Fall'  : '2018-11-04 01:00:00',
    '2018_PMAI_Fall'  : '2018-11-04 01:00:00',
    '2018_PICI_Fall'  : '2018-11-04 01:00:00',
    '2018_TWFI_Fall'  : '2018-11-04 01:00:00',
    '2019_ABEI_Spring': '2019-03-10 01:55:00',
    '2019_CHVO_Spring': '2019-03-10 01:30:00',
    '2019_FOGO_Spring': '2019-03-10 01:30:00',
    '2019_HRMO_Spring': '2019-03-10 01:30:00',
    '2019_MRSO_Spring': '2019-03-10 01:30:00',
    '2019_PMAI_Spring': '2019-03-10 02:30:00',
    '2019_PICI_Spring': '2019-03-10 02:30:00',
    '2019_TWFI_Spring': '2019-03-10 02:30:00',
    '2019_ABEI_Fall'  : '2019-11-04 01:00:00',
    '2019_CHVO_Fall'  : '2019-11-04 01:00:00',
    '2019_FOGO_Fall'  : '2019-11-04 01:00:00',
    '2019_HRMO_Fall'  : '2019-11-04 01:00:00',
    '2019_MRSO_Fall'  : '2019-11-04 01:00:00',
    '2019_PMAI_Fall'  : '2019-11-04 01:00:00',
    '2019_PICI_Fall'  : '2019-11-04 01:00:00',
    '2019_TWFI_Fall'  : '2019-11-04 01:00:00'}

#   This dictionary maps station names to ID numbers.
##
station_ids = {
    'ABEI': '94174',
    'CHVO': '94251',
    'FOGO': '94008',
    'HRMO': '94169',
    'MRSO': '94252',
    'PMAI': '94173',
    'PICI': '94172',
    'TWFI': '94171'}

##
#   Validates and parses command line arguments, returning a station code and
#   starting and ending date objects to the caller.
##
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

##
#   For a specified station and datatype, this gets one or more days worth of
#   data from the AgriMet website. The url (a global constant) has changed
#   several times in the past. The site once began using HTTPS, but reverted
#   to HTTP after about a year.
##
def download(station, data_type, begin_date, end_date):

    # NOTE: 'format=1' causes the default column separater ',' to be replaced by spaces
    query_string = ('station=' + station
        + '&year='  + str(begin_date.year)
        + '&month=' + str(begin_date.month)
        + '&day='   + str(begin_date.day)
        + '&year='  + str(end_date.year)
        + '&month=' + str(end_date.month)
        + '&day='   + str(end_date.day)
        + '&pcode=' + data_type
        + '&format=1')
    url = AGRIMET_WEBSITE + '?' + query_string

    response = urllib2.urlopen(url)
    webpage = response.read()

    return webpage.decode('utf-8')
##
#   Parses a string (web_page) to obtain original data values of a given type, for
#   a given date and time range. Then converts these into corresponding SRML data
#   and inserts them into a dictionary, which is returned.
#
#   Example of web_page format:
#       <HTML>
#       <HEAD><TITLE>Hydromet/AgriMet Data Access</title></head>
#       <BODY BGCOLOR=#FFFFFF>
#       <p><PRE>
#       CHVO
#             DATE  TIME        SQ
#       07/23/2011 00:00     643.36
#        ...
#       07/23/2011 23:00     311.65
#       </pre>
#       </body></html>
##
def convert(station, web_page, data_type):

    # This dictionary maps the frequency of irradiance samples to the station
    irradiance_interval = {
    'ABEI': 60,
    'CHVO': 60,
    'FOGO': 60,
    'HRMO': 60,
#trying 60 on Hermiston
    'MRSO': 60,
    'PICI': 60,
    'PMAI': 60,
    'TWFI': 60}

    # Start with an empty column dictionary
    column = {}

    # Older AgriMet systems for irradiance and rainfall data involve finding the
    # difference between consecutive readings to give the actual value.
    starting_loop = True
    prev_value = 0

    # Split into lines and skip extraneous header text
    lines = web_page.split("\n")
    lines = lines[21:]
    for line in lines:

        #if line[0:4] == "DATE":
         #   continue
        # NOTE: The string 'END DATA' marks the end of data (!)
        if line[0] == "E":
            break

        # Break line into components
        # ag_date, ag_time, ag_data_str = line.split()
        # ag_date, ag_time, ag_data_str = re.split('\s+', line)
        ag_date, ag_time, ag_data_str = line.split()
        ag_datetime = ag_date + " " + ag_time
        ag_datetime = datetime.datetime.strptime(ag_datetime, "%m/%d/%Y %H:%M")
        if ag_data_str[-1] in '0123456789':
            ag_data = float(ag_data_str)
        else:
            # Throw away trailing flag character for now ...
            ag_data_str = ag_data_str[:-1]
            if ag_data_str[-1] in '0123456789':
                # Truncated string seems to be a number
                ag_data = float(ag_data_str)
            else:
                # Truncated string doesn't seem to contain a number, may be blank
                ag_data = float('-999')
        if data_type == "OB":
            # Convert ambient temperature Fahrenheit to Celsius
            ag_data = round((ag_data - 32.0) / 1.8, 1)
        elif data_type == "WS":
            # Convert wind speed in miles/hour to meters/second
            ag_data = round(ag_data * 0.44704, 1)
        elif data_type in ["SI", "SI2"]:
            # Convert global or diffuse irradiance in langleys to Wh/m^2/h
            ag_data = int(round((ag_data * 11.622) * (60 / irradiance_interval[station])))
        elif data_type == "PC":
            # Convert cumulative rainfall in inches
            if starting_loop:
                starting_loop = False
                prev_value = ag_data
                ag_data = 0.00   # A good guess? Rainfall is "unusual" ...
            else:
                difference = ag_data - prev_value
                prev_value = ag_data
                if difference < 0.0:
                    # Rollover probably occurred, but we don't know the threshold value.
                    # Assume there has been 0.01 inches of precipitation and start over
                    # from some new base value (which can vary wildly).
                    ag_data = 0.01
                else:
                    ag_data = round(difference, 2)
        elif data_type == "PI":
            ag_data = round(ag_data, 2)
        elif data_type == "TU":
            ag_data = round(ag_data, 2)
        elif data_type == "WD":
            ag_data = round(ag_data, 1)

        column[str(ag_datetime)] = ag_data,11

    return column

##
#   Copies in_column dictionary to out_column dictionary, inserting key/value
#   pairs with default values in out_column if a value's missing for an interval
#   within the specified date range. This also fills gaps where the particular
#   datatype is not sampled as frequently as some others for this station.
#   (Then, the value is not actually "missing".
##
def fill_gaps(in_column, shortest_interval, data_type, beg_datetime, end_datetime):

    default_value = {'OB': "-99.9,99",  'TU': "-99.9,99", 'WS': "-99.9,99", 'WD': "-99.9,99",
                     'SI': "-999,99", 'SI2': "-999,99",  'PI': "-99.99,99", 'PC': "-99.99,99"}

    if shortest_interval == 15:
        end_min = 45
    elif shortest_interval == 5:
        end_min = 55
    end_datetime = end_datetime.replace(hour=23, minute=end_min)

    out_column = {}
    cur_datetime = beg_datetime
    while cur_datetime <= end_datetime:
        try:
            out_column[str(cur_datetime)] = in_column[str(cur_datetime)]
        except KeyError:
            out_column[str(cur_datetime)] = default_value[data_type]
        cur_datetime += datetime.timedelta(minutes=shortest_interval)

    return out_column

##
#   Converts input datetime to standard time if it was in daylight time
##
def daylight_to_std(station, in_datetime_str):

    in_datetime = datetime.datetime.strptime(in_datetime_str, "%Y-%m-%d %H:%M:%S")
    out_datetime = in_datetime

    spring_key = str(in_datetime.year) + "_" + station + "_Spring"
    spring_datetime_str = daylight_datetimes[spring_key]

    fall_key = str(in_datetime.year) + "_" + station + "_Fall"
    fall_datetime_str = daylight_datetimes[fall_key]

    if in_datetime_str >= spring_datetime_str and in_datetime_str < fall_datetime_str:
        # It's daylight time, so subtract an hour
        out_datetime -= datetime.timedelta(hours=1)

    return str(out_datetime)

def past_March(station, in_datetime_str):

    in_datetime = datetime.datetime.strptime(in_datetime_str, "%Y-%m-%d %H:%M:%S")
    out_datetime = in_datetime

    spring_key = str(in_datetime.year) + "_" + station + "_Spring"
    spring_datetime_str = daylight_datetimes[spring_key]

    fall_key = str(in_datetime.year) + "_" + station + "_Fall"
    fall_datetime_str = daylight_datetimes[fall_key]

    if in_datetime_str >= spring_datetime_str and in_datetime_str < fall_datetime_str:
        # It's daylight time, so subtract an hour
        return True

    else:
        return False

##
#   Copies in_column dictionary to out_column dictionary, adjusting times
#   in accordance with time zone and daylight saving differences, so that
#   resulting times are all PST.
##
def adjust_datetimes(station, time_zone_offset, in_column):

    out_column = {}
    for datetime_str in in_column.keys():
        std_datetime = datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
        if time_zone_offset == 1:
            std_datetime += datetime.timedelta(hours=1)
        std_datetime_str = str(std_datetime)
        std_datetime_str = daylight_to_std(station, datetime_str)
        out_column[std_datetime_str] = in_column[datetime_str]

    return out_column

##
#   Formats a standard time, hh:mm:ss, as an SRML time string; i.e.,
#   m or mm or hmm or hhmm.
##
def std_to_srml_time(year, year_day, std_time):

    std_hr, std_min, std_sec = std_time.split(":")
    if std_hr in ["00", "24"]:
        if int(std_min) == 0:
            srml_time = "2400"
            if year_day == 1:
                year -= 1
                if year % 4 == 0:
                    if year != 2000:
                        year_day = 366
                    else:
                        year_day = 365
                else:
                    year_day = 365
            else:
                year_day -= 1
        else:
            srml_time = str(int(std_min))   # Lose leading zero if any
    else:
        srml_time = str(int(std_hr))    # Get rid of leading zero if any
        srml_time += std_min

    return [str(year), str(year_day), srml_time]


def header_line(station):
    datetime_key = datetime.datetime.strptime(str(daylight_to_std(station,str(effective_begin_date))), "%Y-%m-%d %H:%M:%S")
    year = 0 + int(datetime.datetime.strftime(datetime_key, "%Y"))
    year_day = 0 + int(datetime.datetime.strftime(datetime_key, "%j"))
    if station == 'ABEI':
        header = station_ids[station]+ '\t' + str(year) + '\t' + '1002' + '\t' + '0' + '\t' + '3002' + '\t' + '0' + '\t' + '9301' + '\t' + '0' + '\t' + '9331' + '\t' + '0' + '\t' + '9152' + '\t' + '0' + '\t' + '9201' + '\t' + '0' + '\t' + '9211' + '\t' + '0'
        print(header + str.expandtabs('\t',1))

    elif station == 'CHVO':
        header = station_ids[station]+ '\t' + str(year) + '\t' + '1001' + '\t' + '0' + '\t' + '9301' + '\t' + '0' + '\t' + '9331' + '\t' + '0' + '\t' + '9151' + '\t' + '0' + '\t' + '9201' + '\t' + '0' + '\t' + '9211' + '\t' + '0'
        print(header + str.expandtabs('\t',1))

    elif station == 'FOGO':
        header = station_ids[station]+ '\t' + str(year) + '\t' + '1001' + '\t' + '0' + '\t' + '9301' + '\t' + '0' + '\t' + '9331' + '\t' + '0' + '\t' + '9151' + '\t' + '0' + '\t' + '9201' + '\t' + '0' + '\t' + '9211' + '\t' + '0'
        print ( header + str.expandtabs('\t',1))

    elif station == 'HRMO':
        header = station_ids[station]+ '\t' + str(year) + '\t' + '1001' + '\t' + '0' + '\t' + '3001' + '\t' + '0' + '\t' + '9301' + '\t' + '0' + '\t' + '9331' + '\t' + '0' + '\t' + '9151' + '\t' + '0' + '\t' + '9201' + '\t' + '0' + '\t' + '9211' + '\t' + '0'
        print (header + str.expandtabs('\t',1))

    elif station == 'MRSO':
        header = station_ids[station]+ '\t' + str(year) + '\t' + '1001' + '\t' + '0' + '\t' + '3001' + '\t' + '0' + '\t' + '9301' + '\t' + '0' + '\t' + '9331' + '\t' + '0' + '\t' + '9151' + '\t' + '0' + '\t' + '9201' + '\t' + '0' + '\t' + '9211' + '\t' + '0'
        print (header + str.expandtabs('\t',1))

    elif station == 'PMAI':
        header = station_ids[station]+ '\t' + str(year) + '\t' + '1001' + '\t' + '0' + '\t' + '3001' + '\t' + '0' + '\t' + '9301' + '\t' + '0' + '\t' + '9331' + '\t' + '0' + '\t' + '9151' + '\t' + '0' + '\t' + '9201' + '\t' + '0' + '\t' + '9211' + '\t' + '0'
        print (header + str.expandtabs('\t',1))

    elif station == 'PICI':
        header = station_ids[station]+ '\t' + str(year) + '\t' + '1001' + '\t' + '0' + '\t' + '3001' + '\t' + '0' + '\t' + '9301' + '\t' + '0' + '\t' + '9331' + '\t' + '0' + '\t' + '9151' + '\t' + '0' + '\t' + '9201' + '\t' + '0' + '\t' + '9211' + '\t' + '0'
        print (header + str.expandtabs('\t',1))

    elif station == 'TWFI':
        header = station_ids[station]+ '\t' + str(year) + '\t' + '1001' + '\t' + '0' + '\t' + '3001' + '\t' + '0' + '\t' + '9301' + '\t' + '0' + '\t' + '9331' + '\t' + '0' + '\t' + '9151' + '\t' + '0' + '\t' + '9201' + '\t' + '0' + '\t' + '9211' + '\t' + '0'
        print (header + str.expandtabs('\t',1))

###
#                             M A I N   P R O G R A M
###

station, begin_date, end_date = get_startup_info()

# Move effective start and end dates back 1 day to simplify processing in case of (1) daylight
# time, (2) time zone adjustments, (3) calculations depending on successive raw data values,
# and (4) possible gaps from the previous day.
effective_begin_date = begin_date #- datetime.timedelta(days=1)
effective_end_date = end_date

time_zone_offset = 0   # For Oregon stations; Idaho stations will override this
interval = 15          # Least time between data samples for all stations but ABEI

if station == 'ABEI':
    data_types = ['SI', 'SI2', 'OB', 'TU', 'PI', 'WD', 'WS']
    interval = 5
    time_zone_offset = 1
    if past_March(station,str(effective_begin_date)) == True:
        effective_begin_date = begin_date + datetime.timedelta(hours=1.0833333333)
    else:
        effective_begin_date = begin_date + datetime.timedelta(hours=0.0833333333)
elif station == 'CHVO':
    data_types = ['SI', 'OB', 'TU', 'PC', 'WD', 'WS']
    if past_March(station,str(effective_begin_date)) == True:
        effective_begin_date = begin_date + datetime.timedelta(hours=1.25)
    else:
        effective_begin_date = begin_date + datetime.timedelta(hours=0.25)
elif station == 'FOGO':
    data_types = ['SI', 'OB', 'TU', 'PC', 'WD', 'WS']
    if past_March(station,str(effective_begin_date)) == True:
        effective_begin_date = begin_date + datetime.timedelta(hours=1.25)
    else:
        effective_begin_date = begin_date + datetime.timedelta(hours=0.25)
elif station == 'HRMO':
    data_types = ['SI', 'SI2', 'OB', 'TU', 'PC', 'WD', 'WS']
    if past_March(station,str(effective_begin_date)) == True:
        effective_begin_date = begin_date + datetime.timedelta(hours=1.25)
    else:
        effective_begin_date = begin_date + datetime.timedelta(hours=0.25)
elif station == 'MRSO':
    data_types = ['SI', 'SI2', 'OB', 'TU', 'PC', 'WD', 'WS']
    if past_March(station,str(effective_begin_date)) == True:
        effective_begin_date = begin_date + datetime.timedelta(hours=1.25)
    else:
        effective_begin_date = begin_date + datetime.timedelta(hours=0.25)
elif station == 'PMAI':
    data_types = ['SI', 'SI2', 'OB', 'TU', 'PC', 'WD', 'WS']
    time_zone_offset = 1
    if past_March(station,str(effective_begin_date)) == True:
        effective_begin_date = begin_date + datetime.timedelta(hours=1.25)
    else:
        effective_begin_date = begin_date + datetime.timedelta(hours=0.25)
elif station == 'PICI':
    data_types = ['SI', 'SI2', 'OB', 'TU', 'PC', 'WD', 'WS']
    time_zone_offset = 1
    if past_March(station,str(effective_begin_date)) == True:
        effective_begin_date = begin_date + datetime.timedelta(hours=1.25)
    else:
        effective_begin_date = begin_date + datetime.timedelta(hours=0.25)
elif station == 'TWFI':
    data_types = ['SI', 'SI2', 'OB', 'TU', 'PC', 'WD', 'WS']
    time_zone_offset = 1
    if past_March(station,str(effective_begin_date)) == True:
        effective_begin_date = begin_date + datetime.timedelta(hours=1.25)
    else:
        effective_begin_date = begin_date + datetime.timedelta(hours=0.25)

# Accumulate individual columns (dictionaries) of translated, filled,
# and time-adjusted data in a list.so we can write the values out in
# the expected order.
columns = []
for data_type in data_types:
    webpage = download(station, data_type, effective_begin_date, effective_end_date)
    orig_column = convert(station, webpage, data_type)
    std_column = fill_gaps(orig_column, interval, data_type,
                           effective_begin_date, effective_end_date)
    adjusted_column = adjust_datetimes(station, time_zone_offset, std_column)
    columns.append(adjusted_column)

header_line(station)

# Now write out the data in the dictionaries.
for datetime_str_key in sorted(columns[0].keys()):
    datetime_key = datetime.datetime.strptime(datetime_str_key, "%Y-%m-%d %H:%M:%S")
    year = 0 + int(datetime.datetime.strftime(datetime_key, "%Y"))
    year_day = 0 + int(datetime.datetime.strftime(datetime_key, "%j"))
    year, year_day, srml_time = std_to_srml_time(year, year_day, datetime_str_key[11:])
    cur_rec = year_day + "\t" + srml_time
    for column in columns:
        cur_rec1 = "," + str(column[datetime_str_key]).replace('(', "").replace(')',"")
        cur_rec += str(cur_rec1).replace(" ", "").replace(',','\t')
    print (cur_rec + str.expandtabs('\t',1))
