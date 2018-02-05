from secrets import *
import tweepy
import os
from urllib.request import urlopen, Request
import urllib.request
import time
from bs4 import BeautifulSoup

SUBREDDIT="url_of_subreddit"
postedTXT="posted.txt"
auth = tweepy.OAuthHandler("C_key", "SK_key")
auth.set_access_token("A_token", "A_sk_token")
api = tweepy.API(auth)

def deleteAllTweets():
    for status in tweepy.Cursor(api.user_timeline).items():
        api.destroy_status(status.id)

def already_tweeted(url):#check if already posted
    found = False
    with open(postedTXT, 'r') as in_file:
        for line in in_file:
            if url in line:
                found = True
                break
    return found

def addPostedTweets(url):
    if not os.path.exists(postedTXT):
        os.makedirs(postedTXT)

    with open(postedTXT, 'a') as out_file:
        out_file.write(url + '\n')

def tweetImage(url, message):
    fileName = 'temp.jpg'
    folderName = 'temp_media'

    if not os.path.exists(folderName):
        os.makedirs(folderName)

    try:
        urllib.request.urlretrieve(url, os.path.join(folderName, fileName))
        api.update_with_media(folderName + '/' + fileName, status=message)
        addPostedTweets(url)
        os.remove(folderName + '/' + fileName)
    except:
        print("Unable to download image:",url)

def getSourceCode(url):
    response = urllib.request.urlopen(Request(url, headers={'User-Agent': 'Chrome'})).read()
    return  str(response,'utf=8')

def getPhotoLinks(html):
    photoLinks = []
    # photoLinks = re.findall(r'data-url="(.*?.jpg)"', html)
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('div'):  # Get All Images
        if link.has_attr('data-url'):
            if "imgur.com" in str(link.get('data-url')) and not "jpg" in str(link.get('data-url')) and not "png" in str(
                    link.get('data-url')):
                photoLinks.append(link.get('data-url') + ".jpg")
            else:
                photoLinks.append(link.get('data-url'))
    return photoLinks

def getPhotoMessage(html):
    photoMessage = []
    # photoMessage = re.findall(r'<a .* >(.*)</a>', html)
    soup = BeautifulSoup(html, 'html.parser')
    for link in soup.find_all('a'):  # Get All Messages
        if link.has_attr('data-event-action') and link.get("data-event-action") == "title":
            photoMessage.append(link.getText())
    return photoMessage

def main():
    try:
        html = getSourceCode(SUBREDDIT)
        photoLinks=getPhotoLinks(html)
        photoMessage=getPhotoMessage(html)

        for i in range(len(photoLinks)):
            actualUrl=photoLinks[i]
            actualMessage=str(photoMessage[i])
            if not "My" in actualMessage and not "my" in actualMessage and not already_tweeted(actualUrl):
                tweetImage(actualUrl,actualMessage)

        print("See u in 30 minutes")
        time.sleep(1800)
        main()
    except urllib.error.HTTPError:
        print("To Many Requests")
        time.sleep(300)
        main()

if __name__ == '__main__':
    main();
