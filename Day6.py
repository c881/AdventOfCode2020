def part1():
    groups = 0
    with open('Inputs/Day6.txt','r') as file:
        lines = file.readlines()
        answered_yes = list()
        for line in lines:
            line = line.strip()
            if len(line) > 0:
                answered_yes.extend(list(line))
            else:
                groups += len(set(answered_yes))
                answered_yes = list()
    print(groups)

def part2():
    groups = 0
    with open('Inputs/Day6.txt','r') as file:
        lines = file.readlines()
        answered_yes = list()
        for line in lines:
            line = line.strip()
            if len(line) > 0:
                answered_yes.append(set(line))
            else:
                if len(answered_yes) == 1:
                    groups += len(answered_yes[0])
                else:
                    letters = answered_yes[0]
                    for item in answered_yes[1:]:
                        letters.intersection_update(item)
                    groups += (len(letters))
                answered_yes = list()

    print(groups)
part1()
part2()
