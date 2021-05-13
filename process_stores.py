from __future__ import division
import csv
import re
import os

"""
TODO:

Add the ratios
Sort output by ratios
Make HTML output



Add links to html
add links to the set of tweets downloaded
cut people who have less than X qualifying tweets
"""

# from https://codereview.stackexchange.com/questions/41298/producing-ordinal-numbers 
SUFFIXES = {1: 'st', 2: 'nd', 3: 'rd'}
def ordinal(num):
    # I'm checking for 10-20 because those are the digits that
    # don't follow the normal counting scheme. 
    if 10 <= num % 100 <= 20:
        suffix = 'th'
    else:
        # the second parameter is a default.
        suffix = SUFFIXES.get(num % 10, 'th')
    return str(num) + suffix

def process_file(filename, database, cutoff_date=None):
        # So what do we want?
        total_tweets = 0
        tweets_with_numbers = 0
        tweets_with_numbers_and_links = 0

        # Read the CSV
        f = open(filename, 'rt')
	#print filename
        try:
                reader = csv.reader(f)
                headings = next(reader, None)
                for tweet in reader:
                        total_tweets += 1
                        if re.match(".* \\d+,*\\d* .*", tweet[2]):
                                tweets_with_numbers += 1
                                if "http" in tweet[2]:
                                        tweets_with_numbers_and_links += 1

                if tweets_with_numbers==0:
                        ratio=0
                else:
                        ratio=tweets_with_numbers_and_links/tweets_with_numbers
		# print headings
		# print "here"
                database[
                    headings[0]] = (
                    headings[1],
                    total_tweets,
                    tweets_with_numbers,
                    tweets_with_numbers_and_links,
                    ratio)
		#print "there"
	except TypeError: 
		pass
        finally:
                f.close()
        return (total_tweets,
                tweets_with_numbers,
                tweets_with_numbers_and_links)


def populate_database():
        import glob
        database = {}
        for f in glob.glob('full/*.csv'):
                process_file(f, database)
        return database

def produce_tweet(database):
        processed_mps=database.iteritems()
        processed_mps=sorted(processed_mps,key=lambda  k:k[1][4], reverse=True)
        rank=0
        for key, value in processed_mps:
                rank+=1
 #               print "{} (@{}): {}, {}, {} {:.2f}%".format(value[0], key, value[1], value[2], value[3], value[4]*100)
                print "Congratulations to {} who ranked {} out of the 585 MPs (that I have data for) for sourcing the figures in their tweets. https://joereddington.com/rankingmps/ ".format(key, ordinal(rank))

def produce_html(database):
        # For each filename
        processed_mps=database.iteritems()
        processed_mps=sorted(processed_mps,key=lambda  k:k[1][4], reverse=True)
        rank=0
        f = open("list.txt", "w")
        for key, value in processed_mps:
                rank+=1
                f.write("<tr><td>{}</td><td>{} </td><td> ({}) </td><td> {} </td><td> {} </td><td> {} </td><td> {:.2f}% </td></tr>".format(rank,value[0], key, value[1], value[2], value[3], value[4]*100))
        f.close()

database=populate_database()
produce_html(database)
produce_tweet(database)

