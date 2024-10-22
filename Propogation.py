import math

#forwardProp input (2dArray, 2DArray). Returns 2dArray(neuralNetwork)
#forward propogation. //ABSTRACT -> Runs through network once, propogating values forwards
#nauralNetwork is the entire network. testData is a 2Darray, img of number, and the value
def forwardProp(neuralNetwork, testData):
    print("Hello World")
    neuralNetwork[0] = testData[0]
    del neuralNetwork[1]
    weightPointer = 0
    for row in range(len(neuralNetwork)):
        print(neuralNetwork[row][0])
    #first hiddenLayer as it recieves int from input instead of .output from past layer node
    for node in range(len(neuralNetwork[2])):
        #ABSTRACT -> 'sums' represents the inputValue of each input, times the weight connecting it to hidden node being calculated.
        sums = 0
        for digit in range(len(neuralNetwork[0])):
            sums = sums + (neuralNetwork[1][weightPointer] * neuralNetwork[0][digit])
            weightPointer = weightPointer + 1
        neuralNetwork[2][node].input = sums
        #each node is basically a function, the below equation is the output.
        #in future exchange this with a function or method for interchangable formulas.
        neuralNetwork[2][node].output = 1/(1+ pow(math.e,(-1 * sums)))
    
    #forward Propogation for the rest of hiddenLayers
    for layer in range(4, len(neuralNetwork), 2):
        if(len(neuralNetwork[layer]) == len(neuralNetwork[2])):
            weightPointer = 0
            for node in range(len(neuralNetwork[layer])):
                sums = 0
                for digit in range(len(neuralNetwork[layer - 2])):
                    sums = sums + (neuralNetwork[layer-1][weightPointer] * neuralNetwork[layer-2][digit].output)
                    weightPointer = weightPointer + 1
                neuralNetwork[layer][node].input = sums
                neuralNetwork[layer][node].output = 1/(1+ pow(math.e,(-1 * sums)))
    #forward propogation for output layer
    weightPointer = 0
    for node in range(len(neuralNetwork[-1])):
        sums = 0
        for hiddenNodes in range(len(neuralNetwork[-3])):
            sums = sums + (neuralNetwork[-2][weightPointer] * neuralNetwork[-3][hiddenNodes].output)
            weightPointer = weightPointer+1
        neuralNetwork[-1][node].input = sums
        neuralNetwork[-1][node].output = 1/(1 + pow(math.e,(-1 * sums)))
    
    return neuralNetwork

#backwardProp input (2dArray, 2DArray, float). Returns 2dArray(neuralNetwork)
#backward propogation. //ABSTRACT -> goes through the network backwards in order to change weights and errors to their respective values
# variable 'neuralNetwork' is the entire network. 'testData' is 2Darray with first row being image data and second what is represents. 'learnRate' self explanatory
def backwardProp(neuralNetwork,testData, learnRate):
    #outputLayer backpropogation. Same for all feed forward networks
    tempError = 0
    weightPointer = 0
    for outputNode in range(len(neuralNetwork[-1])):
        tempError = neuralNetwork[-1][outputNode].output * (1-neuralNetwork[-1][outputNode].output) * (testData[1][outputNode] - neuralNetwork[-1][outputNode].output)
        neuralNetwork[-1][outputNode].error = tempError
        for hiddenLayerNode in range(len(neuralNetwork[-3])):
            changeWeightValue = neuralNetwork[-3][hiddenLayerNode].output * learnRate * tempError
            neuralNetwork[-2][weightPointer] = neuralNetwork[-2][weightPointer] + changeWeightValue
            weightPointer = weightPointer + 1
    # hiddenLayer back propogation. change nodes then weights on repeat. 
    for layer in range(-3, -1*(len(neuralNetwork) - 2), -2):
        #stop early due to dataType input problems(I'm a dumbass)
        if len(neuralNetwork) + layer == 2:
            break
        weightPointer = 0
        #change hiddenNode error
        for hiddenNode in range(len(neuralNetwork[layer])):
            totalError = 0
            for rightNode in range(len(neuralNetwork[layer + 2])):
                totalError = totalError + (neuralNetwork[layer + 2][rightNode].error * neuralNetwork[layer + 1][weightPointer])
                weightPointer = weightPointer + 1
            error = neuralNetwork[layer][hiddenNode].output * (1-neuralNetwork[layer][hiddenNode].output) * totalError
            neuralNetwork[layer][hiddenNode].error = error
        #change weight error in row that comes b4 hiddenNodes row
        weightPointer = 0
        for leftNode in range(len(neuralNetwork[layer - 2])):
            for rightNode in range(len(neuralNetwork[layer])):
                changeWeightValue = neuralNetwork[layer - 2][leftNode].output * learnRate * neuralNetwork[layer][rightNode].error
                neuralNetwork[layer - 1][weightPointer] = neuralNetwork[layer - 1][weightPointer] + changeWeightValue
                weightPointer = weightPointer + 1

    #For input layer back propogation
    weightPointer = 0
    oWPointer = 0
    for changedNode in range(len(neuralNetwork[2])):
        totalError = 0
        for node in range(len(neuralNetwork[4])):
            totalError = totalError + (neuralNetwork[4][node].error * neuralNetwork[3][weightPointer])
            weightPointer = weightPointer + 1
        error = neuralNetwork[2][changedNode].output * (1-neuralNetwork[2][changedNode].output) * totalError
        neuralNetwork[2][changedNode].error = error
        for digit in range(len(neuralNetwork[0])):
            changeWeightValue = learnRate * error * testData[0][digit]
            neuralNetwork[1][oWPointer] += changeWeightValue
            oWPointer = oWPointer + 1

    return neuralNetwork