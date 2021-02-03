#  File: Spiral.py

#  Description: Creating a spiral given dimensions and return the sum of adjacent numbers.


import sys
import math

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n
def create_spiral(n):
    spiral = []
    if n % 2 == 0:
        n += 1
    for set in range(n):   #n number of rows
        list_outline = []
        for spot in range(n):     #n number of columns
            list_outline.append("")
        spiral.append(list_outline)     #add the empty created 2d list to spiral

    value = n ** 2   #starts with last number on top right
    position = 0
    topRight = n
    bottomRight = n - 1
    finish = -1
    start = 1
    ender = 0
    limit = math.floor(n/2)

    while position != limit:
        #one spiral circle made with each loop iteration
        for row in range(topRight - 1, finish, -1):   #goes from top right to top left
            spiral[position][row] = value
            value -= 1                  #decreaasing each value thats is being added to the spiral

        for col in range(start, topRight):
            spiral[col][position] = value    #goes top left to bottom left of spiral
            value -= 1

        for row in range(start, bottomRight + 1):
            spiral[bottomRight][row] = value           #goes bottom left to bottom right of spiral
            value -= 1

        for col in range(bottomRight - 1, ender, -1):   #goes from bottom right to top right of spiral
            spiral[col][bottomRight] = value
            value -= 1

        topRight -= 1
        bottomRight -= 1
        position += 1
        finish += 1
        start += 1
        ender += 1
    center = math.floor(n/2)   #finding the center index
    spiral[center][center] = value
    #print(spiral)
    return spiral

# Input: spiral is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers (spiral, n):
    #initialize sum of all the adjacent numbers
    sum = 0
    l = 0
    for length in spiral:
        l = l + 1
    l = l - 1

    #find central x and y
    for r in range(len(spiral)):
        for c in range(len(spiral[r])):
            if n == spiral[r][c]:
                central_x = r
                central_y = c
                break

    if n == spiral[0][0]:
        sum = spiral[central_x][central_y + 1] + spiral[central_x + 1][central_y + 1] + spiral[central_x + 1][central_y]
    elif n == spiral[0][l]:
        sum = spiral[central_x][central_y - 1] + spiral[central_x + 1][central_y - 1] + spiral[central_x + 1][central_y]
    elif n == spiral[l][0]:
        sum = spiral[central_x][central_y + 1] + spiral[central_x - 1][central_y] + spiral[central_x - 1][central_y + 1]
    elif n == spiral[l][l]:
        sum =  spiral[central_x - 1][central_y] + spiral[central_x - 1][central_y - 1] + spiral[central_x][central_y - 1]
    elif central_x == 0:
        sum = spiral[central_x][central_y - 1] + spiral[central_x][central_y + 1] + spiral[central_x + 1][central_y - 1] + spiral[central_x + 1][central_y] + spiral[central_x + 1][central_y + 1]
    elif central_x == l:
        sum = spiral[central_x - 1][central_y - 1] + spiral[central_x - 1][central_y] + spiral[central_x - 1][central_y + 1] + spiral[central_x][central_y - 1] + spiral[central_x][central_y + 1]
    elif central_y == 0:
        sum = spiral[central_x - 1][central_y] + spiral[central_x][central_y + 1] + spiral[central_x - 1][central_y + 1] + spiral[central_x + 1][central_y + 1] + spiral[central_x + 1][central_y]
    elif central_y == l:
        sum = spiral[central_x - 1][central_y] + spiral[central_x - 1][central_y - 1] + spiral[central_x][central_y - 1] + spiral[central_x + 1][central_y - 1] + spiral[central_x + 1][central_y]
    else:
        #sum of adjacent values around N
        sum = spiral[central_x - 1][central_y - 1] + spiral[central_x - 1][central_y] + spiral[central_x - 1][central_y + 1] + spiral[central_x][central_y - 1] + spiral[central_x][central_y + 1] + spiral[central_x + 1][central_y - 1] + spiral[central_x + 1][central_y] + spiral[central_x + 1][central_y + 1]

    #print(sum)
    return sum

def main():
  # read the input file
    n = int(sys.stdin.readline()) #dimension of the spiral
    upper_bound = n ** 2
    # create the spiral
    spiral = create_spiral(n)
    # add the adjacent numbers
    length = len(spiral)
    highest_max = length * length
    for line in sys.stdin:
        line = line.rstrip()

if __name__ == "__main__":
    main()
