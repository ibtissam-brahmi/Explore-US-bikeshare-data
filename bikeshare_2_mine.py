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
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=""
    while city not in ["chicago", "new_york_city", "washington"]:
        city = input("Which city you want to explore: chicago, new_york_city or washington? " ).lower()
    # get user input for month (all, january, february, ... , june)
    month=""
    while month not in ["january", "february", "march", "april", "may", "june", "all"]:
        month = input("For which month (from january to june)? all of them? (print all in this case) " ).lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day=""
    while day not in ["monday", "tuesday", "wednesday", "thirsday", "friday", "saturday", "sunday", "all"]:
        day = input("For which day? all of them ? (print all in this case) ").lower()

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
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    filename = city + '.csv'
    df =  pd.read_csv(filename)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    if month != 'all':
        df = df[df['Start Time'].dt.month == months.index(month) + 1]
    if day != 'all':
        df = df[df['Start Time'].dt.weekday_name == day.title()]

    return df


def time_stats(df, city, month, day):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    if month == 'all':
    # display the most common month
        popular_month = df['Start Time'].dt.month.mode()[0]
        print("The most common month in {} is {} ".format(city, popular_month))
    # display the most common day of week
    if day == 'all':
        popular_day = df['Start Time'].dt.weekday_name.mode()[0]
        print("The most common day of week in {} is {}".format(city, popular_day))
    # display the most common start hour
    popular_hour = df['Start Time'].dt.hour.mode()[0]
    print("The most common hour in {} is {} " .format(city, popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df, city, month, day):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_s_station = df['Start Station'].mode()[0]
    print("The most common start station is ", popular_s_station)

    # display most commonly used end station
    popular_e_station = df['End Station'].mode()[0]
    print("The most common end station is ", popular_e_station)

    # display most frequent combination of start station and end station trip
    df['Trip'] = list(zip(df['Start Station'], df['End Station']))
    popular_trip = df['Trip'].mode()[0]
    print("The most common trip is ", popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df, city, month, day):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is ', total_travel_time)
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city, month, day):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts_u_type = df['User Type'].value_counts()
    print('The counts of each user type are: \note', counts_u_type)
    # Display counts of gender
    if city == 'chicago' or city == 'new_york_city':
        counts_gender = df['Gender'].value_counts()
        print('The counts of gender are: \n', counts_gender)
    # Display earliest, most recent, and most common year of birth
        earliest_y_b = min(df['Birth Year'])
        print('The earliest year of birth is: ', earliest_y_b)

        most_recent_y_b = max(df['Birth Year'])
        print('The most recent year of birth is: ', most_recent_y_b)

        common_y_b = df['Birth Year'].mode()[0]
        print('The most common year of birth is: ', common_y_b)
    else:
         print("No gender data or birth date to share")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, city, month, day)
        station_stats(df, city, month, day)
        trip_duration_stats(df, city, month, day)
        user_stats(df, city, month, day)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
