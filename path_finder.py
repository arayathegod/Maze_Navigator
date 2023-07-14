import curses
from curses import wrapper
import queue
import time

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", "X", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"]
]

def print_maze(maze,stdscr,path=[]):
    '''prints maze'''

    magenta=curses.color_pair(1)
    blue=curses.color_pair(2)

    for i,row in enumerate(maze):
        for j, val in enumerate(row):
            if (i,j) in path:
                stdscr.addstr(i,j*2,"X",magenta)
            else:
                stdscr.addstr(i,j*2,val,blue)

def find_start(maze,start):
    for i,row in enumerate(maze):
        for j,val in enumerate(row):
            if val == start:
                return i,j
    return None

def find_neighbors(maze,r,c):
    '''finds neighbors of current node'''

    neighbors = []

    if r-1>=0:
        neighbors.append((r-1,c))
        if c-1>=0:
            neighbors.append((r-1,c-1))
        if c+1<len(maze[0]):
            neighbors.append((r-1,c+1))

    if r+1<len(maze):
        neighbors.append((r+1,c))
        if c-1>=0:
            neighbors.append((r+1,c-1))
        if c+1<len(maze[0]):
            neighbors.append((r+1,c+1))

    if c-1>=0:
        neighbors.append((r,c-1))

    if c+1<len(maze[0]):
        neighbors.append((r,c+1))

    return neighbors


def find_path(maze,stdscr):
    '''finds shortest path in maze using bfs''' 

    start,end="O","X"
    start_pos=find_start(maze,start)

    q=queue.Queue()
    q.put((start_pos,[start_pos]))

    visited=set()

    while not q.empty():
        current_pos,path=q.get()
        row,col=current_pos

        stdscr.clear()
        print_maze(maze,stdscr,path)
        time.sleep(0.2)
        stdscr.refresh()

        if maze[row][col]==end:
            return path
        
        neighbors=find_neighbors(maze,row,col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue
            r,c=neighbor
            if maze[r][c]=="#":
                continue

            new_path=path+[neighbor]
            q.put((neighbor,new_path))
            visited.add(neighbor)
                
        



def main(stdscr):
    '''main function'''

    curses.init_pair(1,curses.COLOR_MAGENTA,curses.COLOR_BLACK) #id, foreground color, background color
    curses.init_pair(2,curses.COLOR_BLUE,curses.COLOR_BLACK)

    #pink_white=curses.color_pair(1)

    #stdscr.clear()
    #stdscr.addstr(5,5,"Hello world!",pink_white) #add string to output screen
    #print_maze(maze,stdscr)
    #stdscr.refresh()

    find_path(maze,stdscr)
    stdscr.getch() #get character from user

wrapper(main)
