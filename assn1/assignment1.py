import sys
from math import sqrt
import re

pointRE=re.compile("(-?\\d+.?\\d*)\\s(-?\\d+.?\\d*)")

def dist(p1, p2):
    return sqrt(pow(p1[0]-p2[0],2) + pow(p1[1]-p2[1],2))

#Run the divide-and-conquor nearest neighbor 
def nearest_neighbor(points):
    return nearest_neighbor_recursion(points)

#Brute force version of the nearest neighbor algorithm, O(n**2)
def brute_force_nearest_neighbor(points):
    min_distance=0
    return min_distance

def nearest_neighbor_recursion(points):
    min_distance=0
    return min_distance

def read_file(filename):
    points=[]
    # File format
    # x1 y1
    # x2 y2
    # ...
    in_file=open(filename,'r')
    for line in in_file.readlines():
        line = line.strip()
        point_match=pointRE.match(line)
        if point_match:
            x = point_match.group(1)
            y = point_match.group(2)
            points.append((x,y))
    print(points)
    return points

def main(filename,algorithm):
    algorithm=algorithm[1:]
    points=read_file(filename)
    if algorithm =='dc':
        print("Divide and Conquer: ", nearest_neighbor(points))
    if algorithm == 'bf':
        print("Brute Force: ", brute_force_nearest_neighbor(points))
    if algorithm == 'both':
        print("Divide and Conquer: ", nearest_neighbor(points))
        print("Brute Force: ", brute_force_nearest_neighbor(points))

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("python assignment1.py -<dc|bf|both> <input_file>")
        quit(1)
    if len(sys.argv[1]) < 2:
        print("python assignment1.py -<dc|bf|both> <input_file>")
        quit(1)
    main(sys.argv[2],sys.argv[1])