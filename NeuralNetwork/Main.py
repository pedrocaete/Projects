from NeuralNetwork import NeuralNetwork
import numpy

input_nodes = 784 
hidden_nodes = 200 
output_nodes = 10 
learning_rate = 0.1 
 
 
n = NeuralNetwork(input_nodes,hidden_nodes,output_nodes,learning_rate) 
 
training_data_file = open("mnist_dataset/mnist_train.csv", 'r') 
training_data_list = training_data_file.readlines() 
training_data_file.close() 
 
epochs = 5 
 
for e in range(epochs): 
    for record in training_data_list: 
        all_values = record.split(',') 
        inputs = (numpy.asarray(all_values[1:], dtype=float) / 255.0 * 0.99) + 0.01
        targets = numpy.zeros(output_nodes) + 0.01 
        targets[int(all_values[0])] = 0.99 
        n.train(inputs, targets) 
        pass 
    pass 
 
 
test_data_file = open("mnist_dataset/mnist_test.csv", 'r') 
test_data_list = test_data_file.readlines() 
test_data_file.close() 
 
scorecard = [] 
 
for record in test_data_list: 
    all_values = record.split(',') 
    correct_label = int(all_values[0]) 
    inputs = (numpy.asarray(all_values[1:], dtype=float) / 255.0 * 0.99) + 0.01 
    outputs = n.query(inputs) 
    label = numpy.argmax(outputs) 
    if (label == correct_label): 
        scorecard.append(1) 
    else: 
        scorecard.append(0) 
        pass 
    pass 
 
scorecard_array = numpy.asarray(scorecard) 
print ("performance = ", scorecard_array.sum() / 
scorecard_array.size) 
