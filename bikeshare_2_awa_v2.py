import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data! Please choose one of the three available cities Chicago, New York City and Washingthon.')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Enter the name of the city you want to analyze: ').lower()


    while city not in CITY_DATA:
            print('City name is invalid! Please try another one.')
            city = input('Enter the name of the city you want to analyze: ').lower()

    if city in CITY_DATA:
        print('City chosen: {}'.format(city.title()))

    # aks user if they want to filter for month
    print('Do you want to set a filter for month?')
    filter_month = input('Enter "yes" or "no":' ).lower()

    if filter_month == 'no':
        month = 'all'
    else:

    # get user input for month (all, january, february, ... , june)
        months = ['all', 'january','february', 'march', 'april', 'may', 'june']
        month =input('Enter the name  of the month you want to analyze: ').lower()

        while month not in months:
            print('Input is invalid! Please try another one.')
            month =input('Enter the name  of the month you want to analyze: ').lower()

        if month in months:
            print('Month chosen: {}'.format(month.title()))

    # aks user if they want to filter for day
    print('Do you want to set a filter for weekday?')
    filter_day = input('Enter "yes" or "no":' ).lower()

    if filter_day == 'no':
        day = 'all'
    else:

    # get user input for day of week (all, monday, tuesday, ... sunday)
        days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day =input('Enter the name of the weekday you want to analyze: ').lower()

        while day not in days:
         print('Input is invalid! Please try another one.')
         day =input('Enter the name of the weekday you want to analyze: ').lower()

        if day in days:
             print('Weekday chosen: {}'.format(day.title()))


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    #columns for month and day
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()

    # filter for month and day

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df = df[df['month'] == month]

    if day != 'all':
        days = { 'monday':0, 'tuesday':1, 'wednesday':2, 'thursday':3, 'friday':4, 'saturday':5, 'sunday':6}
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)

    # display the most common day of week
    df['day'] = df['Start Time'].dt.weekday
    popular_day = df['day'].mode()[0]
    print('Most Popular Day:', popular_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return popular_month, popular_day, popular_hour

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)

    # display most frequent combination of start station and end station trip
    combination_of_start_and_end_station = df['Start Station'] + df['End Station']
    popular_combination = combination_of_start_and_end_station.mode()[0]
    print('Most Popular Combination of Start and End Station:', popular_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return popular_start_station, popular_end_station, popular_combination

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', int(total_travel_time))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', int(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return total_travel_time, mean_travel_time

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of User Types: ', user_types)
    print('\n')

    # Display counts of gender
    if 'Gender'in df. columns:
        genders = df['Gender'].value_counts()
        print('Counts of Genders: ', genders)
    else:
        print('No stats for gender available for this city.')

    print('\n')
    # Display earliest, most recent, and most common year of birth


    if'Birth Year' in df.columns:
        earliest_year = df['Birth Year'].min()
        latest_year = df['Birth Year'].max()
        popular_year = df['Birth Year'].mode()[0]
        print('Eearliest Year of Birth: ', int(earliest_year))
        print('Latest Year of Birth: ', int(latest_year))
        print('Most Common Year of Birth: ', int(popular_year))
    else:
        print('No stats for birth year available for this city.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return

def view_trip_data(df):
    """ asks the user if they want to see idividal trip data
        returns:
         5 rows of data as long as the input is yes """

    print('Would you like to view 5 rows of individual trip data?')
    view_data = input('Enter "yes" or "no":' ).lower()

    start_loc = 0

    while view_data =='yes':
        print(df.iloc [0:5])
        start_loc += 5
        view_data = input('Would you like to see more rows? Enter "yes" or "no": ').lower()
        if view_data != 'yes':
            break
    return


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_trip_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
