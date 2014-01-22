import heapq

def dist(x,y):
    '''
    Input: Two integers x, y representing the addresses of two houses.
    Output: The shortest distance between the two houses.
    '''
    return min((abs(x-y), 1000000-abs(x-y)))

def adjacent_dists(houselist):
    '''
    Input: A sorted list of house locations.
    Output: A list of distances between consecutive houses.
    The ith element of the output list is the distance between the ith and
    (i+1)th houses in houselist.
    '''
    return [dist(houselist[i],houselist[i+1]) for i in range(len(houselist)-1)] + [dist(houselist[-1], houselist[0])]

def midpoints(x,y):
    '''
    Input: Two integers x, y representing the addresses of two houses.
    Output: A tuple (m1, m2) giving the addresses of the two midpoints between
    x and y.
    '''
    return ((x+y)/2, (500000+(x+y)/2)%1000000)

def max_dist(houselist, p):
    '''
    Input: A list of house locations and a location p.
    Output: The maximum distance from a house in houselist to p.
    '''
    return max([dist(house, p) for house in houselist])
    
def one_hydrant(houselist):
    '''
    Input: A sorted list of house addresses (integers).
    Output: The maximum length of hose required to connect a house its nearest
    fire hydrant, given that we have exactly 1 fire hydrant.
    '''
    if len(houselist) == 1:
        return 0
    else:
        adj_dists = adjacent_dists(houselist)
        max_adjacent_dist = max(adj_dists)
        index = adj_dists.index(max_adjacent_dist)
        two_houses = [houselist[index], houselist[(index + 1)%len(houselist)]]
        mpts = midpoints(two_houses[0], two_houses[1])
        possible_hose_lengths = [max_dist(houselist, point) for point in mpts]
        return min(possible_hose_lengths)    

def split_houses(houselist, k):
    '''
    Input: A list of house locations and an integer k, representing the number of hydrants.
    Output: A list of k lists. Each sublist is a group of houses that are pretty close together.
    '''
    adj_dists = adjacent_dists(houselist)
    k_largest_dists = heapq.nlargest(k, adj_dists)
    indices = [adj_dists.index(d) for d in k_largest_dists]
    indices.sort()
    output = [houselist[indices[i]+1:indices[i+1]+1] for i in range(len(indices)-1)]
    if houselist.index(houselist[(indices[-1] + 1)%len(houselist)]) == 0:
        last_group = [houselist[:indices[0]+1]]
    else:
        last_group = [houselist[(indices[-1] + 1):] + houselist[:indices[0]+1]]
    output += last_group
    return output

houses = [int(input()) for i in range(int(input()))]

houses.sort()

num_hydrants = int(input())

house_groups = split_houses(houses, num_hydrants)

max_hose_length = max([one_hydrant(group) for group in house_groups])

print (max_hose_length)
