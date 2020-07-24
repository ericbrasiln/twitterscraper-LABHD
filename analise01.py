import pandas as pd

df = pd.read_csv('/home/ebn/Documentos/Python/twitterscraper/twint/cr.csv', encoding='UTF-8')
#print(df.iloc[:,7])
df2 = df.drop(columns=['conversation_id', 'user_id', 'created_at', 'timezone', 'place', 'mentions', 'replies_count', 'retweets_count',
              'likes_count', 'cashtags', 'quote_url', 'near', 'geo', 'source', 'user_rt_id', 'retweet_date',
              'translate', 'trans_src', 'trans_dest', 'user_rt', 'retweet_id', 'reply_to'])
df2.info()
print(df2.head())
print(df2.loc[[0,1,2,3,4,5,6]])
