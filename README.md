# Knn_Iris

This example helps in understanding the K-Nearest Neighbor Algorithm implementation in Python. The Iris dataset example is used for implementing algorithm and the algorithm is designed using multiple functions so that implementation and formulae used is clear.

# Objective

The objective of this code is find the nearest neighbour for the test data set. The iris dataset has 150 samples and we samples are devided into training dataset and test dataset. The split value for dataset is kept as 0.67 i.e. the dataset is devided into approx 67% as train data and 33% as test data.

The Euclidean Distance is used to calculate the distance between the test data and train data.

The K value for this particular algorithm is 3 i.e. 3 closest neighbors to the test data are appeneded in a list and afterwards the voting among the neighbors is done to predict the outcome. 

# Disadvantages

1. The KNN method works well for small dataset. if we look at the code the distance for each of the test data is calculated with respect to entire training data. If the dataset would have million samples then the calculation of each test data for the entire training dataset would have been very costly and time consuming. Therefore different Algorithms are preferred for larger dataset.

2. Another Disadvantage of KNN is it not recommeded in Image classification as the Vector Matrix for each image is quite high and accuracy of KNN for image classification is very poor. For example for CIFAR-10 Image dataset the accuracy of KNN turns out to be 0.114000 or 11.4% For a training set of 500 images the result was 57 / 500 correct => accuracy: 0.114000 because the training set was of 5000 images per type of Image.
