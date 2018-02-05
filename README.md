# Easy-Reddit-twitterBOT
Easily configurable bot that can reflect any subreddit photos to twitter

## Prepare the environment

Download or clone the project  
```
git clone https://github.com/MrDasix/Easy-Reddit-twitterBOT.git
```

Enter the new folder created that contains the scripts 
```
cd Easy-Reddit-twitterBOT\EasyBot
```

Install python if you don't have it installed
```
sudo apt get install python3
```

Install pìp
```
sudo apt-get install python-pip
```

Install tweepy
```
sudo pip install tweepy
```

Install Beautiful Soup 4
```
sudo pip install bs4
```

## Set up the bot

Open bot.py 

    1) Replace the variabe SUBREDDIT for the url of the subreddit that you want to mirror
    2) Replace the values C_key, SK_key, A_token and A_sk_token with the the necessary keys of your twitter account
```
auth = tweepy.OAuthHandler("C_key", "SK_key")
auth.set_access_token("A_token", "A_sk_token")
```

All this keys and tokens can be found in your app found in [https://apps.twitter.com/](https://apps.twitter.com)

## Run the bot

Execute in the shell
```
python3 bot.py
```

