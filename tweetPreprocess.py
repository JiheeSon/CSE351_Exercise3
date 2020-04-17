import pandas as pd
import numpy as np
from nltk.stem.porter import *
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


train  = pd.read_csv('train_E6oV3lV.csv')
# test = pd.read_csv('test_tweets_anuFYb8.csv')
finalFile = train

def remove_pattern(input_txt, pattern):
    r = re.findall(pattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)

    return input_txt

# remove twitter handles (@user)
finalFile['tidy_tweet'] = np.vectorize(remove_pattern)(finalFile['tweet'], "@[\w]*")

# remove special characters, numbers, punctuations
finalFile['tidy_tweet'] = finalFile['tidy_tweet'].str.replace("[^a-zA-Z]", " ")

# Removing Short Words
finalFile['tidy_tweet'] = finalFile['tidy_tweet'].apply(lambda x: ' '.join([w for w in x.split() if len(w) > 3]))

tokenized_tweet = finalFile['tidy_tweet'].apply(lambda x: x.split())

# stemmer = PorterStemmer()
# tokenized_tweet = tokenized_tweet.apply(lambda x: [stemmer.stem(i) for i in x]) # stemming

for i in range(len(tokenized_tweet)):
    tokenized_tweet[i] = ' '.join(tokenized_tweet[i])

finalFile['tidy_tweet'] = tokenized_tweet
finalFile.drop(["tweet"], axis = 1, inplace = True)
# print(finalFile.head())
finalFile.to_csv(r'preprocess_train_data.csv', index = False)
# finalFile.to_csv(r'preprocess_test_data.csv', index = False)

