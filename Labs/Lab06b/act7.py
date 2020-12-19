

first_scores = []
second_stores = []
names = []

while True:
    name = input("Enter name of golfer: ")
    names.append(name)
    first_round = float(input("Enter first round score: "))
    if first_round > 0:
        first_scores.append(first_round)
    else:
        break
    second_round = float(input("Enter second round score: "))
    if second_round > 0:
        second_stores.append(second_round)
    else:
        break
    print("First round score: ", first_scores)
    print("Second round score: ", second_stores)
    print("Name: ", names)