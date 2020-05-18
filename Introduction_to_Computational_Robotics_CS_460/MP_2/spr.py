import sys
import numpy as np
from collections import defaultdict
import math 

'''
Report reflexive vertices
'''
def findReflexiveVertices(polygons):
    vertices=[]
   
    vector1 = np.subtract(polygons[0][1] , polygons[0][0])
    vector2= np.subtract(polygons[0][(len(polygons[0])-1)] , polygons[0][0])
    corss_product  = np.cross(vector2,vector1)
    

    for i in range (0, len(polygons)):
        for j in range(0, len(polygons[i])):
            if j == 0:
                vector1 = np.subtract(polygons[i][1] , polygons[i][0])
                vector2= np.subtract(polygons[i][(len(polygons[i])-1)],polygons[i][0])
                corss_product  = np.cross(vector2,vector1)
    
                if(corss_product >= 0):
                    vertices.append(polygons[i][0])
            elif j == (len(polygons[i])-1):
                vector1 = np.subtract(polygons[i][0] , polygons[i][(len(polygons[i])-1)])
                vector2= np.subtract(polygons[i][(len(polygons[i])-2)],polygons[i][(len(polygons[i])-1)])
                corss_product  = np.cross(vector2,vector1)
                
                if(corss_product >= 0):
                    vertices.append(polygons[i][(len(polygons[i])-1)])
                
            else:
                vector1 = np.subtract(polygons[i][j+1] , polygons[i][j])
                vector2= np.subtract(polygons[i][j-1] , polygons[i][j])
                corss_product  = np.cross(vector2,vector1)
                
                if(corss_product >= 0):
                    vertices.append(polygons[i][j])
    
    return vertices

def distance(point_one, point_two):
    return math.sqrt(math.pow(point_one[0]-point_two[0],2) + math.pow(point_one[1]-point_two[1],2))
'''
Compute the roadmap graph
'''
def computeSPRoadmap(polygons, reflexVertices):
    vertexMap = dict()
    adjacencyListMap = defaultdict(list)
   
    for i in range(0, len(reflexVertices)):
        vertexMap[i + 1] = reflexVertices[i]

    for n in range(1, len(vertexMap) + 1):
        adjacent = []
        for m in range(1, len(vertexMap) + 1):
            if n == m:
                continue
           
            if visible(vertexMap[n], vertexMap[m],polygons):
               adjacent.append([m, distance(vertexMap[n], vertexMap[m])])
        adjacencyListMap[n] = adjacent   
       
    return vertexMap, adjacencyListMap

def collision(vertex_one, vertex_two):
    line_one = line_from_points(vertex_one, vertex_two)
    for j in range(0,len(polygons)):
        for k in range(0,len(polygons[j])-1):
            line_two = line_from_points(polygons[j][k], polygons[j][k+1])
            
            array = [line_one[0], line_one[1]], [line_two[0], line_two[1]]
            a = np.array(array)
            array_b = [(-1)*line_one[2], (-1)* line_two[2]]
            b = np.array(array_b)
            solution = np.linalg.solve(a, b)

            
            if(on_seg(polygons[j][k],polygons[j][k+1],vertex_one, vertex_two, solution)):
                return True
            
            if(k == len(polygons[j])- 2):
                line_two = line_from_points(polygons[j][k+1], polygons[j][0])
                
                array_b = [(-1)*line_one[2], (-1)* line_two[2]]
                b = np.array(array_b)
                solution = np.linalg.solve(a, b)
            
                if(on_seg(polygons[j][k+1],polygons[j][0],vertex_one,vertex_two,solution)):
                    return True
    return False

def on_seg(point_one, point_two, point_three, point_four,solution):
    point_first_line = False
    point_second_line = False
    
    if(((min([point_one[0], point_two[0]]) < round(solution[0],4)) and (round(solution[0],4) < max([point_one[0], point_two[0]]))) and ((min([point_one[1], point_two[1]]) < round(solution[1],4)) and (round(solution[1],4) < max([point_one[1], point_two[1]])))):
        point_first_line = True
    if(((min([point_three[0], point_four[0]]) < round(solution[0],4)) and (round(solution[0],4) < max([point_three[0], point_four[0]]))) and ((min([point_three[1], point_four[1]]) < round(solution[1],4)) and (round(solution[1],4) < max([point_three[1], point_four[1]])))):
        if(min([point_three[0], point_four[0]]) < solution[0]):
    
            point_second_line = True
        

    if(point_first_line == True and point_second_line == True ):
        return True
    else:
        return False

def visible(vertex_one,vertex_two, polygons):
    line = line_from_points(vertex_one, vertex_two)

    num_polygon_vertex_one = 0 
    num_polygon_vertex_two = 0
    index_one = 0
    index_two = 0
    point_one_side = False
    point_second_side = False

    for i in range (0, len(polygons)):
        if(vertex_one in polygons[i] and vertex_two in polygons[i]):
            if((polygons[i].index(vertex_one)) - (polygons[i].index(vertex_two)) == -1 or (polygons[i].index(vertex_one)) - (polygons[i].index(vertex_two)) == 1 ):
                return True
            elif ((polygons[i].index(vertex_one)) == 0 and (polygons[i].index(vertex_two) == len(polygons[i])-1)):
                return True 
            elif ((polygons[i].index(vertex_two)) == 0 and (polygons[i].index(vertex_one) == len(polygons[i])-1)):
                return True
            else:
                
                index_one = polygons[i].index(vertex_one) 
                before_point_one = polygons[i][index_one - 1]
                if (index_one == len(polygons[i])-1):
                    after_point_one = polygons[i][0]
                else:
                    after_point_one = polygons[i][index_one + 1]
                
                
                index_two = polygons[i].index(vertex_two) 
                before_point_two = polygons[i][index_two - 1]
                if (index_one == len(polygons[i])-1):
                    after_point_two = polygons[i][0]
                else:
                    after_point_two = polygons[i][index_two + 1]

                plug_in_one_before_line = plug_point_line(line, before_point_one) 
                plug_in_one_after_line = plug_point_line(line, after_point_one)
                

                if((plug_in_one_before_line < 0 and plug_in_one_after_line < 0) or (plug_in_one_before_line > 0 and plug_in_one_after_line > 0)):
                    point_one_side = True 
                

                plug_in_two_before_line = plug_point_line(line, before_point_two) 
                plug_in_two_after_line = plug_point_line(line, after_point_two)

                
    
                
                if((plug_in_two_before_line < 0 and plug_in_two_after_line < 0) or (plug_in_two_before_line > 0 and plug_in_two_after_line > 0)):
                   
                    point_second_side = True

                if(point_one_side and point_second_side == True):
                   
                    #return True
                    if(collision(vertex_one, vertex_two)):
                       
                        return False
                    else:
                      
                        return True
                else:
                   
                    return False



        else: 
            
            if(vertex_one in polygons[i]):
                num_polygon_vertex_one  = i
                index_one = polygons[i].index(vertex_one)
               
            if(vertex_two in polygons[i]):
                num_polygon_vertex_two  = i
                index_two = polygons[i].index(vertex_two)
               
            
    if(num_polygon_vertex_one != num_polygon_vertex_two):
        
        before_point_one = polygons[num_polygon_vertex_one][index_one - 1]
        if (index_one == len(polygons[num_polygon_vertex_one])-1):
             after_point_one = polygons[num_polygon_vertex_one][0]
        else:
            after_point_one = polygons[num_polygon_vertex_one][index_one + 1]

        before_point_two = polygons[num_polygon_vertex_two][index_two - 1]
        if (index_two == len(polygons[num_polygon_vertex_two])-1):
            after_point_two = polygons[num_polygon_vertex_two][0]
        else:
            after_point_two = polygons[num_polygon_vertex_two][index_two + 1]

        plug_in_one_before_line = plug_point_line(line, before_point_one) 
        plug_in_one_after_line = plug_point_line(line, after_point_one)
        
        if((plug_in_one_before_line < 0 and plug_in_one_after_line < 0) or (plug_in_one_before_line > 0 and plug_in_one_after_line > 0)):
            
            point_one_side = True 
        

        plug_in_two_before_line = plug_point_line(line, before_point_two) 
        plug_in_two_after_line = plug_point_line(line, after_point_two)
       
        
        if((plug_in_two_before_line < 0 and plug_in_two_after_line < 0) or (plug_in_two_before_line > 0 and plug_in_two_after_line > 0)):
           
            point_second_side = True

        if(point_one_side and point_second_side == True):
           
            if(collision(vertex_one, vertex_two)):
                
                return False
            else:
                
                return True
            
        else:
            
            return False
    
    else:
        
        return False
                
        
            
def plug_point_line(line, point):
     return ((line[0]*point[0]) + (line[1]*point[1]) + line[2])       


def line_from_points(point_one,point_two): 
    line_component = []
    a = point_one[1] - point_two[1] 
    b = point_two[0] - point_one[0]  
    c = (point_one[0]*point_two[1]) - (point_one[1]*point_two[0]) 
    line_component.append(a)
    line_component.append(b)
    line_component.append(c)
  
    return line_component
'''
Perform uniform cost search 
'''
def uniformCostSearch(adjListMap, start, goal):
    path = []
    pathLength = 0

    visited  = [False for i in range(len(adjListMap))]
    queue = [[start,0]]
    length = [] 
    while queue:
        if(len(length) == 0):
            element  = queue.pop(0)
            vertex = element[0]
        else: 
            min_length = min(length)
            index  = length.index(min_length)
            element = queue.pop(index)
            vertex = element[0]
            pathLength = length.pop(index)
        
        
        if(visited[vertex] == True):
            continue
       
        visited[vertex] = True 
        path.append(vertex)
        if(vertex == goal):
            return path, pathLength
        else:
            array = adjListMap.get(vertex)
            for i in range(0, len(array)):
                queue.append(array[i])
                length.append(array[i][1] + pathLength)


    return path, pathLength

def visible_for_point(vertex_one,vertex_two, polygons):
    line = line_from_points(vertex_one, vertex_two)
    for i in range (0, len(polygons)):
        if(vertex_two in polygons[i]):
            num_polygon_vertex_two  = i
            index_two = polygons[i].index(vertex_two)
    
    before_point_two = polygons[num_polygon_vertex_two][index_two - 1]
    if (index_two == len(polygons[num_polygon_vertex_two])-1):
        after_point_two = polygons[num_polygon_vertex_two][0]
    else:
        after_point_two = polygons[num_polygon_vertex_two][index_two + 1]

    
    plug_in_two_before_line = plug_point_line(line, before_point_two) 
    plug_in_two_after_line = plug_point_line(line, after_point_two)
       
        
    if((plug_in_two_before_line < 0 and plug_in_two_after_line < 0) or (plug_in_two_before_line > 0 and plug_in_two_after_line > 0)):

       
        if(collision(vertex_one, vertex_two)):
           
            return False
        else:
           
            return True
'''     
Agument roadmap to include start and goal
'''
def updateRoadmap(polygons, vertexMap, adjListMap, x1, y1, x2, y2):
    updatedALMap = dict()
    startLabel = 0
    goalLabel = -1
    
    # Your code goes here. Note that for convenience, we 
    # let start and goal have vertex labels 0 and -1,
    # respectively. Make sure you use these as your labels
    # for the start and goal vertices in the shortest path
    # roadmap. Note that what you do here is similar to
    # when you construct the roadmap. 
    
    updatedALMap = adjListMap.copy()

    start_adjacent = []
    for n in range(1, len(vertexMap) + 1):
        if visible_for_point([x1, y1], vertexMap[n],polygons):
            start_adjacent.append([n, distance([x1, y1], vertexMap[n])])
            updatedALMap[n].append([0, distance([x1, y1], vertexMap[n])])
        updatedALMap[startLabel] = start_adjacent   

    goal_adjacent = []
    for m in range(1, len(vertexMap) + 1):
        if visible_for_point([x2,y2], vertexMap[m],polygons):
            goal_adjacent.append([m, distance([x2,y2], vertexMap[m])])
            updatedALMap[m].append([-1, distance([x2, y2], vertexMap[m])])
        updatedALMap[goalLabel] = goal_adjacent 

    return startLabel, goalLabel, updatedALMap


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

    # Read data and parse polygons
    lines = [line.rstrip('\n') for line in open(filename)]
    polygons = []
    for line in range(0, len(lines)):
        xys = lines[line].split(';')
        polygon = []
        for p in range(0, len(xys)):
            polygon.append([float(i) for i in xys[p].split(',')])
        polygons.append(polygon)

    # Print out the data
    print("Pologonal obstacles:")
    for p in range(0, len(polygons)):
        print(str(polygons[p]))
    print("")

    # Compute reflex vertices
    reflexVertices = findReflexiveVertices(polygons)
    print("Reflexive vertices:")
    print(str(reflexVertices))
    print("")

    # Compute the roadmap 
    vertexMap, adjListMap = computeSPRoadmap(polygons, reflexVertices)
    print("Vertex map:")
    print(str(vertexMap))
    print("")
    print("Base roadmap:")
    print(dict(adjListMap))
    print("")

    # Update roadmap
    start, goal, updatedALMap = updateRoadmap(polygons, vertexMap, adjListMap, x1, y1, x2, y2)
    print("Updated roadmap:")
    print(dict(updatedALMap))
    print("")

    # Search for a solution     
    path, length = uniformCostSearch(updatedALMap, start, goal)
    print("Final path:")
    print(str(path))
    print("Final path length:" + str(length))

