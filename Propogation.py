import math

#forwardProp input (2dArray, 2DArray, float). Returns 2dArray
#forward propogation. //ABSTRACT -> Runs through network once, propogating values forwards
#nauralNetwork is the entire network. testData is a 2Darray, img of number, and the value
def forwardProp(neuralNetwork, testData, learnRate):
    print("Hello World")
    neuralNetwork[0] = testData[0]
    weightPointer = 0
    #first hiddenLayer as it recieves int from input instead of .output from past layer node
    for node in neuralNetwork[2]:
        #ABSTRACT -> 'sums' represents the inputValue of each input, times the weight connecting it to hidden node being calculated.
        sums = 0
        for digit in neuralNetwork[0]:
            sums = sums + (neuralNetwork[1][weightPointer] * neuralNetwork[0][digit])
            weightPointer = weightPointer + 1
        neuralNetwork[2][node].input = sums
        #each node is basically a function, the below equation is the output.
        #in future exchange this with a function or method for interchangable formulas.
        neuralNetwork[2][node].output = 1/(1+ pow(math.e,(-1 * sums)))
    
    #forward Propogation for the rest of hiddenLayers
    for layer in range(4, len(neuralNetwork), 2):
        if(neuralNetwork[layer].length == neuralNetwork[2].length):
            weightPointer = 0
            for node in (neuralNetwork[layer].length):
                sums = 0
                for digit in neuralNetwork[layer - 2].length:
                    sums = sums + (neuralNetwork[layer-1][weightPointer] * neuralNetwork[layer-2][digit].output)
                    weightPointer = weightPointer + 1
                neuralNetwork[layer][node].input = sums
                neuralNetwork[layer][node].output = 1/(1+ pow(math.e,(-1 * sums)))
    #forward propogation for output layer
    weightPointer = 0
    for node in neuralNetwork[-1]:
        sums = 0
        for hiddenNodes in neuralNetwork[-3]
            sums = sums + (allLayerWeights[0][weightPointer] * hiddenLayers[0][hiddenNodes].output)
            weightPointer = weightPointer+1
        neuralNetwork[-1][node].input = sums
        neuralNetwork[-1][node].output = 1/(1 + pow(math.e,(-1 * sums)))
    
    return neuralNetwork


def back1Layer(allLayerWeights,hiddenLayers,outputLayer,testData,learnRate):
    #------* Output Layer back propogation*--------#
    tempError = 0
    weightPointer = 0
    for outputNode in range(len(outputLayer)):
        tempError = outputLayer[outputNode].output * (1-outputLayer[outputNode].output)*(testData[1][outputNode] - outputLayer[outputNode].output)
        outputLayer[outputNode].error = tempError
        for hiddenNode in range(len(hiddenLayers[0])):
            changeWeightValue = hiddenLayers[0][hiddenNode].output * learnRate * tempError
            allLayerWeights[0][weightPointer] = allLayerWeights[0][weightPointer] + changeWeightValue
            weightPointer = weightPointer + 1
    #------* Input Layer back propogation*--------#
    weightPointer = 0
    otherweightPointer = 0
    for changeNode in range(len(hiddenLayers[0])): #for each node in node list RIGHT
            totalError = 0
            for node in range(len(outputLayer)):
                totalError = totalError + (outputLayer[node].error * allLayerWeights[1][weightPointer])
                weightPointer = weightPointer + 1
            error = hiddenLayers[0][changeNode].output * (1-hiddenLayers[0][changeNode].output) * totalError
            hiddenLayers[0][changeNode].error = error
            for digit in range(len(testData[0])):
                changeWeightValue = learnRate * error * testData[0][digit]
                allLayerWeights[0][otherweightPointer] = allLayerWeights[0][otherweightPointer] + changeWeightValue
                otherweightPointer = otherweightPointer + 1
    return [allLayerWeights,hiddenLayers,outputLayer]
def backMultiLayer(allLayerWeights,hiddenLayers,outputLayer,testData,hiddenLayerAmt,learnRate):
    #------* Output Layer back propogation*--------#
    tempError = 0
    weightPointer = 0
    for outputNode in range(len(outputLayer)):
        tempError = outputLayer[outputNode].output * (1-outputLayer[outputNode].output)*(testData[1][outputNode] - outputLayer[outputNode].output)
        outputLayer[outputNode].error = tempError
        for hiddenNode in range(len(hiddenLayers[-1])):
            changeWeightValue = hiddenLayers[-1][hiddenNode].output * learnRate * tempError
            allLayerWeights[-1][weightPointer] = allLayerWeights[-1][weightPointer] + changeWeightValue
            weightPointer = weightPointer + 1
    #------* Hidden Layer back propogation*--------#
    weightPointer = 0
    #adjust last hiddenLayer error
    for node in range(len(hiddenLayers[-1])): 
        tempError = 0
        for outputNode in range(len(outputLayer) - 1):
            tempError = tempError + (outputLayer[outputNode].error * allLayerWeights[-1][weightPointer])
            weightPointer = weightPointer + 1
        nodeError = (hiddenLayers[-1][node].output * (1-hiddenLayers[-1][node].output) * tempError)
        hiddenLayers[-1][node].error = nodeError
    #loop through from end -1 to 0 and adjust weight / error (central bit of stuff)
    for layer in reversed(range(hiddenLayerAmt - 1)):
        weightPointer = 0
        #adjust weight
        for node in range(len(hiddenLayers[layer])):
            for rightNode in range(len(hiddenLayers[layer + 1])):
                changeWeightValue = hiddenLayers[layer + 1][rightNode].error * learnRate * hiddenLayers[layer][node].output
                allLayerWeights[layer + 1][weightPointer] = allLayerWeights[layer + 1][weightPointer] + changeWeightValue
                weightPointer = weightPointer + 1
        #adjust node error
        weightPointer = 0
        for node in range(len(hiddenLayers[layer])):
            tempError = 0
            for rightNode in range(len(hiddenLayers[layer + 1])):
                tempError = tempError + (hiddenLayers[layer + 1][rightNode]).error * allLayerWeights[layer + 1][weightPointer]
                weightPointer = weightPointer + 1
            nodeError = (hiddenLayers[layer][node].output * (1-hiddenLayers[layer][node].output) * tempError)
            hiddenLayers[layer][node].error = nodeError
    weightPointer = 0
    for digit in range(len(testData[0])):
        for node in range(len(hiddenLayers[0])):
            changeWeightValue = hiddenLayers[0][node].error * learnRate * digit
            allLayerWeights[0][weightPointer] = allLayerWeights[0][weightPointer] + changeWeightValue
            weightPointer = weightPointer + 1
    return [allLayerWeights,hiddenLayers,outputLayer]

