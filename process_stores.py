import csv


def process_file(filename, cutoff_date=None):
        # So what do we want?
        total_tweets = 0
        tweets_with_numbers = 0
        tweets_with_numbers_and_links = 0

        # Read the CSV
        f = open(filename, 'rt')
        try:
                reader = csv.reader(f)
                for tweet in reader:
                        total_tweets += 1
        # For each tweet increment the relevent counter.
        # Return the tubule of the numbers
        finally:
                f.close()
        return (total_tweets,
                tweets_with_numbers,
                tweets_with_numbers_and_links)


print process_file('doug.csv')
