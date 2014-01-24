winnings = {1:100,
            2:500,
            3:1000,
            4:5000,
            5:10000,
            6:25000,
            7:50000,
            8:100000,
            9:500000,
            10:1000000}

opened = [int(input()) for i in range(int(input()))]

offer = int(input())

remaining = [winnings[k] for k in winnings if k not in opened]

average = sum(remaining)/len(remaining)

if offer > average:
    print("deal")
else:
    print("no deal")
