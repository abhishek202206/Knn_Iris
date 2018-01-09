

# Example of kNN implemented from Scratch in Python
 
import csv
import random
import math
import operator
#from sklearn import datasets

#print (filename) 
def loadDataset(filename, split, trainingSet=[] , testSet=[]):
	with open(filename, 'r') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    for x in range(len(dataset)-1):
	        for y in range(4):
	            # value in the dataset is converted into float from string.
	            dataset[x][y] = float(dataset[x][y])
	            #print (dataset[x][y])
	       # random.random() generates a random floating number between 0.0 to 1.0
	       # The split value is 0.67 therefore it will assign data into training set if the value is less then 0.67 
	       # it will assign the data to test set if the value is greater than split value.
	        if random.random() < split: 
	            trainingSet.append(dataset[x])
	        else:
	            testSet.append(dataset[x])
 
 
def euclideanDistance(instance1, instance2, length):
	distance = 0
	#print (instance1,instance2)
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)
 
def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	#print (length)
	# To get the closest neighbour we calculate the Euciledean Distance between the values in Test set and Training set
	for x in range(len(trainingSet)):
	   # The distance of each testset is compared to element in the training set
	   dist = euclideanDistance(testInstance, trainingSet[x], length)
	   # The training set and its distance from the test set is now stored in a list
	   distances.append((trainingSet[x], dist))
	# Now the distance list is sorted in ascending order
	distances.sort(key=operator.itemgetter(1))
	#print (distances)
	neighbors = []
	for x in range(k):
	    # Since we are interested in closest 3 neighbours so the closest 3 neighbours to the test data are stored in a list
	    neighbors.append(distances[x][0])
	#print (distances[2][1])
	#print (len(neighbors))
	#print (neighbors)
	#print (neighbors[0][-1])
	return neighbors
 
def getResponse(neighbors):
	classVotes = {}
	# Now we need to find which set has the max votes
	# If suppose the neighbors to the test set Virginica are Virginica and Setosa
	# Then out of three neighbours we do voting which set is closest
	# If for virginica set there are two viginica set close to test set then the predicted set is virginica
	for x in range(len(neighbors)):
	    response = neighbors[x][-1]
	    if response in classVotes:
	        classVotes[response] += 1
	    else:
	        classVotes[response] = 1
	sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
	#print (sortedVotes)
	return sortedVotes[0][0]
 
def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0
	
def main():
	# prepare data
	trainingSet=[]
	testSet=[]
	split = 0.67
	loadDataset('iris.data', split, trainingSet, testSet)
	print ('Train set: ' + repr(len(trainingSet)))
	print ('Test set: ' + repr(len(testSet)))
	# generate predictions
	predictions=[]
	k = 3
	for x in range(len(testSet)):
	   # Now each row of testdata is compared with training data to find the closest similarity
	   #print (testSet[x])
	   neighbors = getNeighbors(trainingSet, testSet[x], k)
	   result = getResponse(neighbors)
	   predictions.append(result)
	   print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
	accuracy = getAccuracy(testSet, predictions)
	print('Accuracy: ' + repr(accuracy) + '%')
	
main()