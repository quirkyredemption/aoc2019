from collections import defaultdict
counter = 0

for idx in range(240920, 789858):
    pw_list = list(map(int, str(idx)))
    has_decrease = False
    for idx in range(len(pw_list) - 1):
        if pw_list[idx] > pw_list[idx + 1]:
            has_decrease = True
            break
        
    if has_decrease:
        continue

    double = defaultdict(int)
    for idx in range(len(pw_list) - 1):
        if pw_list[idx] == pw_list[idx + 1]:
            double[pw_list[idx]] += 1
    
    print(pw_list, double, double.values())
    has_adjacent = 1 in double.values()
    if has_adjacent:
        counter += 1

    
print(counter)
    
