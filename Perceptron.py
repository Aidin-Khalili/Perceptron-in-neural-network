list = [[]]
patternList = [[]]
separator = '\t'
#Function to convert string to float (it had used for file entry)
def cnv_string2float(list):
    patternList=list
    for i in range(len(list)): 
        for j in range(len(list[i])): 
            patternList[i][j] = float(list[i][j]) 
    return patternList
#Class for read from file & out the resualt(input part of program)
class File_entry:
    fileAddress=''
    def __init__(self, fileAddress):
        self.fileAddress = fileAddress
    def read_file(self):
        f = open(self.fileAddress, "r")
        for line in f:
            list.append((line.replace("\n", "")).split(separator))
        f.close()
        patternList=cnv_string2float(list[1:])
        return patternList
    def get_pattern(self): return list
#Main part
if __name__ == '__main__':
    read = File_entry('H:\\Input.txt')
    patternList=read.read_file()
    num_weights=len(patternList[0])-1
    weight=[0]*num_weights
    b_weight=0
    alfa=1
    teta=0.2
    cnt_epoch=0
    change_flag=False
    while(cnt_epoch<1000):
        cnt_epoch+=1
        for i in range(0,len(patternList)):
            yi_n=b_weight
            for j in range(0,num_weights):
                yi_n+=weight[j]*patternList[i][j]
            if(yi_n>teta):
                y=1
            elif((-teta<=yi_n) & (teta>yi_n)):
                y=0
            else:
                y=-1
            if(patternList[i][num_weights]!=y):
                change_flag=True
                for j in range(0,num_weights):
                    weight[j]+=patternList[i][j]*patternList[i][num_weights]*alfa
                b_weight+=patternList[i][num_weights]*alfa
        if(change_flag==False):
            break
        change_flag=False
    if(cnt_epoch==1000):
        print('It does not have answer in ',cnt_epoch,' epoch.')
    else:
        print('Weghits are : ' , weight,'& b is : ' , b_weight,' in ',cnt_epoch,' epoch')
