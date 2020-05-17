import sys
import numpy as np
import math

def multilaterate(distances):
  
    sphere_one = distances[0]           # get the first sphere coordinates 
    new = []

    for i in range(0,len(distances)):
        sphere = distances[i]
        new.append(list(map(float,(np.subtract(sphere,sphere_one)))))      # subtract first sphere coordinates form all four sphere's coordinates 
        
    
    A = np.array([[2*new[1][0],2*new[1][1],2*new[1][2]],[2*new[2][0],2*new[2][1],2*new[2][2]],[2*new[3][0],2*new[3][1],2*new[3][2]]])

    matrix_b =[]
    matrix_b.append(math.pow(distances[0][3],2)-math.pow(distances[1][3],2) + math.pow(new[1][0],2) + math.pow(new[1][1],2) + math.pow(new[1][2],2)) 
    matrix_b.append(math.pow(distances[0][3],2)-math.pow(distances[2][3],2) + math.pow(new[2][0],2) + math.pow(new[2][1],2) + math.pow(new[2][2],2))
    matrix_b.append(math.pow(distances[0][3],2)-math.pow(distances[3][3],2) + math.pow(new[3][0],2) + math.pow(new[3][1],2) + math.pow(new[3][2],2))

    B = np.array(matrix_b)
   
    # slove Ax = B
    solution = np.linalg.solve(A, B )

    # add the first sphere's coordinates to all four sphere's cordinates to get the exact point
    solve =[]
    for j in range(0,len(solution)):
        solve.append(solution[j] + sphere_one[j])

    x = solve[0]
    y = solve[1]
    z = solve[2]

    
    solve.append(_check_error(x, y, z, distances))
    
    return solve

# to find the error or area
def _check_error(x ,y, z, distances):
    error = 0.0
    value_of_equation = _equation(x,y,z,distances)
    if(value_of_equation[0] != distances[0][3]):
        error = distances[0][3] - value_of_equation[0]
    elif(value_of_equation[1] != distances[1][3]):
        error = distances[1][3] - value_of_equation[1]
    elif(value_of_equation[2] != distances[2][3]):
        error = distances[2][3] - value_of_equation[2]
    elif(value_of_equation[3] != distances[3][3]):
        error = distances[3][3] - value_of_equation[3]
    else:
        pass

    if(error < 0 ):
        error = error * (-1)
    

    return error

# to find 4 equations values 
def _equation(x,y,z,distances):
    equation_value =[]
    for i in range(0,4):
        equation_value.append(math.pow((x-distances[i][0]),2) + math.pow((x-distances[i][1]),2) + math.pow((x-distances[i][2]),2))
    return equation_value

if __name__ == "__main__":
    
    # Retrive file name for input data
    if(len(sys.argv) == 1):
        print("Please enter data file name.")
        exit()
    
    filename = sys.argv[1]
  
    # Read data
    lines = [line.rstrip('\n') for line in open(filename)]
    distances = []
    for line in range(0, len(lines)):
        distances.append(list(map(float, lines[line].split(' '))))

    # Print out the data
    print ("The input four points and distances, in the format of [x, y, z, d], are:")
    for p in range(0, len(distances)):
        print (*distances[p]) 

    # Call the function and compute the location 
    location = multilaterate(distances)
    print ("The location of the point is: " + str(location))
