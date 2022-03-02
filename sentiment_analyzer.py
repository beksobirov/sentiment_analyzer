from nltk.sentiment import  SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

print(sia.polarity_scores('Programming is fun'))
# {'neg': 0.0, 'neu': 0.377, 'pos': 0.623, 'compound': 0.5106}

print(sia.polarity_scores('It is bad weather today'))
# {'neg': 0.467, 'neu': 0.533, 'pos': 0.0, 'compound': -0.5423}