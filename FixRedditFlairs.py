import praw
import os

subredditName = 'SUBREDDIT_NAME'  # Name of subreddit to make edits to (without the r/)
cssClass = ''                     # Name of the CSS class to change to (empty by default)
flairClassMatch = 'CSS_CLASS'     # Name of the CSS class to make changes to
keywordMatch = ''                 # Text of the CSS class to match with (will match to empty flairs by default)

reddit = praw.Reddit(client_id=os.environ.get('client_id'),
                     username=os.environ.get('praw_username'),
                     password=os.environ.get('praw_password'),
                     client_secret=os.environ.get('client_secret'),
                     user_agent="Remove Flair Script")
usersChanged = []

for userFlairInfo in reddit.subreddit(subredditName).flair(limit=None):
    if userFlairInfo.get('flair_text') == keywordMatch:
        if userFlairInfo.get('flair_css_class') == flairClassMatch:
            reddit.subreddit(subredditName).flair.set(userFlairInfo.get('user'), "", css_class=cssClass)
            usersChanged.append(userFlairInfo.get('user'))
            print(userFlairInfo.get('user'))
print(usersChanged)
print("Modified flairs for " + str(len(usersChanged)) + " users.")
