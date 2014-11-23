

import twitter4j.Twitter;
import twitter4j.TwitterFactory;
import twitter4j.conf.ConfigurationBuilder;

/** produces the objects that interfact with Twitter
 * @model
 * @author josephreddington
 *
 */
public class TwitApplicationFactory {

	/**
	 * @model
	 * @return a Twitter object for the 'botofgrammar' account and application
	 */
	public static Twitter getBotOfGrammarTwitter() {
		ConfigurationBuilder cb = new ConfigurationBuilder();
		cb.setDebugEnabled(true).setOAuthConsumerKey("EpyBWKZpkpOekWSljCP70Q")
		.setOAuthConsumerSecret("Wtn2Lgiy1akLKeK2gpKKiqvFu5yLtsbUKTreMo2lU74")
		.setOAuthAccessToken("71890123-uoSmdJud0cFBqo9qfjcfwPayJZl1s2zm7LGcZOgzE")
		.setOAuthAccessTokenSecret("AEW198U51lfMvA5MBK5Kq5S9j85UArQiFNBseyqOI");
		TwitterFactory tf = new TwitterFactory(cb.build());
		Twitter twitter = tf.getInstance();
		return twitter;
	}

	/**
	 * @model
	 * @return a Twitter object for the 'joereddington' account and application
	 */
	public static Twitter getjoereddingtonTwitter() {
		ConfigurationBuilder cb = new ConfigurationBuilder();
		cb.setDebugEnabled(true).setOAuthConsumerKey("Dbc7aPzp6QOEog5RlHplA")
				.setOAuthConsumerSecret("3jPHSkzQdFjGll6FZxAMEpaAJccJ7AXg4kP8jv1Y7nY")
				.setOAuthAccessToken("18700332-laoON1Y7n0qXZiRhClilE2jRIgDWQY0qpJB8QI4FD")
				.setOAuthAccessTokenSecret("t6qAuZwJN82xS2Vssm57rmghWHwx7X95lutNqU7IqdQ");
		TwitterFactory tf = new TwitterFactory(cb.build());
		Twitter twitter = tf.getInstance();
		return twitter;
	}

}
