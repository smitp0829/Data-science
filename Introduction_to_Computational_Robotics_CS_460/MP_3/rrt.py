import sys
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import numpy as np
import math

'''
Set up matplotlib to create a plot with an empty square
'''
def setupPlot():
    fig = plt.figure(num=None, figsize=(5, 5), dpi=120, facecolor='w', edgecolor='k')
    ax = fig.subplots()
    ax.set_axisbelow(True)
    ax.set_ylim(-1, 11)
    ax.set_xlim(-1, 11)
    ax.grid(which='minor', linestyle=':', alpha=0.2)
    ax.grid(which='major', linestyle=':', alpha=0.5)
    return fig, ax

'''
Make a patch for a single pology 
'''
def createPolygonPatch(polygon, color):
    verts = []
    codes= []
    for v in range(0, len(polygon)):
        xy = polygon[v]
        verts.append((xy[0], xy[1]))
        if v == 0:
            codes.append(Path.MOVETO)
        else:
            codes.append(Path.LINETO)
    verts.append(verts[0])
    codes.append(Path.CLOSEPOLY)
    path = Path(verts, codes)
    patch = patches.PathPatch(path, facecolor=color, lw=1)

    return patch
    

'''
Render the problem  
'''
def drawProblem(robotStart, robotGoal, polygons):
    _, ax = setupPlot()
    patch = createPolygonPatch(robotStart, 'green')
    ax.add_patch(patch)    
    patch = createPolygonPatch(robotGoal, 'red')
    ax.add_patch(patch)    
    for p in range(0, len(polygons)):
        patch = createPolygonPatch(polygons[p], 'gray')
        ax.add_patch(patch)    
    plt.show()


def distance(point_one, point_two):
    return math.sqrt(math.pow(point_one[0]-point_two[0],2) + math.pow(point_one[1]-point_two[1],2))


def line_from_points(point_one,point_two): 
    line_component = []
    a = point_one[1] - point_two[1] 
    b = point_two[0] - point_one[0]  
    c = (point_one[0]*point_two[1]) - (point_one[1]*point_two[0]) 
    line_component.append(a)
    line_component.append(b)
    line_component.append(c)
  
    return line_component

def get_adjacency_list(points):
    adjListMap = {}
    for l in range(1, len(points)+1):
        adjListMap[l] =[]

    for i in range(2,len(points) + 1):
        dis = []
        index_j = []
        
        # print("finding near neighbor", points[i])
        for j in range(1, i + 1):
            if i == j:
                continue
            dis.append(distance(points[i], points[j]))
            index_j.append(points[j])
        min_point = index_j[dis.index(min(dis))]

        for m in range(1, i + 1):
            if(points[m] == min_point):
                index_min = m
                # print("Index of min" + str(index_min) + " point" + str(points[m]))
                if m not in adjListMap[i]:
                    adjListMap[i].append(m)

                if i not in adjListMap[m]:
                    adjListMap[m].append(i)
        
    return adjListMap

   
'''
Grow a simple RRT 
'''
def growSimpleRRT(points):
    newPoints = {}
    adjListMap = {}
    new_point_index = len(points)+1
    lines = []
    new_point_adjListMap = {}
    new_point_cordinate = dict()
    trak_of_line_first_point = []
    trak_of_line_second_point =[]
    min_index_of_before_point  = 0 
    min_index_of_after_point = 0 
    
    
    # adjListMap = get_adjacency_list(points)
    
    for l in range(1, len(points)+1):
        adjListMap[l] =[]

    if(len(points) == 2):
        adjListMap[1].append(2)
        adjListMap[2].append(1)
    
    lines.append(line_from_points(points[1], points[2]))
    trak_of_line_first_point.append(points[1])
    trak_of_line_second_point.append(points[2])
    adjListMap[1].append(2)
    adjListMap[2].append(1)
    # len(points) + 1


    for i in range(3,len(points)+1):
    # for i in range(3,4):
        point = points[i]
        dis = []
        points_x_y = []
        # point_before_index_array = []
        # point_after_index_array = []
        store_line = []
        find_index_min_before_in_points = False
        find_index_min_after_in_points = False
        find_index_min_before_in_newPoints = False
        find_index_min_after_in_newPoints = False
        find_point_on_line = False

        # print("I got the point......." , point)
        for j in range(0, len(lines)):
            if(find_point_on_line):
                continue
            line = lines[j]
            # print("I got the line-----" + str(line) + "of point" + str(trak_of_line_first_point[j]) + "and" + str(trak_of_line_second_point[j]))
            try:
                x_is_good = False
                y_is_good = False
                x = ((line[1] * ((line[1]*point[0]) - (line[0]*point[1]))) - (line[0]*line[2])) / (math.pow(line[0],2) + math.pow(line[1],2))
                y = ((line[0] * (((-1)*line[1]*point[0]) + (line[0]*point[1]))) - (line[1]* line[2])) / (math.pow(line[0],2) + math.pow(line[1],2))

                # print("print x",x)
                # print("print y",y)
                point_before = trak_of_line_first_point[j]
                point_after = trak_of_line_second_point[j]
                
                # print("point_before",point_before)
                # print("point_after",point_after)
                # print("x is ", x)
                # print("y is", y)
                if(x == point[0] and y == point[1] and x >= min(point_before[0],point_after[0]) and x <= max(point_before[0],point_after[0])
                        and y >= min(point_before[1],point_after[1]) and y <= max(point_before[1],point_after[1])):
                    min_index_of_before_point_on_line = 0 
                    min_index_of_after_point_on_line = 0 
                    find_index_min_before_in_points_on_line = False
                    find_index_min_after_in_points_on_line = False
                    find_index_min_before_in_newPoints_on_line = False
                    find_index_min_after_in_newPoints_on_line = False

                    for x in range(1, i+1):
                        if(points[x] == point_before):
                            min_index_of_before_point_on_line = x 
                            # print("min_index_of_before_point_on_line",min_index_of_before_point_on_line)
                            find_index_min_before_in_points_on_line = True
                        if(points[x] == point_after):
                            # print("point[p]" , points[p])
                            min_index_of_after_point_on_line = x
                            # print("min_index_of_after_point_on_line",min_index_of_after_point_on_line)
                            find_index_min_after_in_points_on_line = True
                        if(points[x] == point):
                            index_of_point = x
                    
                    for z in range(len(points)+1 , len(points)+ 1 + len(new_point_cordinate)):
                        # print(new_point_cordinate[q])
                        if(new_point_cordinate[z] == point_before):
                            min_index_of_before_point_on_line = z
                            find_index_min_before_in_newPoints_on_line = True
                        if(new_point_cordinate[z] == point_after):
                            min_index_of_after_point_on_line = z
                            find_index_min_after_in_newPoints_on_line = True
                            # print("Q,",q)
                    
                    if(find_index_min_before_in_points_on_line and find_index_min_after_in_points_on_line):
                        adjListMap[min_index_of_before_point_on_line].remove(min_index_of_after_point_on_line)
                        adjListMap[min_index_of_after_point_on_line].remove(min_index_of_before_point_on_line)
                        # print(adjListMap[min_index_of_before_point])
                        # print(adjListMap[min_index_of_after_point])
                    elif(find_index_min_before_in_points_on_line and find_index_min_after_in_newPoints_on_line):
                        adjListMap[min_index_of_before_point_on_line].remove(min_index_of_after_point_on_line)
                        new_point_adjListMap[min_index_of_after_point_on_line].remove(min_index_of_before_point_on_line)
                        
                    elif(find_index_min_before_in_newPoints_on_line and find_index_min_after_in_points_on_line):
                        new_point_adjListMap[min_index_of_before_point_on_line].remove(min_index_of_after_point_on_line)
                        adjListMap[min_index_of_after_point_on_line].remove(min_index_of_before_point_on_line)

                    elif(find_index_min_before_in_newPoints_on_line and find_index_min_after_in_newPoints_on_line):
                        new_point_adjListMap[min_index_of_before_point_on_line].remove(min_index_of_after_point_on_line)
                        new_point_adjListMap[min_index_of_after_point_on_line].remove(min_index_of_before_point_on_line)
                    else:
                        pass
                    
                    # print("point_length", len(points))
                    # print("index_of_point",index_of_point)

                    if(min_index_of_before_point_on_line <= len(points) and min_index_of_after_point_on_line <= len(points)):
                        adjListMap[min_index_of_before_point_on_line].append(index_of_point)
                        adjListMap[min_index_of_after_point_on_line].append(index_of_point)
                    else:
                        if(min_index_of_before_point_on_line <= len(points) and min_index_of_after_point_on_line > len(points)):
                            adjListMap[min_index_of_before_point_on_line].append(index_of_point)
                            new_point_adjListMap[min_index_of_after_point_on_line].append(index_of_point)

                        elif(min_index_of_before_point_on_line > len(points) and min_index_of_after_point_on_line <= len(points)):
                            adjListMap[min_index_of_after_point_on_line].append(index_of_point)
                            new_point_adjListMap[min_index_of_before_point_on_line].append(index_of_point)
                        else:
                            new_point_adjListMap[min_index_of_before_point_on_line].append(index_of_point)
                            new_point_adjListMap[min_index_of_after_point_on_line].append(index_of_point)   


                    adjListMap[index_of_point].append(min_index_of_before_point_on_line)
                    adjListMap[index_of_point].append(min_index_of_after_point_on_line)
                    
                    lines.append(line_from_points(point_before,point))
                    lines.append(line_from_points(point_after,point))

                    trak_of_line_first_point.append(point_before)
                    trak_of_line_second_point.append(point)
                    
                    trak_of_line_first_point.append(point)
                    trak_of_line_second_point.append(point_after)
                    

                    lines.pop(j)
                    trak_of_line_first_point.pop(j)
                    trak_of_line_second_point.pop(j)

                    find_point_on_line = True
                    break
                else:
                    if(find_point_on_line):
                        continue
                    else:
                        pass
                    
                if(find_point_on_line == False):
                    if(min(point_after[0], point_before[0]) <= x and max(point_after[0], point_before[0]) >= x):
                        x_is_good = True
                        
                    if(min(point_after[1], point_before[1]) <= y and max(point_after[1], point_before[1]) >= y):
                        y_is_good = True
                    
                    if(x_is_good == True and y_is_good == True):
                        # print("going here too///////////////////////////////////////////")
                        # print("x is good and x is",x)
                        # print("y is good and y is",y)
                        distance_between = distance((x,y), point)
                        point_x_and_y = (x,y)
                        dis.append(distance_between)
                        points_x_y. append(point_x_and_y)
                        store_line.append(line)
                        # point_before_index_array.append(j+1)
                        # point_after_index_array.append(j+2)
            except:
                # print("go in except")
                continue
        if(find_point_on_line):
            # print("coming here")
            continue
        
        # print("I AM going here..................................................................................")
        distance_vertex = []
        # index_store = []
        for n in range(1, i):
            distance_vertex.append(distance(point, points[n]))
            # index_store.append(n)
        
        # print("min(distance_vertex)",min(distance_vertex))
        # print("min(dis)",min(dis))
        if(len(dis) != 0):
            if(min(distance_vertex) <= min(dis)):
                min_distance_vertex_index = distance_vertex.index(min(distance_vertex))
                min_distance_vertex_index = min_distance_vertex_index + 1
                if min_distance_vertex_index not in adjListMap[i]:
                    adjListMap[i].append(min_distance_vertex_index)

                if i not in adjListMap[min_distance_vertex_index]:
                    adjListMap[min_distance_vertex_index].append(i)

                lines.append(line_from_points(points[min_distance_vertex_index],point))
                trak_of_line_first_point.append(points[min_distance_vertex_index])
                trak_of_line_second_point.append(point)
        
            else:    
                
                min_distance_index  = dis.index(min(dis))
                min_point  = points_x_y[min_distance_index]
                min_point_line = store_line[min_distance_index]
                index_of_min_point_line_index = lines.index(min_point_line)
                min_point_before_point_index  = index_of_min_point_line_index
                min_point_after_point_index  = index_of_min_point_line_index
                min_x_and_y = points_x_y[min_distance_index]
                found_m = False


                for m in range(1, i ):
                    if(points[m] == min_point):
                        index_min = m
                        found_m = True

                        if m not in adjListMap[i]:
                            adjListMap[i].append(m)
                            
                        if i not in adjListMap[m]:
                            adjListMap[m].append(i)
                        lines.append(line_from_points(min_point,point))
                        trak_of_line_first_point.append(min_point)
                        trak_of_line_second_point.append(point)


                if(found_m == False):    
                    # print("trak_of_line_first_point[min_point_before_point_index]", trak_of_line_first_point[min_point_before_point_index])
                    # print("trak_of_line_second_point[min_point_after_point_index]", trak_of_line_second_point[min_point_after_point_index])
                    for p in range(1, i):
                        if(points[p] == trak_of_line_first_point[min_point_before_point_index]):
                            min_index_of_before_point = p 
                            find_index_min_before_in_points = True
                        if(points[p] == trak_of_line_second_point[min_point_after_point_index]):
                            # print("point[p]" , points[p])
                            min_index_of_after_point = p
                            find_index_min_after_in_points = True
                    
                    for q in range(len(points)+1 , len(points)+ 1 + len(new_point_cordinate)):
                        # print(new_point_cordinate[q])
                        if(new_point_cordinate[q] == trak_of_line_first_point[min_point_before_point_index]):
                            min_index_of_before_point = q
                            find_index_min_before_in_newPoints = True
                        if(new_point_cordinate[q] == trak_of_line_second_point[min_point_after_point_index]):
                            min_index_of_after_point = q
                            find_index_min_after_in_newPoints = True
                            # print("Q,",q)

                    if(find_index_min_before_in_points and find_index_min_after_in_points):
                        adjListMap[min_index_of_before_point].remove(min_index_of_after_point)
                        adjListMap[min_index_of_after_point].remove(min_index_of_before_point)
                        # print(adjListMap[min_index_of_before_point])
                        # print(adjListMap[min_index_of_after_point])
                    elif(find_index_min_before_in_points and find_index_min_after_in_newPoints):
                        adjListMap[min_index_of_before_point].remove(min_index_of_after_point)
                        new_point_adjListMap[min_index_of_after_point].remove(min_index_of_before_point)
                    elif(find_index_min_before_in_newPoints and find_index_min_after_in_points):
                        new_point_adjListMap[min_index_of_before_point].remove(min_index_of_after_point)
                        adjListMap[min_index_of_after_point].remove(min_index_of_before_point)
                    elif(find_index_min_before_in_newPoints and find_index_min_after_in_newPoints):
                        new_point_adjListMap[min_index_of_before_point].remove(min_index_of_after_point)
                        new_point_adjListMap[min_index_of_after_point].remove(min_index_of_before_point)
                    else:
                        pass
                    # print("min_index_of_after_point", min_index_of_after_point)
                    # print("min_index_of_before_point", min_index_of_before_point)
                    
                    
                    
                    # newPoints[new_point_index] = []
                    new_point_adjListMap[new_point_index]=[]

                    new_point_adjListMap[new_point_index].append(min_index_of_before_point)
                    new_point_adjListMap[new_point_index].append(min_index_of_after_point)
                    new_point_adjListMap[new_point_index].append(i)
                    adjListMap[i].append(new_point_index)
                    if(min_index_of_before_point < len(points) and min_index_of_after_point < len(points)):
                        adjListMap[min_index_of_after_point].append(new_point_index)
                        adjListMap[min_index_of_before_point].append(new_point_index)
                    else:
                        if(min_index_of_before_point < len(points) and min_index_of_after_point >= len(points)):
                            adjListMap[min_index_of_before_point].append(new_point_index)
                            new_point_adjListMap[min_index_of_after_point].append(new_point_index)
                        elif(min_index_of_before_point >= len(points) and min_index_of_after_point < len(points)):
                            adjListMap[min_index_of_after_point].append(new_point_index)
                            new_point_adjListMap[min_index_of_before_point].append(new_point_index)
                        else:
                            new_point_adjListMap[min_index_of_before_point].append(new_point_index)
                            new_point_adjListMap[min_index_of_after_point].append(new_point_index)   
                    new_point_cordinate[new_point_index] = min_x_and_y
                    new_point_index += 1
                    
                    
                    lines.append(line_from_points(trak_of_line_first_point[min_point_before_point_index], min_point))
                    lines.append(line_from_points(trak_of_line_second_point[min_point_after_point_index], min_point))
                    lines.append(line_from_points(point,min_point))
                    
                    trak_of_line_first_point.append(trak_of_line_first_point[min_point_before_point_index])
                    trak_of_line_first_point.append(trak_of_line_second_point[min_point_after_point_index])
                    trak_of_line_first_point.append(point)

                    trak_of_line_second_point.append(min_point)
                    trak_of_line_second_point.append(min_point)
                    trak_of_line_second_point.append(min_point)

                    lines.pop(index_of_min_point_line_index)
                    trak_of_line_first_point.pop(min_point_before_point_index)
                    trak_of_line_second_point.pop(min_point_after_point_index)

                # print("--------------------------------------------------------------------")
        if(len(dis) == 0):
            distance_vertex = []
            # index_store = []
            for n in range(1, i):
                distance_vertex.append(distance(point, points[n]))
                # print("distance" + str(distance(point, points[n])) + "from point" + str(points[n]) + " and" + str(point))
                # index_store.append(n)
            
            # print("min distance index",distance_vertex.index(min(distance_vertex)))
            min_distance_vertex_index = distance_vertex.index(min(distance_vertex))
            min_distance_vertex_index = min_distance_vertex_index + 1
            if min_distance_vertex_index not in adjListMap[i]:
                adjListMap[i].append(min_distance_vertex_index)

            if i not in adjListMap[min_distance_vertex_index]:
                adjListMap[min_distance_vertex_index].append(i)

            lines.append(line_from_points(points[min_distance_vertex_index],point))
            trak_of_line_first_point.append(points[min_distance_vertex_index])
            trak_of_line_second_point.append(point)
        

        # print("length of line array",len(lines))
        # print(lines)
    # print(points)
    # print("New point coordinate", new_point_cordinate)
    # print("NEW_point_adjustlist", new_point_adjListMap)
    # print(adjListMap)
    # Your code goes here
    # newPoints = new_point_cordinate
    newPoints.update(points)
    newPoints.update(new_point_cordinate)
    adjListMap.update(new_point_adjListMap)
    
    return newPoints, adjListMap



'''
Perform basic search 
'''
def basicSearch(tree, start, goal):
    path = []
    queue = []
    # Your code goes here. As the result, the function should
    # return a list of vertex labels, e.g.
    #
    # path = [23, 15, 9, ..., 37]
    #
    # in which 23 would be the label for the start and 37 the
    # label for the goal.
    # print("length of tree", len(tree))
    found = False
    visited  = [False for i in range(len(tree))]
    visited[start-1] = True
    # print(visited)
    queue.append(start)
    while (len(queue) != 0 and found == False):
        current_vertex = queue.pop(0)
        # print("Current_vertex", current_vertex)
        path.append(current_vertex)
        if current_vertex == goal:
            found  = True
        else:
            arr = tree[current_vertex]
            # print(arr)
            # print("visited arry", len(visited))
            for i in range(0,len(arr)):
                # print("array[i]", arr[i])
                if (visited[arr[i]-1] == False):
                    visited[arr[i]-1] = True
                    queue.append(arr[i])


    return path

'''
Display the RRT and Path
'''
def displayRRTandPath(points, adjListMap, path, robotStart=None, robotGoal=None, polygons=None):
    # Your code goes here
    # You could start by copying code from the function
    # drawProblem and modify it to do what you need.
    # You should draw the problem when applicable.
    x = []
    y = []
    for i in range(1, len(adjListMap)):
        x= []
        y= []
        for j in range(0, len(adjListMap[i])):
            point_one = points[i]
            point_two = points[adjListMap[i][j]]
            x.append(point_one[0])
            x.append(point_two[0])
            y.append(point_one[1])
            y.append(point_two[1])
            # print("x",x)
            # print("y",y)
            # print(adjListMap[i][j])
            # print("-------------------------------------")

        plt.plot(x,y, color='black')


  

    # print("path",path)
    path_x =[]
    path_y =[]
    visited  = {path[0]} if path else {}

    for l in range(1, len(path)):
        adjlist = set(adjListMap[path[l]])
        index_point  = visited.intersection(adjlist)
        point = points[list(index_point)[0]]
        path_x.append(point[0])
        path_y.append(point[1])
        # print ('{} {}'.format(path[l], index_point)) 

        plt.plot([points[path[l]][0], point[0]], [points[path[l]][1], point[1]], color='orange', linestyle='-', linewidth=2)
        # plt.plot(path_x,path_y, color = 'orange')
        visited.add(path[l])
    plt.show()
    return

'''
Collision checking
'''
def isCollisionFree(robot, point, obstacles):

    # Your code goes here.
    
    return False

'''
The full RRT algorithm
'''
def RRT(robot, obstacles, startPoint, goalPoint):

    points = dict()
    tree = dict()
    path = []
    # Your code goes here.
    
    return points, tree, path

def main(filename, x1, y1, x2, y2, display=''):
    # Read data and parse polygons
    lines = [line.rstrip('\n') for line in open(filename)]
    robot = []
    obstacles = []
    for line in range(0, len(lines)):
        xys = lines[line].split(';')
        polygon = []
        for p in range(0, len(xys)):
            xy = xys[p].split(',')
            polygon.append((float(xy[0]), float(xy[1])))
        if line == 0 :
            robot = polygon
        else:
            obstacles.append(polygon)

    # Print out the data
    print("Robot:")
    print(str(robot))
    print("Pologonal obstacles:")
    for p in range(0, len(obstacles)):
        print(str(obstacles[p]))
    print("")

    # Visualize
    if display == 'display':
        robotStart = [(x + x1, y + y1) for x, y in robot]
        robotGoal = [(x + x2, y + y2) for x, y in robot]
        drawProblem(robotStart, robotGoal, obstacles)

    # Example points for calling growSimpleRRT
    # You should expect many mroe points, e.g., 200-500
    points = dict()
    # points[1] = (5, 5)
    # points[2] = (7, 8.2)
    # points[3] = (6.5, 5.2)
    # points[4] = (0.3, 4)
    # points[5] = (6, 3.7)
    # points[6] = (9.7, 6.4)
    # points[7] = (4.4, 2.8)
    # points[8] = (9.1, 3.1)
    # points[9] = (8.1, 6.5)
    # points[10] = (0.7, 5.4)
    # points[11] = (5.1, 3.9)
    # points[12] = (2, 6)
    # points[13] = (0.5, 6.7)
    # points[14] = (8.3, 2.1)
    # points[15] = (7.7, 6.3)
    # points[16] = (7.9, 5)
    # points[17] = (4.8, 6.1)
    # points[18] = (3.2, 9.3)
    # points[19] = (7.3, 5.8)
    # points[20] = (9, 0.6)

    points[1] = (5, 5)
    points[2] = (2, 2)
    points[3] = (3, 3)
    points[4] = (4, 4)
    points[5] = (1, 1)
    points[6] = (6, 4.0)
    points[7] = (7, 3)
    points[8] = (8, 2)
    points[9] = (9, 1)

    # points[1] = (5, 5)
    # points[2] = (6, 4.0)
    # points[3] = (7, 3)

    # points[1] = (5, 5)
    # points[2] = (7, 8.2)
    # points[3] = (9.7, 6.4)
    # Printing the points
    print("")
    print("The input points are:")
    print(str(points))
    print("")
    
    points, adjListMap = growSimpleRRT(points)
    print("")
    print("The new points are:")
    print(str(points))
    print("")
    print("")
    print("The tree is:")
    print(str(adjListMap))
    print("")

    # Search for a solution  
    # change 1 and 20 as you want
    # path = basicSearch(adjListMap, 1, 2)
    path = basicSearch(adjListMap, 2, 1)
    print("")
    print("The path is:")
    print(str(path))
    print("")

    # Your visualization code 
    if display == 'display':
        displayRRTandPath(points, adjListMap, path) 

    # Solve a real RRT problem
    points, adjListMap, path = RRT(robot, obstacles, (x1, y1), (x2, y2))
    
    # Your visualization code 
    if display == 'display':
        displayRRTandPath(points, adjListMap, path, robotStart, robotGoal, obstacles) 


if __name__ == "__main__":
    # Retrive file name for input data
    if(len(sys.argv) < 6):
        print("Five arguments required: python spr.py [env-file] [x1] [y1] [x2] [y2]")
        exit()
    
    filename = sys.argv[1]
    x1 = float(sys.argv[2])
    y1 = float(sys.argv[3])
    x2 = float(sys.argv[4])
    y2 = float(sys.argv[5])
    display = ''
    if(len(sys.argv) == 7):
        display = sys.argv[6]

    main(filename, x1, y1, x2, y2, display)