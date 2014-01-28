# Initialize information
min_dist = int(input())
max_dist = int(input())
motels = [0, 990, 1010, 1970, 2030, 2940, 3060, 3930, 4060, 4970, 5030, 5990, 6010, 7000]
for i in range(int(input())):
    motels.append(int(input()))

# This is the number we output
counter = 0

def find_eligible_motels(A, B, d, motel_list):
    '''
    Input: A distance d and a list of motel locations along with the minimum
    and maximum distances (A and B respectively), that the driver can travel in
    one day.

    Increments 1 to the counter if the current motel is the final destination.

    Otherwise, makes a list eligible_motels of all motels the driver can stay at the next
    night and runs find_eligible_motels on each motel in the list.
    '''
    global counter 
    if d == 7000:
        counter += 1
    else:
        eligible_motels = []
        for motel in motel_list:
            if motel - d >= A and motel - d <= B:
                eligible_motels.append(motel)
        for motel in eligible_motels:
            find_eligible_motels(A, B, motel, motel_list)
    

find_eligible_motels(min_dist, max_dist, 0, motels)
print(counter)
