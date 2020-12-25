#!/usr/bin/python3
import json
import datetime

data = json.load(open("383924.json"))
year = int(data['event'])
members = data['members']

table = []
for id, member in members.items():
    name = member['name']
    score = int(member['local_score'])
    days = member['completion_day_level']

    if not name or not days:
        continue

    progress = {}
    for day, completion in days.items():
        startTime = datetime.datetime(year, 12, int(day), 6, 0, 0)

        star = []
        for n in ['1', '2']:
            if n in completion:
                ts = datetime.datetime.fromtimestamp(int(completion[n]['get_star_ts']))                
                star.append(ts - startTime)
                startTime = ts

        progress[day] = star

    table.append({
        "name": name,
        "score": score,
        "progress": progress
    })

table.sort(key=lambda x: x['score'])    

for member in table:
    name = member['name']
    score = member['score']
    progress = member['progress']

    print("# ({1}) {0} ".format(name, score))
    for day in sorted(progress.keys()):
        print("  ", day + ": ", end="")
        for star in range(len(progress[day])):
            print("{0:>10} ".format("+" + str(progress[day][star])), end="")
        print()
