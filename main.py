# -*- coding: utf-8 -*-
"""
Created on Sat May  5 18:51:11 2018

@author: TheJouleThief
"""

import re
import praw
from datetime import datetime as dt

s =""
frequency = {}
time = dt.now()
date = str(time.day) +"_" +str(time.month)
print(date)


reddit = praw.Reddit(client_id='',client_secret='',user_agent='RedditScrapper', username=dev_username,password=dev_password)

username = input("Input username to query.\n")
filename = username + "_Comments_" + date  + "'.txt"
text_file = open(filename,"w")

user = reddit.redditor(username)

for comment in user.comments.new(limit=1000):
    s=s+comment.body

#print(s)
#text_file.write(s)


text_string = s.lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)

for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1;

for word in frequency:
	text_file.write(word)
	text_file.write(',')
	text_file.write(str(frequency[word]) + '\n')

text_file.close()
    
