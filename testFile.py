def get_csv_filenames():
    import glob
    superList = glob.glob("*.csv")
    filterList = list(filter(lambda x: x!="everyone.csv",superList))
    filter2List = list(filter(lambda x: x!="mlp6.csv",filterList))
    return filter2List



def checkSpaces(teamName):
        if " " in teamName:
            print("space found")

def getUniqueNames(allTeamNames):
    allTeamNamesSet = set(allTeamNames)
    uniqueTeamNames = list(allTeamNamesSet)
    filterNames1 = list(filter(lambda x: x!="none",uniqueTeamNames))
    filterNames2 = list(filter(lambda x: x!="None",filterNames1))
    return filterNames2

def checkCamelCase(uniqueSet):

    counter = 0
    counter2 = 0
    for i in range(len(uniqueSet)):
        holdVal = uniqueSet[i]
        if holdVal.isupper() == False and holdVal.islower() == False:
            counter2 = 0
            for i2 in range(len(holdVal)):

                if holdVal[i2].isupper() == True:
                    counter2 = counter2 + 1
            if counter2 >= 2:
                print("is camel case")
                counter = counter + 1
    print(counter)
    return(counter)

def convertCSVtoJSON(pdDataFrame,JSONfileName):
    import pandas as pd
    import json

    str2 = ".json"
    str3 = JSONfileName + str2
    jsonFile = pdDataFrame.to_json()
    with open(str3,'w') as f:
        json.dump(jsonFile,f)

def read_csv(passed_List):
    import pandas as pd

    framesList = []
    teamNamesList = []
    for i in range(len(passed_List)):
        fileNameJSON = passed_List[i]
        df = pd.read_csv(passed_List[i],header=None)
        convertCSVtoJSON(df,fileNameJSON)
        dfArray = df.values
        dfAnalyze = pd.DataFrame(dfArray,index = list('a'),columns=list('ABCDE'))
        oneTeamsName = str(dfAnalyze.loc['a','E'])
        oneTeamsName = oneTeamsName.strip()
        teamNamesList.append(oneTeamsName)
        checkSpaces(oneTeamsName)
        framesList.append(dfAnalyze)

    finalDf = pd.concat(framesList)
    finalDf.to_csv("everyone.csv",index=False,header=None)


    checkCamelCase(getUniqueNames(teamNamesList))



def main():

    get_csv_filenames()
    read_csv(get_csv_filenames())

main()
