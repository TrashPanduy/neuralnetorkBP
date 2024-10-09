import random
#mostly for Eulers number 
import math


class hiddenNode():
    def __init__(self, inpuToHNode = None, outputValue = None, error = None):
        self.inpuToHNode = inpuToHNode
        self.outputValue = outputValue
        self.error = error
class outputNode():
    def __init__(self, inpuToONode = None, outputValue = None, error = None):
        self.inpuToONode = inpuToONode
        self.outputValue = outputValue
        self.error = error
#-------------------------------------------^constructors--------------- Forward Propogation ------------------
def forwardPropogation(hiddenLayerWeights,outputLayerWeights,hiddenNodesArr,outputNodesArr,testData):
    #------* Hidden Layer forward propogation*-------#
    
    jk = 0
    for i in range(len(hiddenNodesArr)):   
        sums = 0
        for j in range(len(testData)):
            sums = sums + (hiddenLayerWeights[jk] * testData[j])
            jk = jk+1
        hiddenNodesArr[i].inpuToHNode = sums      #sigmoidnrepresents activation function
        hiddenNodesArr[i].outputValue = 1/(1 + pow(math.e,(-1 * sums)))
        
    #------* Output Layer forward propogation*--------#
        
    jk = 0
    for i in range(len(outputNodesArr)):
        sums = 0
        for j in range(len(hiddenNodesArr)):
            sums = sums + (outputLayerWeights[jk] * hiddenNodesArr[j].outputValue)
            jk = jk+1
        outputNodesArr[i].inpuToONode = sums
        outputNodesArr[i].outputValue = 1/(1 + pow(math.e,(-1 * sums))) 
def backPropogation(hiddenLayerWeights,outputLayerWeights,hiddenNodesArr,outputNodesArr,testData,validationData,LR):
    #------* Output Layer back propogation*--------#
    jk = 0
    Sh = 0
    for i in range(len(outputNodesArr)):
        Sh = outputNodesArr[i].outputValue*(1 - outputNodesArr[i].outputValue)*(validationData[i] - outputNodesArr[i].outputValue)
        outputNodesArr[i].error = Sh
        for j in range(len(hiddenNodesArr)):
            changeInWeight = hiddenNodesArr[j].outputValue * LR  * Sh
            outputLayerWeights[jk] = outputLayerWeights[jk] + changeInWeight
            jk = jk+1
            
    #------* Hidden Layer Back propogation *-------#
            
    jk = 0
    Sk = 0
    ij = 0
    for i in range(len(hiddenNodesArr)):
        Ak = 0
        for j in range(len(outputNodesArr)):
            Ak = Ak + (outputNodesArr[j].error * outputLayerWeights[jk])
            jk=jk+1
        Sk = (hiddenNodesArr[i].outputValue * (1-hiddenNodesArr[i].outputValue) * Ak)
        hiddenNodesArr[i].error = Sk
        for k in range(len(testArray)):
            changeInWeight = LR * Sk * testArray[k] 
            hiddenLayerWeights[ij] = hiddenLayerWeights[ij] + changeInWeight
            ij=ij+1
    
    
#---------------* reading from file *------------------#
#opens files for reading
f = open('/Users/michaelowen/VSCode_Files/neuralNetwork/dataPackets/learningData.txt','r')
Validate = open('/Users/michaelowen/VSCode_Files/neuralNetwork/dataPackets/learningData.txt','r') 
#reads line from file as list
x = f.read().splitlines()
y = Validate.read().splitlines()

testDataArray = []
validationArrayData = []
IDontTrustLetters = 0
#splits long list into 2D array for easy shuffle and usage
while IDontTrustLetters < (len(x)):
    testArray = [int(i) for i in str(x[IDontTrustLetters])]
    IDontTrustLetters = IDontTrustLetters+1
    expectedOutput = [int(i) for i in str(x[IDontTrustLetters])]
    IDontTrustLetters = IDontTrustLetters+1
    testDataArray.append([testArray,expectedOutput])
Pm = 0
while Pm < (len(y)):
    validationArray1 = [int(i) for i in str(y[Pm])]
    Pm = Pm+1
    validationArray2 = [int(i) for i in str(y[Pm])]
    Pm = Pm+1
    validationArrayData.append([validationArray1,validationArray2])
f.close()
Validate.close()

#-------------* creating nodes *-----------#
hiddenNodesArr = []
hiddenNodesAMT = 17
for i in range(hiddenNodesAMT):
    newNode = hiddenNode(None,None,None)
    hiddenNodesArr.append(newNode)

outputNodesArr = []
outputNodesAmt = 10
for i in range(outputNodesAmt):
    newNode = outputNode(None,None,None)
    outputNodesArr.append(newNode)

#-------------* Random weights *--------------#
hiddenLayerWeights = []
for i in range(17 * hiddenNodesAMT):
    hiddenLayerWeights.append(random.uniform(-.5,.5))
outputLayerWeights = []
for i in range(10 * hiddenNodesAMT):
    outputLayerWeights.append(random.uniform(-.5,.5))
#validationArrayData - validation data
#testDataArray   - learning data
    
#------------------------------------------* LR  & Iterations  *----------
ierations = 7000
LR = .07
for i in range(ierations):
    UV = 0
    random.shuffle(testDataArray)
    random.shuffle(testDataArray)
    if(i % 500 == 0):
        print("iterations: ",i)
        #print("hiddenLayerWeights: ",hiddenLayerWeights)
        #print("outputLayer: ", outputLayerWeights)
        print("Hiddenerror ", hiddenNodesArr[4].error)
        print("outputError ", outputNodesArr[4].error)
        
    while(UV < len(testDataArray)):   #will run 26 times, one for each data
        testData = testDataArray[UV][0]
        validationData = testDataArray[UV][1]
        forwardPropogation(hiddenLayerWeights,outputLayerWeights,hiddenNodesArr,outputNodesArr,testData)
        backPropogation(hiddenLayerWeights,outputLayerWeights,hiddenNodesArr,outputNodesArr,testData,validationData,LR)
        UV = UV +1

#loop through validation data
VU = 0
count = 0 
while VU < len(validationArrayData):
    possibleValues = []
    newTestData = validationArrayData[VU][0]
    testForData = validationArrayData[VU][1]
    forwardPropogation(hiddenLayerWeights, outputLayerWeights, hiddenNodesArr, outputNodesArr, newTestData)

    correctIndex = -1
    greatestOutput = -1
    for i in range(len(outputNodesArr)):
        print("outputValue: ", outputNodesArr[i].outputValue)
        if testForData[i] == 1:
            correctIndex = i
        if outputNodesArr[i].outputValue > greatestOutput:
            greatestOutput = outputNodesArr[i].outputValue
            greatestIndex = i

    print("Predicted index with the highest output value:", greatestIndex)
    print("Expected index where the output is 1:", correctIndex)

    if greatestIndex == correctIndex:
        count += 1

    print("value to test for: ", validationArrayData[VU][1])
    VU += 1

print("final accuracy:", count, "/ 26")

