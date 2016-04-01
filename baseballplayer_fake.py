import sys
import random
import json
import urllib

sb_animals = list()
hit_animals = list()
hr_animals = list()
final_result = list()
quotes_list = list()
productive_cmt = list()
quotes_list1 = list()
quotes_list2 = list()
quotes_list3 = list()

iampoor_lines = list()
for line in open('baseball_quote.txt'):
	line = line.strip()
	if len(line) > 0 :
		quotes_list.append(line)


def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value)
                for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

careerstats = open("harper.json").read()
player_data = json.loads(careerstats)
animal_speed = open("animal_speed.json").read()
fast_animals = json.loads(animal_speed)
animal_productivity = open("animal_productivity.json").read()
productive_animals = json.loads(animal_productivity)
animal_strength = open("animal_strength.json").read()
strong_animals = json.loads(animal_strength)
greekgods = open("greekgods.json").read()
god_dict = json.loads(greekgods)
advs = open("advs.json").read()
advs_dict = json.loads(advs)
adjs = open("adjs.json").read()
adjs_dict = json.loads(adjs)
body = open("body_parts.json").read()
body_dict = json.loads(body)
harper_news = open("harper_news.json").read()
news_dict = json.loads(harper_news)

player_data = byteify(player_data)
fast_animals = byteify(fast_animals)
productive_animals = byteify(productive_animals)
strong_animals = byteify(strong_animals)
god_dict = byteify(god_dict) 
advs_dict = byteify(advs_dict)
adjs_dict = byteify(adjs_dict)
body_dict = byteify(body_dict)
news_dict = byteify(news_dict)

news_title = str(news_dict["response"]["docs"][0]["headline"]["main"])

god_list = god_dict["greek_gods"]
advs_list = advs_dict["adverbs"]

sblevel = player_data[len(player_data)-3]["SB"] / 10 +1
hitlevel = player_data[len(player_data)-3]["H"] / 18
hrlevel = player_data[len(player_data)-3]["HR"] / 4

for item in fast_animals:
	if item["speedlevel"]==sblevel:
		sb_animals.append(item["animal"])
		sb_adv = item["adv"]
		speed_cmt = item["adv"]
for item in productive_animals:
	if item["productivelevel"]==hitlevel:
		hit_animals.append(item["animal"])
		productive_cmt.append(item["comments"])
for item in strong_animals:
	if item["strength level"] ==hrlevel:
		hr_animals.append(item["animal"])
if hrlevel >8:
	hr_animals = god_list

# productive_cmt = productive_cmt[0].split(" ")
# productive_cmt = productive_cmt[1:len(productive_cmt)/2]
# productive_cmt_chosen = " ".join(productive_cmt)

quotes_list1 = random.choice(quotes_list)
quotes_list1 = quotes_list1.split(" ")
quotes_list1 = quotes_list1[1:7]
quotes_list1_chosen = " ".join(quotes_list1)

quotes_list2 = random.choice(quotes_list)
quotes_list2 = quotes_list2.split(" ")
quotes_list2 = quotes_list2[2:8]
# next: make the quote length random
quotes_list2_chosen = " ".join(quotes_list2)

quotes_list3 = random.choice(quotes_list)
quotes_list3 = quotes_list3.split(" ")
quotes_list3 = quotes_list3[3:9]
# next: make the quote length random
quotes_list3_chosen = " ".join(quotes_list3)

final_result.append(player_data[0]["Name"] + ", " + player_data[len(player_data)-3]["Tm"]+" "+str(player_data[0]["Number"]) + ", " + player_data[0]["Nickname"]+", in "+str(player_data[len(player_data)-3]["Year"]))
final_result.append(random.choice(adjs_dict["adjs"])+" "+random.choice(body_dict["bodyParts"])+", "+random.choice(adjs_dict["adjs"])+" "+random.choice(body_dict["bodyParts"])+", "+random.choice(adjs_dict["adjs"])+" "+random.choice(body_dict["bodyParts"]))
final_result.append("hits like a productive "+random.choice(hit_animals))
final_result.append(quotes_list1_chosen+" "+str(player_data[len(player_data)-3]["H"])+" "+"hits")
final_result.append("run "+random.choice(advs_list)+" "+speed_cmt+" like "+ random.choice(sb_animals).lower())
final_result.append(quotes_list2_chosen+" "+str(player_data[len(player_data)-3]["SB"])+" "+"stolen bases")
final_result.append("the "+random.choice(adjs_dict["adjs"])+", "+random.choice(adjs_dict["adjs"])+" "+random.choice(hr_animals)+", "+quotes_list3_chosen)
final_result.append("with "+str(player_data[len(player_data)-3]["HR"])+" homeruns --- "+str(player_data[len(player_data)-3]["Age"])+"-year-old"+" "+player_data[0]["Position"] )
final_result.append(news_title)
# final_result.append(player_data[0]["Name"] + ", " + player_data[len(player_data)-3]["Tm"]+" "+str(player_data[0]["Number"]) + ", " + player_data[0]["Nickname"]+", in "+player_data[len(player_data)-3]["Year"])

# for items in final_result:
# 	for item in items:
# 		item.replace("me", "him")
# 		item.replace("you", "he")
# 		item.replace("I", "he")
# 		item.replace("my", "his")
# 		item.replace("your", "his")

# for datakeys in player_data[0].keys():
# 	print str(datakeys)

# print player_data[len(player_data)-3]["SB"]
# print fast_animals[0]["speedlevel"]
# print player_data[0]["Name"] + " " + str(player_data[0]["Number"])
# print random.choice(sb_animals)
# print random.choice(hit_animals)
# print sb_adv
for lines in final_result:
	print lines






