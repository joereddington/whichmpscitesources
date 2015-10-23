import csv
import re


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
                        if re.match(".* \\d+,*\\d* .*", tweet[2]):
                                tweets_with_numbers += 1
                                if "http" in tweet[2]:
                                        tweets_with_numbers_and_links += 1
        finally:
                f.close()
        return (total_tweets,
                tweets_with_numbers,
                tweets_with_numbers_and_links)


print process_file('doug.csv')
