# HackerLand Enterprise is adopting a new viral advertising strategy. When they launch a new product, they advertise it to exactly  people on social media.

# On the first day, half of those  people (i.e., ) like the advertisement and each shares it with  of their friends. At the beginning of the second day,  people receive the advertisement.

# Each day,  of the recipients like the advertisement and will share it with  friends on the following day. Assuming nobody receives the advertisement twice, determine how many people have liked the ad by the end of a given day, beginning with launch day as day .

# For example, assume you want to know how many have liked the ad by the end of the  day.


# 1) divide the no. of recipients by 2

total_liked = 0
    
recipients = 5

for x in range(3):

    liked = recipients // 2

    total_liked += liked

    recipients = liked * 3


print(total_liked)