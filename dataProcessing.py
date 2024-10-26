
class initializeData:
    #outputs a 2d array [example to learn][expected output]; takes a string file name such as fileName.txt
    def getLearningData(learn_file_name):
        #open and split data in file into lines to be read  
        learning_data_file = open('/Users/michaelowen/VSCode_Files/neuralnetorkBP/dataPackets/learningData.txt','r')
        learn_data_line = learning_data_file.read().splitlines()
        
        learning_data_arr = []        #final array to be populated
        pointer = 0             #pointer to which line is being read

        #loop through files and transfer values to 2dArray
        while pointer < (len(learn_data_line)):
            test_data = [int(i) for i in str(learn_data_line[pointer])]
            pointer = pointer+1
            expected_output = [int(i) for i in str(learn_data_line[pointer])]
            pointer = pointer+1
            learning_data_arr.append([test_data,expected_output])
        learning_data_file.close()
        return learning_data_arr

    #outputs a 2d array [example to learn][expected output]; takes a string file name such as fileName.txt
    def getValidateData(validate_file_name):
        #open and split data in file into lines to be read   
        validation_data_file = open('/Users/michaelowen/VSCode_Files/neuralnetorkBP/dataPackets/validationData.txt','r')
        validate_data_line = validation_data_file.read().splitlines()
        
        validate_data_arr = []    #final array to be populated
        pointer = 0     #pointer to which line is being read

        # loop through each line in the file and transferring it to an in array ex: [0,0,1,0,1,0,1,1,0,1,1,1,0,0,0]
        while pointer < (len(validate_data_line)):
            test_data = [int(i) for i in str(validate_data_line[pointer])]
            pointer = pointer + 1
            expected_output = [int(i) for i in str(validate_data_line[pointer])]
            pointer = pointer + 1
            validate_data_arr.append([test_data,expected_output])
        validation_data_file.close()
        return validate_data_arr