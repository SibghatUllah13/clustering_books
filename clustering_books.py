import matplotlib.pyplot as plt
import numpy as np
import os

def total(array): #Function to calculate total of an array
    total=0
    for i in range(len(array)):
        total=total+array[i]
    return total
    
def char_freq(file_name, filt): #Function which reads a file based on characters in filter
    data=[]
    counter_array=np.zeros(len(filt))
    cwd=os.getcwd()
    path=cwd+"\\"+file_name
    file=open(path,'r',encoding='utf-8')
    for line in file:
        data.append(line)
    words=str(data)
    for character in words:
        for i in range(len(filt)):
            if character==filt[i]:
                counter_array[i]+=1
    tot=total(counter_array)            
    for i in range(len(counter_array)):
        counter_array[i]=counter_array[i]/tot
    return counter_array

def plot_histogram(array):
    plt.figure()
    for char_count in array:
        plt.subplot(411)
        plt.hist(char_count)
        plt.show()
        plt.savefig('histograms_of_books.png')
        
def euc_distance(x,y): #Calculating Eucledian Distance between two Multidimentional Vectors of Same Length
        return  np.sqrt(np.sum((x-y)**2))
    
def cluster_distance(c1,c2): #Cluster_distance
    matrix=np.zeros((len(c1),len(c2)))
    for i in range(len(c1)):
        for j in range(len(c2)):
            matrix[i,j]=euc_distance(c1[i],c2[j])
    return np.min(matrix)

def cldist(c1,c2):  #Minimum Cluster_distance
    d=np.infty
    for x in c1:
        for y in c2:
            if euc_distance(x,y)<d:
                d=euc_distance(x,y)
    return d

def closest_cluster(clusters): #Find the closest cluster out of list of clusters
    matrix=np.ones((len(clusters),len(clusters)))
    matrix=matrix*np.infty
    for i in range(len(clusters)):
        for j in range(len(clusters)):
            if i!=j:
                matrix[i,j]=cldist(clusters[i],clusters[j])
                    
    return find_minimum(matrix)

def find_minimum(D):
    minimum=np.argmin(D)
    cluster_index=np.unravel_index(minimum,D.shape)
    return cluster_index

def closest(L): #Find the closest cluster out of list of clusters
    d=np.infty
    a,b=-1,-1
    for i in range(len(L)-1):
        for j in range(i+1,len(L)):
            if cldist(L[i],L[j])<d:
                d=cldist(L[i],L[j])
                a,b=i,j
    return (a,b)
    
