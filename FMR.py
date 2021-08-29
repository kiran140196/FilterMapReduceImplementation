#Function to accept data
def AcceptData():
    arr=[]
    print("Enter how many elements you want to enter")
    iSize=int(input())

    for iCnt in range(iSize):
        print("Enter the element",iCnt+1)
        iEle=int(input())
        arr.append(iEle)
    return arr

#Function to check if no is even
def CheckEven(iNo):
	if iNo % 2 == 0 :
		return True
	else:
		return False

#Implementaion of Filter
def FilterClone(inputData):
	filterData=[]
	for iCnt in range(len(inputData)):
		if CheckEven(inputData[iCnt]) == True:
			filterData.append(inputData[iCnt])
	return filterData

#Implementaion of map
def MapClone(Filterlist):
	mapData=[]
	for iCnt in range(len(Filterlist)):
		iNewEle=Filterlist[iCnt]+2
		mapData.append(iNewEle)
	return mapData

#Implementaion of reduce
def ReduceClone(Maplist):
	iSum=0
	for iCnt in range(len(Maplist)):
		iSum=iSum+Maplist[iCnt]
	return iSum

#Entry point function
def main():
    UserEnteredData=[]
    UserEnteredData=AcceptData()
    print("Your entered data is",UserEnteredData)

    newFilterData=FilterClone(UserEnteredData)
    print("Filtered data is",newFilterData)

    newMapData=MapClone(newFilterData)
    print("Map data is",newMapData)
    
    reduceData=ReduceClone(newMapData)
    print("Reduce data is",reduceData)

if __name__=="__main__":
	main()