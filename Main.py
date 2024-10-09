import dataProcessing
import Propogation
import random
#mostly for Eulers number 
import math

#Neural network variables
#implements xyz calculation

class node:
    def __init__(self, input, output, error):
        self.input = input
        self.output = output
        self.error = error

class main:
    #initialize network nodes & random weights according to hyperValues
    def initializeHiddenLayers():
        #initialize hidden layers & neural nodes to be stored in 2dArray 'hiddenLayers'
        hiddenLayers = [[]]
        for layerNum in range(hiddenLayerAmt):
            tempArray = []
            for layerVals in range(hiddenNodesPerLayer):
                newNode = node(None,None,None)
                tempArray.append(newNode)
            
            hiddenLayers.append(tempArray)

        hiddenLayers.pop(0)
        return hiddenLayers
    def initializeOutputLayers():
        #initialize output layer & neural netowrk, store in 1d array.
        outputLayer = []
        for layerVals in range(outputNodesAmt):
            newNode = node(None,None,None)
            outputLayer.append(newNode)
        return outputLayer
    def initializeWeights():
        #create random weights to propogate network with
        #format of array will be [inputToHiddenWeights, HiddenToHiddenWeights, HiddenToOutputWeights]
        tempArray = []
        allLayerWeights = [[]]
        for value in range(inputNodes * hiddenNodesPerLayer):
            tempArray.append(random.uniform(-.7,.7))
        allLayerWeights.append(tempArray)

        if(hiddenLayerAmt > 1):
            for i in range(hiddenLayerAmt):
               tempArray = []
               for value in range(hiddenNodesPerLayer * hiddenNodesPerLayer):
                    tempArray.append(random.uniform(-.7,.7)) 
               allLayerWeights.append(tempArray) 
        
        for value in range(outputNodesAmt * hiddenNodesPerLayer):
            tempArray.append(random.uniform(-.7,.7))
        allLayerWeights.append(tempArray)
        allLayerWeights.pop(0)
        return allLayerWeights
    def checkAcuracy():
        index = 0
        count = 0 
        while index < len(validationData):
            expectedValue = validationData[index][1]
            testedData = validationData[index]
            tempArray = Propogation.forward1Layer(allLayerWeights,hiddenLayers,outputLayer,testedData,hiddenLayerAmt)
            tempOutputLayer = tempArray[2]
            correctIndex = -1
            greatestOutput = -1
            for i in range(len(tempOutputLayer)):
                print("outputValue: ", tempOutputLayer[i].output)
                if expectedValue[i] == 1:
                    correctIndex = i
                if tempOutputLayer[i].output > greatestOutput:
                    greatestOutput = tempOutputLayer[i].output
                    greatestIndex = i
            
            print("number found:", greatestIndex)
            print("expected number:", correctIndex)

            if greatestIndex == correctIndex:
                count += 1

            print("value to test for: ", validationData[index][1])
            index += 1
        return count

        



hiddenLayerAmt = 1
hiddenNodesPerLayer = 17
outputNodesAmt = 10
inputNodes = 15
learnRate = .07
iterations = 7000
hiddenLayers = main.initializeHiddenLayers()
outputLayer = main.initializeOutputLayers()
allLayerWeights = main.initializeWeights()
testData = dataProcessing.initializeData().getLearningData()
validationData = dataProcessing.initializeData().getValidateData()
row1Validation = validationData[0]
row1testData = testData[0]


if(hiddenLayerAmt > 1):
    for i in range(iterations):
        counter = 0
        random.shuffle(testData)
        random.shuffle(testData)
        if i % 1000 == 0:
            print(hiddenLayers[0][5].error)
            print(outputLayer[5].error)
        while counter < len(testData):
            row1testData = testData[counter]
            tempArray = Propogation.forwardMultiLayer(allLayerWeights,hiddenLayers,outputLayer,row1testData,hiddenLayerAmt)
            allLayerWeights = tempArray[0]
            hiddenLayers = tempArray[1]
            outputLayer = tempArray[2]
            tempArray = Propogation.backMultiLayer(allLayerWeights,hiddenLayers,outputLayer,row1testData,hiddenLayerAmt,learnRate)
            allLayerWeights = tempArray[0]
            hiddenLayers = tempArray[1]
            outputLayer = tempArray[2]
            counter = counter + 1
else:
    for i in range(iterations):
        counter = 0
        random.shuffle(testData)
        random.shuffle(testData)
        if i % 1000 == 0:
            print(hiddenLayers[0][5].error)
            print(outputLayer[5].error)
        while counter < len(testData):
            row1testData = testData[counter]
            tempArray = Propogation.forward1Layer(allLayerWeights,hiddenLayers,outputLayer,row1testData,hiddenLayerAmt)
            allLayerWeights = tempArray[0]
            hiddenLayers = tempArray[1]
            outputLayer = tempArray[2]
            tempArray = Propogation.back1Layer(allLayerWeights,hiddenLayers,outputLayer,row1testData,learnRate)
            allLayerWeights = tempArray[0]
            hiddenLayers = tempArray[1]
            outputLayer = tempArray[2]
            counter = counter + 1

score = main.checkAcuracy()
print(score, "/",len(validationData))
print("done")
