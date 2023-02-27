from collections import defaultdict
file_content = open('input', 'r').readlines()

bots = defaultdict(list)
outputs = defaultdict(list)
actions = dict()

# for i in range(300):
#     bots[str(i)] = []

for line in file_content:
    parts = line.split()
    if parts[0] == 'value':
        bots[parts[5]].append(int(parts[1]))
    else:
        source_bot = parts[1]
        target_low_type = parts[5]
        target_low_id = parts[6]
        target_high_type = parts[10]
        target_high_id = parts[11]
        actions[source_bot] = {
            "target_low_type": target_low_type,
            "target_low_id": target_low_id,
            "target_high_type": target_high_type,
            "target_high_id": target_high_id
        }
zoo = True
while zoo:
    zoo = False
    for key in bots.copy().keys():
        bot = bots[key]
        if len(bot) == 2:
            zoo = True
            low = min(bot)
            high = max(bot)
            if low == 17 and high == 61:
                print("--->", key)
            action = actions[key]
            if action['target_low_type'] == 'bot':
                bots[action['target_low_id']] += [low]
            else:
                outputs[action['target_low_id']] += [low]
            if action['target_high_type'] == 'bot':
                bots[action['target_high_id']] += [high]
            else:
                outputs[action['target_high_id']] += [high]
            bots[key] = []
print(outputs['0'][0] * outputs['1'][0] * outputs['2'][0])
