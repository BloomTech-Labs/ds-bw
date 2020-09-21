from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

'''
function for calling sentiment score on data
'''


def sentiment_score(comment: str) -> float:
    sentiment_dict = sia.polarity_scores(sentence)
    return sentiment_dict['compound']
