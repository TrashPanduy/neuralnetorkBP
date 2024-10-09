import math

def forward1Layer(allLayerWeights,hiddenLayers,outputLayer,testData,hiddenLayerAmt,):
    #------* input Layer forward propogation*-------#
    weightPointer = 0
    for node in range(len(hiddenLayers[0])):
        sums = 0
        for digit in range(len(testData[0])):
            sums = sums + (allLayerWeights[0][weightPointer] * testData[0][digit])
            weightPointer = weightPointer + 1
        hiddenLayers[0][node].input = sums
        hiddenLayers[0][node].output = 1/(1+ pow(math.e,(-1 * sums)))
    #------* Output Layer forward propogation*--------#
    weightPointer = 0
    for endNode in range(len(outputLayer)):
        sums = 0
        for hiddenNodes in range(len(hiddenLayers[0])):
            sums = sums + (allLayerWeights[0][weightPointer] * hiddenLayers[0][hiddenNodes].output)
            weightPointer = weightPointer+1
        outputLayer[endNode].input = sums
        outputLayer[endNode].output = 1/(1 + pow(math.e,(-1 * sums)))
    return [allLayerWeights,hiddenLayers,outputLayer]
def forwardMultiLayer(allLayerWeights,hiddenLayers,outputLayer,testData,hiddenLayerAmt,):
    #------* input Layer forward propogation*-------#
    weightPointer = 0
    for node in range(len(hiddenLayers[0])):
        sums = 0
        for digit in range(len(testData)):
            sums = sums + (allLayerWeights[0][weightPointer] * testData[0][digit])
            weightPointer = weightPointer + 1
        hiddenLayers[0][node].input = sums
        hiddenLayers[0][node].output = 1/(1+ pow(math.e,(-1 * sums)))
    
    #------* Hidden Layer forward propogation*--------#
    for layer in range(hiddenLayerAmt - 1):#for each layer
        weightPointer = 0
        for node in range(len(hiddenLayers[layer])): #for each node in the first hidden layer
            sums = 0
            for otherNode in range(len(hiddenLayers[layer + 1]) - 1): #for each node in the second hiddenLayer
                sums = sums + (allLayerWeights[layer + 1][weightPointer] * hiddenLayers[layer][otherNode].output)
                weightPointer = weightPointer + 1
            hiddenLayers[layer + 1][node].input = sums
            hiddenLayers[layer + 1][node].output = 1/(1+ pow(math.e,(-1 * sums)))
    #------* Output Layer forward propogation*--------#
    weightPointer = 0
    for endNode in range(len(outputLayer)):
        sums = 0
        if(hiddenLayerAmt > 1):
            for hiddenNodes in range(len(hiddenLayers[-1])):
                sums = sums + (allLayerWeights[-1][weightPointer] * hiddenLayers[-1][hiddenNodes].output)
                weightPointer = weightPointer+1
        else:
            for hiddenNodes in range(len(hiddenLayers[0])):
                sums = sums + (allLayerWeights[0][weightPointer] * hiddenLayers[0][hiddenNodes].output)
                weightPointer = weightPointer+1
        outputLayer[endNode].input = sums
        outputLayer[endNode].output = 1/(1 + pow(math.e,(-1 * sums)))
    return [allLayerWeights,hiddenLayers,outputLayer]

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

