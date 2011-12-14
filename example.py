"""
	An example Python client for the Chatterbox Analytics Sentiment Detection API
	delivered through the Mashape platform.  The API is designed specifically
	for short social texts.

	This client has some hard coded (but real) tweets which are passed to the
	API.

	You need to add your Developer Keys found on the Mashape Dashboard and subscribe
	to a plan on the Mashape API page (http://www.mashape.com/apis/Sentiment+Analysis/pricing)
"""
from SentimentAnalysis import SentimentAnalysis
#add your keys below
public_key = ""
private_key = ""

#build the API object with your keys
chatterboxapi = SentimentAnalysis(public_key, private_key)

#Our hard coded sample tweets.  Your application will figure out 
#what it needs...
sampletexts = ["@getflockler must have a great designer cause it looks hot!! :-)",
	"I've started exploring Evernote... this may change my life.. I'm not sure yet, but it may.",
	"Well, Saudi Airlines have really messed up our holiday. Pretty pissed off they can get away with it.",
	"How did someone make it to our site using the keywords: \"different types of birth control\"? #odd",
	"Apple Mail, why do you crash so? #grrrr",
	"If you ever wonder 'how bad can a coffee from burger king be, really?' the answer is bad, very bad. #badcoffeebadmorning",
	"Great meeting with TK from the Queen Mary student paper - really interesting questions!"]

highestnumber = 0
highesttext = False

try:
	for sampletext in sampletexts:
		print "Text: " + sampletext
		
		#Here we do the actual classification.  We pass in a language
		#identifier and the text we wish to be classified.
		classification = chatterboxapi.classifytext("en",sampletext)
		
		#Uncomment this line if you want to inspect the result.
		#print classification
		
		#Value is the predicted strength of the sentiment in the text
		sentiment_value = classification['value']
		
		if sentiment_value > highestnumber:
			highestnumber = sentiment_value
			highesttext = sampletext
			
		#Sent is the sentiment class. 1 is positive, -1 is negative
		sentiment_label = classification['sent']
		
		if abs(sentiment_value) < 0.25:
			#As a consumer of this API you will need to experiment with
			#which cut-off value works best for your application.
			print "WEAK: Hmm. Weak or netural sentiment it seems"
		elif sentiment_label > 0:
			print "POS: W00t! Seems like a positive message"
		else:
			print "NEG: Oh foo. Seems like a negative one"

	print "The most positive message is", highesttext
except KeyError:
	#Errors should be handled more elegantly than this.
	print classification