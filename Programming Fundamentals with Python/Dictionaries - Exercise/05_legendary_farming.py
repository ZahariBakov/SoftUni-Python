resources = {"shards": 0, "fragments": 0, "motes": 0}
found = False
legendary_item = ""

while True:
    command = input().split(" ")

    for i in range(1, len(command), 2):
        if command[i].lower() not in resources:
            resources[command[i].lower()] = 0
        resources[command[i].lower()] += int(command[i - 1])

        if resources["shards"] >= 250 or resources["fragments"] >= 250 or resources["motes"] >= 250:
            found = True

            if resources["shards"] >= 250:
                legendary_item = "Shadowmourne"
                resources["shards"] -= 250
            elif resources["fragments"] >= 250:
                legendary_item = "Valanyr"
                resources["fragments"] -= 250
            else:
                legendary_item = "Dragonwrath"
                resources["motes"] -= 250

            print(f"{legendary_item} obtained!")
            break

    if found:
        break

for key, value in resources.items():
    print(f"{key}: {value}")
