import java.util.Date;
import java.util.Map;

import twitter4j.Paging;
import twitter4j.RateLimitStatus;
import twitter4j.ResponseList;
import twitter4j.Status;
import twitter4j.Twitter;
import twitter4j.TwitterException;
import twitter4j.User;
import TwitApplicationFactory;

public class ProcessMp {

	public static Twitter twitter;

	public static void main(String[] args) throws TwitterException,
			InterruptedException {
		twitter = TwitApplicationFactory.getjoereddingtonTwitter();
		String username = args[0];
		System.out.println(username);
		User user = twitter.showUser(username.replace("@", ""));
		// ht: from http://www.devmanuals.com/tutorials/java/gettingUserId.html
		checkUser(user);
	}

	@SuppressWarnings("deprecation")
	protected static void checkUser(User user) throws TwitterException,
			InterruptedException {
		int withNumberAndRef = 0;
		int tweets = 0;
		int withNumber = 0;

		for (int i = 1; i < 10; i++) {
			ResponseList<Status> currentlyExaminedStatus = twitter
					.getUserTimeline(user.getId(), new Paging(i, 100));
			for (Status status : currentlyExaminedStatus) {
				Date start = new Date(115, 1, 1);
				if (status.getCreatedAt().before(start)) {
					System.out.println("hey!");
					continue;
				}
				if (status.getText().startsWith("RT")) {
					continue;
				}
				System.out.println(status.getText() + " "
						+ status.getCreatedAt());
				tweets++;
				if (status.getText().matches(".* \\d+,*\\d* .*")) {
					withNumber++;
					if (status.getText().matches(".*http.*")) {
						withNumberAndRef++;
					}
				}
			}
			waitUntilICanMakeAnotherCall();
		}

		System.out.print("XX," + user.getScreenName() + ",");
		System.out.print(user.getName() + ",");
		System.out.print(tweets + ",");
		System.out.print(withNumber + ",");
		System.out.println(withNumberAndRef);

	}

	protected static void waitUntilICanMakeAnotherCall()
			throws TwitterException, InterruptedException {
		{
			Map<String, RateLimitStatus> temp = twitter.getRateLimitStatus();
			RateLimitStatus secondsRemaining = temp
					.get("/statuses/retweets/:id");
			if (secondsRemaining.getRemaining() == 0) {
				Thread.sleep((secondsRemaining.getSecondsUntilReset() + 5) * 1000);
				return;
			}
			int secondstosleep = 1 + secondsRemaining.getSecondsUntilReset()
					/ secondsRemaining.getRemaining();
			Thread.sleep(secondstosleep * 1000);
		}
	}

}
