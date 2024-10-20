
class initializeData:
    #outputs a 2d array [example to learn][expected output]; takes a string file name such as fileName.txt
    def getLearningData(learnFileName):
        #open and split data in file into lines to be read  
        learningDataFile = open('/Users/michaelowen/VSCode_Files/neuralnetorkBP/dataPackets/learningData.txt','r')
        learnDataLine = learningDataFile.read().splitlines()
        
        learningDataArr = []        #final array to be populated
        pointer = 0             #pointer to which line is being read

        #loop through files and transfer values to 2dArray
        while pointer < (len(learnDataLine)):
            testData = [int(i) for i in str(learnDataLine[pointer])]
            pointer = pointer+1
            expectedOutput = [int(i) for i in str(learnDataLine[pointer])]
            pointer = pointer+1
            learningDataArr.append([testData,expectedOutput])
        learningDataFile.close()
        return learningDataArr

    #outputs a 2d array [example to learn][expected output]; takes a string file name such as fileName.txt
    def getValidateData(ValidateFileName):
        #open and split data in file into lines to be read   
        ValidationDataFile = open('/Users/michaelowen/VSCode_Files/neuralnetorkBP/dataPackets/validationData.txt','r')
        validateDataLine = ValidationDataFile.read().splitlines()
        
        validateDataArr = []    #final array to be populated
        pointer = 0     #pointer to which line is being read

        # loop through each line in the file and transferring it to an in array ex: [0,0,1,0,1,0,1,1,0,1,1,1,0,0,0]
        while pointer < (len(validateDataLine)):
            testData = [int(i) for i in str(validateDataLine[pointer])]
            pointer = pointer + 1
            expectedOutput = [int(i) for i in str(validateDataLine[pointer])]
            pointer = pointer + 1
            validateDataArr.append([testData,expectedOutput])
        ValidationDataFile.close()
        return validateDataArr