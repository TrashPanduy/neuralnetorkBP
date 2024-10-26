import math

#forwardProp input (2dArray, 2DArray). Returns 2dArray(neural_network)
#forward propogation. //ABSTRACT -> Runs through network once, propogating values forwards
#nauralNetwork is the entire network. test_data is a 2Darray, img of number, and the value
def forwardProp(neural_network, test_data):
    weight_pointer = 0
    #first hiddenLayer as it recieves int from input instead of .output from past layer node
    for node in range(len(neural_network[2])):
        #ABSTRACT -> 'sums' represents the inputValue of each input, times the weight connecting it to hidden node being calculated.
        sums = 0
        for digit in range(len(neural_network[0])):
            sums = sums + (neural_network[1][weight_pointer] * neural_network[0][digit])
            weight_pointer = weight_pointer + 1
        neural_network[2][node].input = sums
        #each node is basically a function, the below equation is the output.
        #in future exchange this with a function or method for interchangable formulas.
        neural_network[2][node].output = 1/(1+ pow(math.e,(-1 * sums)))
    
    #forward Propogation for the rest of hiddenLayers
    for layer in range(4, len(neural_network), 2):
        if(len(neural_network[layer]) == len(neural_network[2])):
            weight_pointer = 0
            for node in range(len(neural_network[layer])):
                sums = 0
                for digit in range(len(neural_network[layer - 2])):
                    sums = sums + (neural_network[layer-1][weight_pointer] * neural_network[layer-2][digit].output)
                    weight_pointer = weight_pointer + 1
                neural_network[layer][node].input = sums
                neural_network[layer][node].output = 1/(1+ pow(math.e,(-1 * sums)))
    #forward propogation for output layer
    weight_pointer = 0
    for node in range(len(neural_network[-1])):
        sums = 0
        for hidden_nodes in range(len(neural_network[-3])):
            sums = sums + (neural_network[-2][weight_pointer] * neural_network[-3][hidden_nodes].output)
            weight_pointer = weight_pointer+1
        neural_network[-1][node].input = sums
        neural_network[-1][node].output = 1/(1 + pow(math.e,(-1 * sums)))
    
    return neural_network

#backwardProp input (2dArray, 2DArray, float). Returns 2dArray(neural_network)
#backward propogation. //ABSTRACT -> goes through the network backwards in order to change weights and errors to their respective values
# variable 'neural_network' is the entire network. 'test_data' is 2Darray with first row being image data and second what is represents. 'learn_rate' self explanatory
def backwardProp(neural_network,test_data, learn_rate):
    #outputLayer backpropogation. Same for all feed forward networks
    temp_error = 0
    weight_pointer = 0
    for output_node in range(len(neural_network[-1])):
        temp_error = neural_network[-1][output_node].output * (1-neural_network[-1][output_node].output) * (test_data[1][output_node] - neural_network[-1][output_node].output)
        neural_network[-1][output_node].error = temp_error
        for hidden_layer_node in range(len(neural_network[-3])):
            change_weight_value = neural_network[-3][hidden_layer_node].output * learn_rate * temp_error
            neural_network[-2][weight_pointer] = neural_network[-2][weight_pointer] + change_weight_value
            weight_pointer = weight_pointer + 1
    # hiddenLayer back propogation. change nodes then weights on repeat. 
    for layer in range(-3, -1*(len(neural_network) - 2), -2):
        #stop early due to dataType input problems(I'm a dumbass)
        if len(neural_network) + layer == 2:
            break
        weight_pointer = 0
        #change hidden_node error
        for hidden_node in range(len(neural_network[layer])):
            total_error = 0
            for right_node in range(len(neural_network[layer + 2])):
                total_error = total_error + (neural_network[layer + 2][right_node].error * neural_network[layer + 1][weight_pointer])
                weight_pointer = weight_pointer + 1
            error = neural_network[layer][hidden_node].output * (1-neural_network[layer][hidden_node].output) * total_error
            neural_network[layer][hidden_node].error = error
        #change weight error in row that comes b4 hidden_nodes row
        weight_pointer = 0
        for left_node in range(len(neural_network[layer - 2])):
            for right_node in range(len(neural_network[layer])):
                change_weight_value = neural_network[layer - 2][left_node].output * learn_rate * neural_network[layer][right_node].error
                neural_network[layer - 1][weight_pointer] = neural_network[layer - 1][weight_pointer] + change_weight_value
                weight_pointer = weight_pointer + 1

    #For input layer back propogation
    weight_pointer = 0
    first_weight_pointer = 0
    for changed_node in range(len(neural_network[2])):
        total_error = 0
        for node in range(len(neural_network[4])):
            total_error = total_error + (neural_network[4][node].error * neural_network[3][weight_pointer])
            weight_pointer = weight_pointer + 1
        error = neural_network[2][changed_node].output * (1-neural_network[2][changed_node].output) * total_error
        neural_network[2][changed_node].error = error
        for digit in range(len(neural_network[0])):
            change_weight_value = learn_rate * error * test_data[0][digit]
            neural_network[1][first_weight_pointer] += change_weight_value
            first_weight_pointer = first_weight_pointer + 1

    return neural_network