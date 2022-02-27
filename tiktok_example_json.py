from TikTokApi import TikTokApi

api = TikTokApi()

count = 1

for video in api.hashtag(name="funny").videos(count=count):
    print(video)


user = api.user(username='rotififi')
print(user.as_dict)
for video in user.videos(count=count):
    print(video)
