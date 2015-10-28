#!/usr/bin/env python
# encoding: utf-8
import tweepy  # https://github.com/tweepy/tweepy
import csv
"""So here is the plan.

Read the twitter for each MP and place in text files.
    -   Partly to keep the code as it is
    -   Partly in case of interupted signal (do we have this file? Okay move on)
    -   Partly so people can check the work

Then read the text files - create a table of MPs and their links,
    -   sort table
    -   produce HTML automatically
    -   Two versions - one with the >5 tweets and one without


"""
# Twitter API credentials
# from http://stackoverflow.com/a/29479549/170243
try:
        from configparser import ConfigParser
except ImportError:
        from ConfigParser import ConfigParser  # ver. < 3.0
config = ConfigParser()
config.read('keys.ini')
consumer_key = config.get('twitter', 'consumer_key')
consumer_secret = config.get('twitter', 'consumer_secret')
access_key = config.get('twitter', 'access_key')
access_secret = config.get('twitter', 'access_secret')


def get_all_handles(filename):
        """Returns all of the twitter handles in the filename"""
        file = open(filename)
        screennames = []
        for rawline in file:
                splitline = rawline.split('@')
                screennames.insert(0, splitline[1])
        return screennames


def get_all_tweets(screen_name):
                # Twitter only allows access to a users most recent 3240 tweets with
                # this method

                # authorize twitter, initialize tweepy
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        api = tweepy.API(auth, wait_on_rate_limit=True)

        # initialize a list to hold all the tweepy Tweets
        alltweets = []

        # make initial request for most recent tweets (200 is the maximum
        # allowed count)
        try:
                new_tweets = api.user_timeline(
                    screen_name=screen_name,
                    count=200)
        except tweepy.TweepError as e:
                if "Not authorized." in e.message:
                        print "The user {} appears to NOT exist".format(screen_name)
                        return
        user = api.get_user(screen_name)
        top_line = (
            user.screen_name,
            user.name,
            user.description,
            user.followers_count,
            user.statuses_count,
            user.url)
        # save most recent tweets
        alltweets.extend(new_tweets)
        # some people have NO tweets
        if len(alltweets) == 0:
                return
        # save the id of the oldest tweet less one
        oldest = alltweets[-1].id - 1

        # keep grabbing tweets until there are no tweets left to grab
        while len(new_tweets) > 0:
                print "getting tweets before %s" % (oldest)

                # all subsiquent requests use the max_id param to prevent
                # duplicates
                new_tweets = api.user_timeline(
                    screen_name=screen_name,
                    count=200,
                    max_id=oldest)

                # save most recent tweets
                alltweets.extend(new_tweets)

                # update the id of the oldest tweet less one
                oldest = alltweets[-1].id - 1

                print "...%s tweets downloaded so far" % (len(alltweets))

        # transform the tweepy tweets into a 2D array that will populate the csv
        outtweets = [
            [tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")]
            for tweet in alltweets]

        # write the csv
        with open('%s_tweets.csv' % screen_name.strip(), 'wb') as f:
                writer = csv.writer(f)
                writer.writerow(top_line)
                writer.writerows(outtweets)

        pass


if __name__ == '__main__':
        names = get_all_handles('mps.txt')
        for mp in names:
                get_all_tweets(mp)
