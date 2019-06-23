# FixRedditFlairs
Emergency script to fix persisting issues due to Reddit bug

### Summary
Reddit recently had a critical bug where user flairs that should be restricted to moderators only were able to be accessed by any public user. Upon investigation, it seems as the flair IDs were overlapped between a public and private flair, and anyone who selected the publicly available flair was also granted the moderator-only flair.

The overlapping IDs have since been fixed, but the changes were not reverted. This script was created as an emergency script to reverse the changes made by Reddit's error.

### Requirements
- Reddit account (modded on the subreddit to make the changes to) with credentials stored as environment variables (praw_username and praw_password)
- Reddit client ID and client secret (from the same account as above) stored as environment variables (client_id and client_secret)
- subredditName = name of the subreddit to make changes to
- cssClass = the CSS class to change the flairs back to
- flairClassMatch = if the flairs were changed to a different CSS class, this will identify the class to match changes to
- keyWordMatch = if the flair has a specific line of text, you can use this to identify what to make changes to

### Dependencies
- **praw** to interact with the Reddit API
- **os** for environment variables