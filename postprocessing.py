from TikTokApi import TikTokApi
import csv
from feedgen.feed import FeedGenerator
from datetime import datetime, timezone

# Normal GitHub Pages URL
ghPagesURL = "https://roastedbill.github.io/tiktok-rss-flat/"

api = TikTokApi()

count = 10

# # user subscriptions
# with open('users.csv') as f:
#     cf = csv.DictReader(f, fieldnames=['username'])
#     for row in cf:
#         user = row['username']
#
#         print(f'Running for user \'{user}\'')
#
#         fg = FeedGenerator()
#         fg.id('https://www.tiktok.com/@' + user)
#         fg.title(user + ' TikTok')
#         fg.author( {'name':'RS','email':'rensheng@lolo.city'} )
#         fg.link( href='http://tiktok.com', rel='alternate' )
#         fg.logo(ghPagesURL + 'tiktok-rss.png')
#         fg.subtitle('OK Boomer, all the latest TikToks from ' + user)
#         fg.link( href=ghPagesURL + 'rss/' + user + '.xml', rel='self' )
#         fg.language('en')
#
#         # Set the last modification time for the feed to be the most recent post, else now.
#         updated=None
#
#         for tiktok in api.user(username=user).videos(count=count):
#             fe = fg.add_entry()
#             link = "https://tiktok.com/@" + user + "/video/" + tiktok.id
#             fe.id(link)
#             ts = datetime.fromtimestamp(tiktok.as_dict['createTime'], timezone.utc)
#             fe.published(ts)
#             fe.updated(ts)
#             updated = max(ts, updated) if updated else ts
#             fe.title(tiktok.as_dict['desc'])
#             fe.link(href=link)
#             fe.description("<img src='" + tiktok.as_dict['video']['cover'] + "' />")
#
#         fg.updated(updated)
#
#         fg.atom_file('rss/' + user + '.xml', pretty=True) # Write the RSS feed to a file

# hashtag subscriptions
with open('hashtags.csv') as f:
    cf = csv.DictReader(f, fieldnames=['hashtag'])
    for row in cf:
        hashtag = row['hashtag']

        print(f'Running for hashtag \'{hashtag}\'')

        fg = FeedGenerator()
        fg.id('https://www.tiktok.com/tag/' + hashtag)
        fg.title('#' + hashtag + ' TikTok')
        fg.author( {'name':'RS','email':'rensheng@lolo.city'} )
        fg.link( href='http://tiktok.com', rel='alternate' )
        fg.logo(ghPagesURL + 'tiktok-rss.png')
        fg.subtitle('OK Boomer, all the latest TikToks about #' + hashtag)
        fg.link( href=ghPagesURL + 'rss/' + hashtag + '.xml', rel='self' )
        fg.language('en')

        # Set the last modification time for the feed to be the most recent post, else now.
        updated=None

        for tiktok in api.hashtag(name=hashtag).videos(count=count):
            fe = fg.add_entry()
            link = "https://tiktok.com/@" + tiktok.author.username + "/video/" + tiktok.id
            fe.id(link)
            ts = datetime.fromtimestamp(tiktok.as_dict['createTime'], timezone.utc)
            fe.published(ts)
            fe.updated(ts)
            updated = max(ts, updated) if updated else ts
            fe.title(tiktok.as_dict['desc'])
            fe.link(href=link)
            fe.description("<img src='" + tiktok.as_dict['video']['cover'] + "' />")

        fg.updated(updated)

        fg.atom_file('rss/' + hashtag + '.xml', pretty=True) # Write the RSS feed to a file