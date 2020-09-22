from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

'''
function for calling sentiment score on data
'''


def pos_sentiment_score(comment: str) -> float:
    sentiment_dict = sia.polarity_scores(comment)
    return sentiment_dict['compound']


def neg_sentiment_score(comment: str) -> float:
    sentiment_dict = sia.polarity_scores(comment)
    return -sentiment_dict['compound']
