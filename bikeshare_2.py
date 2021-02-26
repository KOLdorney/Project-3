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
   cities = [chicago, new york city, washington]
    while True:
        city = input("\nWhich city would you like info for?\n")
        city = city.lower()
        if city in cities:
            break
        else:
            print("No city detected. Check for spelling")

    # get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input("Which of the first six months would you like to filter the results by, or to avoid filtering type 'all'\n")
        month = month.lower()
        if month in months:
           break
        else:
           print("No month detected. Check for spelling.")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = input("Which day of the week would you like to filter by, or to avoid filtering type 'all'\n")
        day = day.lower()
        if day in days:
            break
        else:
            print("No day detected. Check for spelling.")

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
    #I loaded the code titleing in this function from practice problem #3 to help with structuring

    # load data file into a dataframe

    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':

        # use the index of the months list to get the corresponding int

        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe

        df = df[df['month'] == month]

    # filter by day of week if applicable

    if day != 'all':

        # filter by day of week to create the new dataframe

        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
                                    #|most common month calculation|
    print("\nThe most common month is", df['month'].mode()[0])

    # display the most common day of week
                                    #|most common day calculation|
    print("\nThe most common day is", df['day_of_week'].mode()[0])

    # display the most common start hour

    df['hour'] = df['Start Time'].dt.hour
    print("\nThe most common start hour is", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
                                                      #|Most common start calculation|
    print("\nThe most commonly used start station is", df['Start Station'].mode()[0])

    # display most commonly used end station
                                                    #|Most common end calculation|
    print("\nThe most commonly used end station is", df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    df['combination'] = (df['Start Station'] + df['End Station']).mode()[0]
    print("\nThe most common start to end trip is", df['combination'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
                                        #|total time calculation|
    print("\nThe total travel time is", df['Trip Duration'].sum())

    # display mean travel time
                                     #|mean time calculation|
    print("\nThe total mean time is", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
                                                #|calc that gets data of customer type counts|
    print("The count of user types:" + '\n' + str(df['User Type'].value_counts()))
    # Display counts of gender
    if city != 'washington':                    #|calc that gets strings of gender type counts|
        print("Count per user gender:" + "\n" + str(df['Gender'].value_counts()))
        # Display earliest, most recent, and most common year of birth

        #prints earliest DOB       |DOB calculation for min|
        print('\nEarliest Year of Birth:', df['Birth Year'].min())
        #prints latest DOB          |DOB calculation for max|
        print('\nMost Recent Year of Birth:', df['Birth Year'].max())
        #prints most common DOB    |DOB calculation for most common|
        print('\nMost Common Year of Birth:', df['Birth Year'].mode()[0])
        #else statement so there is no confusion from user on washington data
    else:
        print("\nWashington has no info on gender or D.O.B.\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    num = 0
    while True:
        raw = input('\nEnter yes for the 5 raw rows\n')
        if raw.lower() == 'yes':
            num = num+5
            print(df[num:num+5])
        elif raw.lower() == 'no':
            break
        else:
            print("Sorry I can't recognize that. yes or no?")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
