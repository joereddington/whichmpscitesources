
import csv
import re
import os

"""
TODO:

Add the ratios
Sort output by ratios
Make HTML output
Add links to html
cut people who have less than X qualifying tweets

def process_file(filename, database, cutoff_date=None):
        # So what do we want?
        total_tweets = 0
        tweets_with_numbers = 0
        tweets_with_numbers_and_links = 0

        # Read the CSV
        f = open(filename, 'rt')
        try:
                reader = csv.reader(f)
                headings = next(reader, None)
                for tweet in reader:
                        total_tweets += 1
                        if re.match(".* \\d+,*\\d* .*", tweet[2]):
                                tweets_with_numbers += 1
                                if "http" in tweet[2]:
                                        tweets_with_numbers_and_links += 1
                database[
                    headings[0]] = (
                    headings[1],
                    total_tweets,
                    tweets_with_numbers,
                    tweets_with_numbers_and_links)
        finally:
                f.close()
        return (total_tweets,
                tweets_with_numbers,
                tweets_with_numbers_and_links)


def populate_database():
        database = {}
        for f in os.listdir('testdata'):
                process_file('testdata/'+f, database)
        return database


def produce_html(database):
        # For each filename
        for key, value in database.iteritems():
                print "{} (@{}): {}, {}, {}".format(value[0], key, value[1], value[2], value[3])

produce_html(populate_database())
