## TODO: import all necessary packages and functions
import os
import time
import pandas as pd
import numpy as np
from datetime import datetime
from pprint import pprint

## Filenames
# chicago = 'chicago.csv'
# new_york = 'new_york_city.csv'
# washington = 'washington.csv'


def get_city():
    '''Asks the user for a city and returns the filename for that city's bike share data.

    Args:
        none.
    Returns:
        (str) Filename for a city's bikeshare data.
    '''
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')
    # TODO: handle raw input and complete function
    if city.lower() =='chicago':
        city = 'chicago.csv'
        return str(city)
    elif city.lower() in ('new york','newyork'):
        city = 'new_york_city.csv'
        return str(city)
    elif city.lower() =='washington':
        city = 'washington.csv'
        return str(city)
    else:
        get_city()


def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n').lower()
    # TODO: handle raw input and complete function
    if time_period in('month','day','none'):
        return str(time_period.lower())
    else:
        get_time_period()

def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    month = input('\nWhich month? January, February, March, April, May, or June?\n').title()
    # TODO: handle raw input and complete function
    if month in('January', 'February', 'March', 'April', 'May', 'June'):
        return str(month.title())
    else:
        get_month()


def get_day():
    '''Asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    day = input('\nWhich day? Please type your response as Sunday,Monday etc.\n').title()
    # TODO: handle raw input and complete function
    if day in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'):
        return str(day.title())
    else:
        get_day()


def popular_month(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular month for start time?
    '''
    # TODO: complete function
    df = pd.DataFrame(city_file)
    df['month'] = pd.DatetimeIndex(df['Start Time']).month
    df1 = pd.DataFrame(df.groupby(['month']).count().idxmax())
    x = df1.values
    y = int(x[:1])
    l = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June'}
    for key, value in l.items():
        if key == y:
            z = value
    return str(z)


def popular_day(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    '''
    # TODO: complete function
    df = pd.DataFrame(city_file['Start Time'])
    df['month'] = pd.DatetimeIndex(df['Start Time']).month
    df['week'] = pd.DatetimeIndex(df['Start Time']).weekday_name

    if time_period == 'none':
        df1 = pd.DataFrame(df.groupby(['month', 'week']).count().idxmax())
        x = tuple(df1.values.tolist())
        y = tuple(x[0])
        z = tuple(y[0])
        return str(z[1])

    if time_period in ('January', 'February', 'March', 'April', 'May', 'June'):
        l = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June'}
        for i, k in l.items():
            if k == time_period:
                time_period = i
        df1 = df[df.month == time_period]
        df2 = pd.DataFrame(df1.groupby(['month', 'week']).count().idxmax())
        x = tuple(df2.values.tolist())
        y = tuple(x[0])
        z = tuple(y[0])
        return str(z[1])


def popular_hour(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular hour of day for start time?
    '''
    # TODO: complete function
    df = pd.DataFrame(city_file['Start Time'])
    df['month'] = pd.DatetimeIndex(df['Start Time']).month
    df['day'] = pd.DatetimeIndex(df['Start Time']).day
    df['weekday_name'] = pd.DatetimeIndex(df['Start Time']).weekday_name
    df['hour'] = pd.DatetimeIndex(df['Start Time']).hour

    if time_period in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'):
        df1 = df[df.weekday_name == time_period]
        df2 = pd.DataFrame(df1.groupby(['month', 'weekday_name', 'hour']).count().idxmax())
        x = tuple(df2.values.tolist())
        y = tuple(x[0])
        z = tuple(y[0])
        print("Most popular hour of day for start time is:" + str(z[2]))

    elif time_period in ('January', 'February', 'March', 'April', 'May', 'June'):
        l = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June'}
        for i, k in l.items():
            if k == time_period:
                time_period = i
        df1 = df[df.month == time_period]
        df2 = pd.DataFrame(df1.groupby(['month', 'weekday_name', 'hour']).count().idxmax())
        x = tuple(df2.values.tolist())
        y = tuple(x[0])
        z = tuple(y[0])
        print("Most popular hour of day for start time is: " + str(z[2]))

    else:
        if time_period=='none':
            df1 = pd.DataFrame(df.groupby(['month', 'weekday_name', 'hour']).count().idxmax())
            x = tuple(df1.values.tolist())
            y = tuple(x[0])
            z = tuple(y[0])
            print("Most popular hour of day for start time is: " + str(z[2]))


def trip_duration(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the total trip duration and average trip duration?
    '''
    # TODO: complete function
    df = pd.DataFrame(city_file)
    df['month'] = pd.DatetimeIndex(df['Start Time']).month
    df['weekday_name'] = pd.DatetimeIndex(df['Start Time']).weekday_name

    if time_period in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'):
        df1 = df[df.weekday_name == time_period]
        trip_mean = str(df1['Trip Duration'].mean())
        trip_sum = str(df1['Trip Duration'].sum())
        print("Total trip duration is: " + trip_sum + " and average trip duration is: " + trip_mean)

    elif time_period in ('January', 'February', 'March', 'April', 'May', 'June'):
        l = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June'}
        for i, k in l.items():
            if k == time_period:
                time_period = i
        df1 = df[df.month == time_period]
        trip_mean = str(df1['Trip Duration'].mean())
        trip_sum = str(df1['Trip Duration'].sum())
        print("Total trip duration is: " + trip_sum + " and average trip duration is: " + trip_mean)

    else:
        if time_period == 'none':
            trip_mean = str(df['Trip Duration'].mean())
            trip_sum = str(df['Trip Duration'].sum())
            print("Total trip duration is: " + trip_sum + " and average trip duration is: " + trip_mean)


def popular_stations(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular start station and most popular end station?
    '''
    # TODO: complete function
    df = pd.DataFrame(city_file)
    df['month'] = pd.DatetimeIndex(df['Start Time']).month
    df['weekday_name'] = pd.DatetimeIndex(df['Start Time']).weekday_name

    if time_period in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'):
        df1 = df[df.weekday_name == time_period]
        df2 = pd.DataFrame(df1.groupby(['Start Station']).count().idxmax())
        df3 = pd.DataFrame(df1.groupby(['End Station']).count().idxmax())
        x = tuple(df2.values.tolist())
        y = tuple(x[0])
        start_station = y[0]
        xx = tuple(df3.values.tolist())
        yx = tuple(xx[0])
        end_station = yx[0]
        return start_station, end_station

    elif time_period in ('January', 'February', 'March', 'April', 'May', 'June'):
        l = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June'}
        for i, k in l.items():
            if k == time_period:
                time_period = i
        df1 = df[df.month == time_period]
        df2 = pd.DataFrame(df1.groupby(['Start Station']).count().idxmax())
        df3 = pd.DataFrame(df1.groupby(['End Station']).count().idxmax())
        x = tuple(df2.values.tolist())
        y = tuple(x[0])
        start_station = y[0]
        xx = tuple(df3.values.tolist())
        yx = tuple(xx[0])
        end_station = yx[0]
        return start_station, end_station

    else:
        if time_period == 'none':
            df2 = pd.DataFrame(df.groupby(['Start Station']).count().idxmax())
            df3 = pd.DataFrame(df.groupby(['End Station']).count().idxmax())
            x = tuple(df2.values.tolist())
            y = tuple(x[0])
            start_station = y[0]
            xx = tuple(df3.values.tolist())
            yx = tuple(xx[0])
            end_station = yx[0]
            return start_station, end_station


def popular_trip(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular trip?
    '''
    # TODO: complete function
    df = pd.DataFrame(city_file)
    df['month'] = pd.DatetimeIndex(df['Start Time']).month
    df['weekday_name'] = pd.DatetimeIndex(df['Start Time']).weekday_name

    if time_period in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'):
        df1 = df[df.weekday_name == time_period]
        df2 = pd.DataFrame(df1.groupby(['Start Station', 'End Station']).count().idxmax())
        x = tuple(df2.values.tolist())
        y = tuple(x[0])
        return str(y[0])

    elif time_period in ('January', 'February', 'March', 'April', 'May', 'June'):
        l = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June'}
        for i, k in l.items():
            if k == time_period:
                time_period = i
        df1 = df[df.month == time_period]
        df2 = pd.DataFrame(df1.groupby(['Start Station', 'End Station']).count().idxmax())
        x = tuple(df2.values.tolist())
        y = tuple(x[0])
        return str(y[0])

    else:
        if time_period == 'none':
            df2 = pd.DataFrame(df.groupby(['Start Station', 'End Station']).count().idxmax())
            x = tuple(df2.values.tolist())
            y = tuple(x[0])
            return str(y[0])


def users(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of each user type?
    '''
    # TODO: complete function
    df = pd.DataFrame(city_file)
    df['month'] = pd.DatetimeIndex(df['Start Time']).month
    df['weekday_name'] = pd.DatetimeIndex(df['Start Time']).weekday_name

    if time_period in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'):
        df1 = df[df.weekday_name == time_period]
        df2 = df1.groupby(['User Type']).count().to_dict()
        print("Counts of each user type: " + str(df2['Start Time']))

    elif time_period in ('January', 'February', 'March', 'April', 'May', 'June'):
        l = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June'}
        for i, k in l.items():
            if k == time_period:
                time_period = i
        df1 = df[df.month == time_period]
        df2 = df1.groupby(['User Type']).count().to_dict()
        print("Counts of each user type: " + str(df2['Start Time']))

    else:
        if time_period == 'none':
            df2 = df.groupby(['User Type']).count().to_dict()
            print("Counts of each user type: " + str(df2['Start Time']))


def gender(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of gender?
    '''
    # TODO: complete function
    df = pd.DataFrame(city_file)
    df['month'] = pd.DatetimeIndex(df['Start Time']).month
    df['weekday_name'] = pd.DatetimeIndex(df['Start Time']).weekday_name

    if time_period in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'):
        df1 = df[df.weekday_name == time_period]
        df2 = df1.groupby(['Gender']).count().to_dict()
        print("Counts of gender: " + str(df2['Start Time']))

    elif time_period in ('January', 'February', 'March', 'April', 'May', 'June'):
        l = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June'}
        for i, k in l.items():
            if k == time_period:
                time_period = i
        df1 = df[df.month == time_period]
        df2 = df1.groupby(['Gender']).count().to_dict()
        print("Counts of gender: " + str(df2['Start Time']))

    else:
        if time_period =='none':
            df2 = df.groupby(['Gender']).count().to_dict()
            print("Counts of gender: " + str(df2['Start Time']))


def birth_years(city_file, time_period):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the earliest (i.e. oldest user), most recent (i.e. youngest user),
    and most popular birth years?
    '''
    # TODO: complete function
    df = pd.DataFrame(city_file)
    df['month'] = pd.DatetimeIndex(df['Start Time']).month
    df['day'] = pd.DatetimeIndex(df['Start Time']).day
    df['weekday_name'] = pd.DatetimeIndex(df['Start Time']).weekday_name

    if time_period in ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'):
        df1 = df[df.weekday_name == time_period]
        x = str(df1['Birth Year'].max())
        y = str(df1['Birth Year'].min())
        print("Youngest user: " + x + " Oldest user: " + y)

    elif time_period in ('January', 'February', 'March', 'April', 'May', 'June'):
        l = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June'}
        for i, k in l.items():
            if k == time_period:
                time_period = i
        df1 = df[df.month == time_period]
        x = str(df1['Birth Year'].max())
        y = str(df1['Birth Year'].min())
        print("Youngest user: " + x + " Oldest user: " + y)

    else:
        if time_period == 'none':
            x = str(df['Birth Year'].max())
            y = str(df['Birth Year'].min())
            print("Youngest user: " + x + " Oldest user: " + y)


def display_data(city_file):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')
    # TODO: handle raw input and complete function
    labels={'Start Time','End Time','Trip Duration','Start Station','End Station','User Type','Gender','Birth Year'}
    if display.lower()=='yes':
        output=pd.DataFrame(city_file,columns=labels)
        for i,row in output.iterrows():
            if (i%5==0) and (i!=0):
                answer=input("Would you like to see five more\n")
                if(answer.lower())=='yes':
                    print(row)
                else:
                    break
            else:
                print(row)


def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    # Filter by city (Chicago, New York, Washington)
    city = get_city()
    city_file = pd.read_csv(city)
    # Filter by time period (month, day, none)
    time_period = get_time_period()
    print('Calculating the first statistic...')

    # What is the most popular month for start time?
    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    if time_period == 'none':
        start_time = time.time()

        # TODO: call popular_month function and print the results
        popularmonth = popular_month(city_file, time_period)
        print("Most popular month for start time is: " + popularmonth)
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()
        getmonth = 'none'
        popularday = popular_day(city_file, getmonth)
        print("Most popular day of week for start time in month " + getmonth + " is:" + popularday)
        # TODO: call popular_day function and print the results

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

        start_time = time.time()

        # What is the most popular hour of day for start time?
        # TODO: call popular_hour function and print the results
        popular_hour(city_file, getmonth)
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()

        # What is the total trip duration and average trip duration?
        # TODO: call trip_duration function and print the results
        trip_duration(city_file, getmonth)
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()

        # What is the most popular start station and most popular end station?
        # TODO: call popular_stations function and print the results
        start_station, end_station = popular_stations(city_file, getmonth)
        print("Most popular start station and most popular end station are: " + start_station + " & " + end_station)
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()

        # What is the most popular trip?
        # TODO: call popular_trip function and print the results
        trip = popular_trip(city_file, getmonth)
        print("Most popular trip" + trip)
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()

        # What are the counts of each user type?
        # TODO: call users function and print the results
        users(city_file, getmonth)
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()

        # What are the counts of gender?
        # TODO: call gender function and print the results
        try:
            gender(city_file, getmonth)
        except KeyError:
            print("Washington file doesn't have Gender")


        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()

        # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
        # most popular birth years?
        # TODO: call birth_years function and print the results
        try:
            birth_years(city_file, getmonth)
        except KeyError:
            print("Washington file doesn't have Birth year")
        print("That took %s seconds." % (time.time() - start_time))
    elif time_period == 'month':
        start_time = time.time()

        # TODO: call popular_month function and print the results
        popularmonth = popular_month(city_file, time_period)
        print("Most popular month for start time is: " + popularmonth)
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()
        getmonth = get_month()
        popularday = popular_day(city_file, getmonth)
        print("Most popular day of week for start time in month " + getmonth + " is:" + popularday)
        # TODO: call popular_day function and print the results

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")

        start_time = time.time()

        # What is the most popular hour of day for start time?
        # TODO: call popular_hour function and print the results
        popular_hour(city_file, getmonth)
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()

        # What is the total trip duration and average trip duration?
        # TODO: call trip_duration function and print the results
        trip_duration(city_file, getmonth)
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()

        # What is the most popular start station and most popular end station?
        # TODO: call popular_stations function and print the results
        start_station, end_station = popular_stations(city_file, getmonth)
        print("Most popular start station and most popular end station are: " + start_station + " & " + end_station)
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()

        # What is the most popular trip?
        # TODO: call popular_trip function and print the results
        trip = popular_trip(city_file, getmonth)
        print("Most popular trip" + trip)
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()

        # What are the counts of each user type?
        # TODO: call users function and print the results
        users(city_file, getmonth)
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()

        # What are the counts of gender?
        # TODO: call gender function and print the results
        try:
            gender(city_file, getmonth)
        except KeyError:
            print("Washington file doesn't have Gender")

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()

        # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
        # most popular birth years?
        # TODO: call birth_years function and print the results
        try:
            birth_years(city_file, getmonth)
        except KeyError:
            print("Washington file doesn't have Birth year")
        print("That took %s seconds." % (time.time() - start_time))
    elif time_period == 'day':
        start_time = time.time()
        print("Enter the day in 'Sunday','Monday' format")
        print("Calculating the next statistic...")
        # TODO: call popular_day function and print the result
        # What is the most popular hour of day for start time?
        # TODO: call popular_hour function and print the results
        getday = get_day()
        popular_hour(city_file, getday)
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()

        # What is the total trip duration and average trip duration?
        # TODO: call trip_duration function and print the results
        trip_duration(city_file, getday)
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()

        # What is the most popular start station and most popular end station?
        # TODO: call popular_stations function and print the results
        start_station, end_station = popular_stations(city_file, getday)
        print("Most popular start station and most popular end station are: " + start_station + " & " + end_station)
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()

        # What is the most popular trip?
        # TODO: call popular_trip function and print the results
        trip = popular_trip(city_file, getday)
        print("Most popular trip" + trip)
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()

        # What are the counts of each user type?
        # TODO: call users function and print the results
        users(city_file, getday)
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()

        # What are the counts of gender?
        # TODO: call gender function and print the results
        try:
            gender(city_file, getday)
        except KeyError:
            print("Washington file doesn't have Gender")

        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()

        # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
        # most popular birth years?
        # TODO: call birth_years function and print the results
        try:
            birth_years(city_file, getday)
        except KeyError:
            print("Washington file doesn't have Birth year")
        print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    display_data(city_file)

    # Restart?
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()


if __name__ == "__main__":
    try:
        statistics()
    except IOError:
        print("File not found\n")
    except Exception as e:
        print(e.message)
    restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()
