import numpy as np
import time
import pandas as pd


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

     while True:
        city = input('Please type the city you want to analyze from Chicago,\
                     New York city or Washington: ').lower()

        if  city not in ('chicago','new york city','washington'):
            print("Sorry, try again and make sure the city is correct")

        else:
            break

     while True:
        month = input('Please type the month you want to analyze from January to June.\
                      If you don\'t want to filter, tipe "all".: ').lower()

        if month not in ('january','february','march','april','may','june','all'):
            print("Sorry, try again and make sure the month is correct.")

        else:
            break

     while True:
        day = input('Please type the day of the week you want to analyze.\
                    If you don\'t want to filter, tipe "all".: ').lower()

        if day not in ('monday','tuesday','wednesday','thursday',\
                       'friday','saturday','sunday','all'):
            print("Sorry, try again and make sure the day is correct.")

        else:
            break

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
        df - pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    file = city.replace(' ','_')+'.csv'
    df = pd.read_csv(file)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        #filter by day of week to create the new dataframe
        days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        day = days.index(day)+1
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    #Register start time for function time_stats
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month_mf = months[df['month'].mode()[0]-1]
    print('The most common month of travel is {}'.format(month_mf.title()))

    # TO DO: display the most common day of week
    days_of_week = ['monday','tuesday','wednesday','thursday',
            'friday','saturday','sunday','all']
    dow_mf = days_of_week[df['day_of_week'].mode()[0]-1]
    print('The most common day of travel is {}'.format(dow_mf.title()))


    # TO DO: display the most common start hour
    print('The most common start hour is {}h'.format(df['Start Time'].dt.hour.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most popular start station is {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('The most popular end station is {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    print('The most frequent combination of start and en station in a a trip are {}'\
    .format(df.groupby(['Start Station', 'End Station']).size().idxmax()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total travel time is {} seconds'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('The average travel time is {} seconds'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('These are the type of users and the count for each type')
    print(df['User Type'].value_counts())


    # TO DO: Display counts of gender
    print('The count of gender is the following')
    print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    print('Below you can find the earliest, most recent and most common year of birth')
    print(df['Birth Year'].min())
    print(df['Birth Year'].max())
    print(df['Birth Year'].mode()[0])

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
        if restart.lower() == 'yes':
            continue
        else:
            break


if __name__ == "__main__":
	main()
