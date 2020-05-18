import sys
import numpy as np 
import matplotlib.pyplot as plt
import math

# intialize arrays to store values 
k = []
predictedx1 = []
predictedx2 = []
observationz1 = []
observationz2 = []
Q = np.array([[math.pow(10,-4),2*math.pow(10,-5)],[2*math.pow(10,-5),math.pow(10,-4)]])       # Q is given 
R = np.array([[math.pow(10,-2),5*math.pow(10,-3)],[5*pow(10,-3), 2*pow(10,-2)]])              # R is given 
H = np.array([[1.0, 0.0],[0.0,1.0]])                                                          # H is identity 
I = np.array([[1.0, 0.0],[0.0,1.0]])                                                          # I is identity 

# To plot points in matplotlib
def graph(x1k,x2k,z1k,z2k):
	plt.scatter(x1k,x2k,label = "Prediction")
	plt.plot(x1k,x2k)
	plt.scatter(z1k,z2k, label = "Observation")
	plt.plot(z1k,z2k)
	plt.legend()
	plt.show()
	return

if __name__ == "__main__":
    
    # Retrive file name for input data
    if(len(sys.argv) < 5):
        print ("Four arguments required: python kalman2d.py [datafile] [x1] [x2] [lambda]")
        exit()
    
    filename = sys.argv[1]
    x10 = float(sys.argv[2])
    x20 = float(sys.argv[3])
    scaler = float(sys.argv[4])

    # Read data
    lines = [line.rstrip('\n') for line in open(filename)]
    data = []
    for line in range(0, len(lines)):
        data.append(list(map(float, lines[line].split(' '))))

    
    
    # Print out the data
    print ("The input data points in the format of 'k [u1, u2, z1, z2]', are:")
    for it in range(0, len(data)):
        print (str(it + 1) + ": ", end='')
        k.append(it+1)
        print (*data[it])

    previous_x = np.array([[x10],[x20]])                         # gussed xk = previous_xk
    previous_p = scaler * np.array([[1.0,0.0],[0.0,1.0]])        # gussed scaler * identity = previous_pk

    for i in range(1,len(k)+1):
        A = np.array([[1.0,i],[0.0,1.0]])                 # Matrix A
        B = np.array([[0.0,0.5*math.pow(i,2)],[0,i]])     # Matrix B
        A_transpose= np.transpose(A)                      # Matrix A_transpose

        # Time Update 
        uk = np.array([  [  data[i-1][0]  ]  , [   data[i-1][1]  ] ])   # uk given in data 
        xk = np.dot(A ,previous_x) + np.dot(B,uk)                       # xk = A * previous_xk + B * uk
        pk = np.dot(np.dot(A,previous_p),A_transpose) + Q               # pk = A * previous_xk * A_transpose + Q

        
        # Measurement update
        zk = np.array([ [  data[i-1][2] ] , [ data [i-1][3] ]])             # zk given in data 
        inverse = np.linalg.inv(np.dot(np.dot(H,pk),np.transpose(H))+ R)    # inverse of ((H * pk * H_transpose ) + R )
        kk = np.dot(np.dot(pk,np.transpose(H)),inverse)                     # kk = (pk * H_transpose) * inverse of ((H * pk * H_transpose ) + R )
        new_xk = xk + np.dot(kk,(zk - np.dot(H,xk)))                        # new_xk = xk + (kk (zk - (H*xk)))
        new_pk = np.dot((I - np.dot(kk,H)),pk)                              # new_pk = (I - (kk * H)) * pk

        previous_x = new_xk                   # new_xk will become previous_xk for next iteration
        previous_p = new_pk                   # new_pk will become previous_pk for next iteration

        # store value of xk1, xk2, zk1, zk2
        predictedx1.append(new_xk[0])
        predictedx2.append(new_xk[1])
        observationz1.append(zk[0])
        observationz2.append(zk[1])
        
      
        
    # plot values of xk1, xk2, zk1, zk2
    graph(predictedx1,predictedx2,observationz1,observationz2)




        