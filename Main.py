import dataProcessing
import Propogation
import random
#mostly for Eulers number 
import math

class Node:
    def __init__(self, input, output, error):
        self.input = input
        self.output = output
        self.error = error

class Main:
    
    #initialize network nodes & random weights according to hyperValues
    @staticmethod
    def initializeLayers():
        neuralNetwork = [[]]
        #generate input nodes
        tempArr = []
        for layerVals in range(inputNodesAmt):
            newNode = Node(None,None,None)
            tempArr.append(newNode)
        #add input nodes to array
        neuralNetwork.append(tempArr)

        #generate input to hidden layer weights
        tempArr = []
        for value in range(inputNodesAmt * hiddenNodesPerLayer):
            tempArr.append(random.uniform(weightsLower,weightsHigher))
        neuralNetwork.append(tempArr)

        #generate hiddenLayer nodes 
        tempHiddenArr = [[]]
        for layers in range(hiddenLayerAmt):
            tempArr = []
            for node in range(hiddenNodesPerLayer):
                newNode = Node(None,None,None)
                tempArr.append(newNode)
            tempHiddenArr.append(tempArr)

        #generate weights
        tempWeights = [[]]
        if(hiddenLayerAmt > 1):
            for layers in range(hiddenLayerAmt - 1):
                tempArr = []
                for value in range(inputNodesAmt * hiddenNodesPerLayer):
                    tempArr.append(random.uniform(weightsLower,weightsHigher))
                tempWeights.append(tempArr)
        tempArr = []
        for value in range(outputNodesAmt * hiddenNodesPerLayer):
            tempArr.append(random.uniform(weightsLower,weightsHigher))
        tempWeights.append(tempArr)

        for row in range(len(tempHiddenArr)):
            neuralNetwork.append(tempHiddenArr[row])
            neuralNetwork.append(tempWeights[row])
        #generate outputNodes
        tempArr = []
        for outputNodes in range(outputNodesAmt):
            newNode = Node(None,None,None)
            tempArr.append(newNode)
        neuralNetwork.append(tempArr)
        #neuralNetwork has been fully generated.
        print("network setup complete")
        return neuralNetwork
    
    @staticmethod
    def checkAcuracy():
        index = 0
        count = 0 
        while index < len(validationData):
            expectedValue = validationData[index][1]
            testedData = validationData[index]
            nerualNetwork = Propogation.forwardPropogation(nerualNetwork,testedData)
            tempOutputLayer = nerualNetwork[-1]
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




#Neural network variables
hiddenLayerAmt = 2
hiddenNodesPerLayer = 17
outputNodesAmt = 10
inputNodesAmt = 15
learnRate = .07
iterations = 7000
weightsLower = -0.7
weightsHigher = 0.7
nerualNetwork = Main.initializeLayers()
testData = dataProcessing.initializeData().getLearningData()
validationData = dataProcessing.initializeData().getValidateData()
row1Validation = validationData[0]
row1testData = testData[0]





for i in range(iterations):
    
    counter = 0
    random.shuffle(testData)
    random.shuffle(testData)
    #if i % 1000 == 0:
        #print(nerualNetwork[0][5].error)
        #print(outputLayer[5].error)
    while counter < len(testData):
        row1testData = testData[counter]
        nerualNetwork = Propogation.forwardProp(nerualNetwork,row1testData)
        nerualNetwork = Propogation.backwardProp(nerualNetwork,row1testData,learnRate)
        counter = counter + 1


score = Main.checkAcuracy()
print(score, "/",len(validationData))
print("done")

