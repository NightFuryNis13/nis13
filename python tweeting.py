# importing the module

import tweepy

# personal details
consumer_key ="6666666666666666"
consumer_secret ="6666666666666666"
access_token ="666666666666666"
access_token_secret ="66666666666666"

# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# update the status
api.update_status(status ="yo??")
