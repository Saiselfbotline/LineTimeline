#coding: utf-8
from LineTimeline import *
import time

client = LineTimeline("Your Token")

while True:
    feed = client.getFeed()
    for x in feed["result"]["feeds"]:
        if x["post"]["postInfo"]["liked"] == False:
            client.likePost(x["post"]["postInfo"]["postId"])
    time.sleep(60)
