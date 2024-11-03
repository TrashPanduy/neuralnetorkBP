import dataProcessing
import Propogation
import random
#mostly for Eulers number 
import math

class Node:
    def __init__(self, input: float, output: float, error: float):
        self.input = input
        self.output = output
        self.error = error

class Main:
    
    #initialize network nodes & random weights according to hyperValues
    @staticmethod
    def initializeLayers():
        neural_network = [[]]
        #generate input nodes
        temp_arr = []
        for _ in range(input_nodes_amt):
            input_value = -1
            temp_arr.append(input_value)
        #add input nodes to array
        neural_network.append(temp_arr)

        #generate input to hidden layer weights
        temp_arr = []
        for _ in range(input_nodes_amt * hidden_nodes_per_layer):
            temp_arr.append(random.uniform(weights_lower_bound,weights_upper_bound))
        neural_network.append(temp_arr)

        #generate hiddenLayer nodes 
        temp_hidden_arr = [[]]
        for _ in range(hidden_layer_amt):
            temp_arr = []
            for __ in range(hidden_nodes_per_layer):
                new_node = Node(None,None,None)
                temp_arr.append(new_node)
            temp_hidden_arr.append(temp_arr)

        #generate weights
        temp_weights = [[]]
        if(hidden_layer_amt > 1):
            for _ in range(hidden_layer_amt - 1):
                temp_arr = []
                for _ in range(input_nodes_amt * hidden_nodes_per_layer):
                    temp_arr.append(random.uniform(weights_lower_bound,weights_upper_bound))
                temp_weights.append(temp_arr)
        temp_arr = []
        for _ in range(output_nodes_amt * hidden_nodes_per_layer):
            temp_arr.append(random.uniform(weights_lower_bound,weights_upper_bound))
        temp_weights.append(temp_arr)

        del temp_hidden_arr[0]
        del temp_weights[0]

        for row in range(len(temp_hidden_arr)):
            neural_network.append(temp_hidden_arr[row])
            neural_network.append(temp_weights[row])
        #generate outputNodes
        temp_arr = []
        for _ in range(output_nodes_amt):
            new_node = Node(None,None,None)
            temp_arr.append(new_node)
        neural_network.append(temp_arr)
        #neural_network has been fully generated.
        return neural_network
    
    #takes a 2dArray/ the neural network
    @staticmethod
    def checkAcuracy(nerual_network):
        index = 0
        count = 0 
        while index < len(validation_data):
            expected_value = validation_data[index][1]
            tested_data = validation_data[index]
            nerual_network = Propogation.forwardProp(nerual_network,tested_data)
            temp_output_layer = nerual_network[-1]
            correct_index = -1
            greatest_output = -1
            for i in range(len(temp_output_layer)):
                #print("outputValue: ", temp_output_layer[i].output)
                if expected_value[i] == 1:
                    correct_index = i
                if temp_output_layer[i].output > greatest_output:
                    greatest_output = temp_output_layer[i].output
                    greatest_index = i
            
            #print("number found:", greatest_index)
            #print("expected number:", correct_index)

            if greatest_index == correct_index:
                count += 1

            #print("value to test for: ", validation_data[index][1])
            index += 1
        
        return count

if __name__ == "__main__":
    #Neural network variables
    hidden_layer_amt = 2
    hidden_nodes_per_layer = 15
    output_nodes_amt = 10
    input_nodes_amt = 15
    learn_rate = .07
    iterations = 5000
    weights_lower_bound = -0.7
    weights_upper_bound = 0.7
    nerual_network = Main.initializeLayers()
    test_data = dataProcessing.initializeData().getLearningData()
    validation_data = dataProcessing.initializeData().getValidateData()
    row1_validation = validation_data[0]
    row1_test_data = test_data[0]


    #don't ask why this is here, it just needs to be
    row1_test_data = test_data[0]
    nerual_network[0] = row1_test_data[0]
    del nerual_network[1]

    #learning looping
    for i in range(iterations):
        counter = 0
        random.shuffle(test_data)
        random.shuffle(test_data)
        #if i % 1000 == 0:
            #print(nerual_network[2][5].error)
            #print("weight",nerual_network[1][10])
            
        while counter < len(test_data):
            row1_test_data = test_data[counter]
            nerual_network[0] = row1_test_data[0]
            nerual_network = Propogation.forwardProp(nerual_network,row1_test_data)
            nerual_network = Propogation.backwardProp(nerual_network,row1_test_data,learn_rate)
            counter = counter + 1


    score = Main.checkAcuracy(nerual_network)
    print("Training Complete, Accuracy:")
    print(score, "/",len(validation_data))