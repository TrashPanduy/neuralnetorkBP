import dataProcessing
import Propogation
import random
#mostly for Eulers number 
import math

#Neural network variables
#implements xyz calculation
hiddenLayerAmt = 2
hiddenNodesPerLayer = 17
outputNodesAmt = 10
inputNodesAmt = 15
learnRate = .07
iterations = 7000
weightsLower = -0.7
weightsHigher = 0.7
nerualNetwork = main.initializenerualNetwork()
outputLayer = main.initializeOutputLayers()
allLayerWeights = main.initializeWeights()
testData = dataProcessing.initializeData().getLearningData()
validationData = dataProcessing.initializeData().getValidateData()
row1Validation = validationData[0]
row1testData = testData[0]

class node:
    def __init__(self, input, output, error):
        self.input = input
        self.output = output
        self.error = error

class main:
    #initialize network nodes & random weights according to hyperValues
    def initializeLayers():
        nerualNetwork = [[]]
        #generate input nodes
        tempArr = []
        for layerVals in range(inputNodesAmt):
            newNode = node(None,None,None)
            tempArr.append(newNode)
        #add input nodes to array
        nerualNetwork.append(tempArr)

        #generate hiddenLayer nodes
        tempHiddenNodes = [[]]
        for layers in hiddenLayerAmt:
            for node in hiddenNodesPerLayer:
                newNode = node(None,None,None)
                tempHiddenNodes[layers].append(newNode)

        #add hiddenLayer nodes and weights to network
        for layers in hiddenLayerAmt:
            #generate weights
            tempArr = []
            for value in range(inputNodesAmt * hiddenNodesPerLayer):
                tempArr.append(random.uniform(weightsLower,weightsHigher))
            #add weights then nodes. Last row will be nodes.
            neuralNetwork.append(tempArr)
            neuralNetwork.append(tempHiddenNodes[layers])
        #add new row of weights to leave only output nodes ungenerated
        tempArr = []
            for value in range(inputNodesAmt * hiddenNodesPerLayer):
                tempArr.append(random.uniform(weightsLower,weightsHigher))
            neuralNetwork.append(tempArr)
        
        #generate outputNodes
        tempArr = []
        for outputNodes in outputNodesAmt:
            newNode = node(None,None,None)
            tempArr.append(newNode)
        neuralNetwork.append(tempArr)
        #nerualNetwork has been fully generated.
        return nerualNetwork

    def checkAcuracy():
        index = 0
        count = 0 
        while index < len(validationData):
            expectedValue = validationData[index][1]
            testedData = validationData[index]
            tempArray = Propogation.forward1Layer(allLayerWeights,nerualNetwork,outputLayer,testedData,hiddenLayerAmt)
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


for i in range(iterations):
    counter = 0
    random.shuffle(testData)
    random.shuffle(testData)
    if i % 1000 == 0:
        #print(nerualNetwork[0][5].error)
        #print(outputLayer[5].error)
    while counter < len(testData):
        row1testData = testData[counter]
        tempArray = Propogation.forwardMultiLayer(nerualNetwork,row1testData,learnRate)
        tempArray = Propogation.backMultiLayer(allLayerWeights,nerualNetwork,outputLayer,row1testData,hiddenLayerAmt,learnRate)
        counter = counter + 1

score = main.checkAcuracy()
print(score, "/",len(validationData))
print("done")
