import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
MONTHS_LIST =  ['january', 'february', 'march', 'april',
            'may', 'june','all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    while True:
        # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

        city = input(
            "Welcome to the US Bike Share Mariobros! \n Which city would you like to explore, Washington, New York City or Chicago?\n").lower()
        if city not in ['chicago', 'new york city', 'washington']:
            print("Sorry, I do not understand your input. Please input either chicago, new york city, or Washington.")
            continue

        # get user input for month (all, january, february, ... , june)

        month_input = input("Please enter which month.\n").lower()
        if month_input not in MONTHS_LIST:
            print("Sorry, enter a valid month (January, February, etc).\n")
            continue
        else:
            if(month_input == "all"):
                month = -1
            else:
                month = MONTHS_LIST.index(month_input)+1


        # get user input for day of week (all, monday, tuesday, ... sunday)

        day_input = input("Please enter which day.\n").lower()
        if day_input not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            print("Sorry, please enter a valid day  (Monday, Tuesday, etc.)\n")
            continue
        else:
            if(day_input == "all"):
                day = ""
            else:
                day = day_input.capitalize()

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
    df = pd.read_csv(CITY_DATA[city], parse_dates= ["Start Time","End Time"])
    if(month > 0):
        df = df[df["Start Time"].dt.month == month]
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.day_name.html#pandas.Series.dt.day_name
    if(day != ""):
        df = df[df["Start Time"].dt.day_name() == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print(df["Start Time"].dt.month.value_counts())
    print(df["Start Time"].dt.month.value_counts().idxmax())
    print("You have selected the month: ")
    print(MONTHS_LIST[
        df["Start Time"].dt.month.value_counts().idxmax()-1
        ])

    # display the most common day of week
    print("You have selected the day: ")
    print(df["Start Time"].dt.day_name().value_counts().idxmax())
    print("How many times: " + str(df["Start Time"].dt.day_name().value_counts().max()))


    # display the most common start hour
    print("The most common start hour: ")
    print(df["Start Time"].dt.hour.value_counts().idxmax())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print("The most common used start station")
    print(df["Start Station"].value_counts().idxmax())


    # display most commonly used end station
    print("The most common used End station")
    print(df["End Station"].value_counts().idxmax())

    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("The total travel time")
    print(df["Trip Duration"].sum())


    # display mean travel time
    print("The mean travel time")
    print(df["Trip Duration"].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User types')

    print(df["User Type"].value_counts())


    # Display counts of gender
    print('User gender')
    if("Gender" in df):
        print(df["Gender"].value_counts())
    else:
        print('N/A')


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
