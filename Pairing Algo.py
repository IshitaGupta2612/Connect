from pulp import *
import numpy as np 
import pandas as pd  
from scipy.stats import rankdata

print("\n------ Fetching/Reading The Data From The Data Set")
mentor = pd.read_csv('MentorDataframe.csv')
mentee = pd.read_csv('MenteeDataframe.csv')
print(mentor.head()) 
print(mentee.head()) 

mentorFields=[]

mentorFields.append(mentor["AD"])
mentorFields.append(mentor["AI"])
mentorFields.append(mentor["coding"])
mentorFields.append(mentor["CS"])
mentorFields.append(mentor["CyS"])
mentorFields.append(mentor["DS"])
mentorFields.append(mentor["IT"])
mentorFields.append(mentor["IOS"])
mentorFields.append(mentor["robotics"])
mentorFields.append(mentor["SE"])
mentorFields.append(mentor["UI"])
mentorFields.append(mentor["WD"])

#mentorFields[7]

menteeFields=[]

menteeFields.append(mentee["AD2"])
menteeFields.append(mentee["AI2"])
menteeFields.append(mentee["coding2"])
menteeFields.append(mentee["CS2"])
menteeFields.append(mentee["CyS2"])
menteeFields.append(mentee["DS2"])
menteeFields.append(mentee["IT2"])
menteeFields.append(mentee["IOS2"])
menteeFields.append(mentee["robotics2"])
menteeFields.append(mentee["SE2"])
menteeFields.append(mentee["UI2"])
menteeFields.append(mentee["WD2"])
#menteeFields[7]

MatchFields=[]
for m in range (len(menteeFields)):
    Menteerows, Mentorcols = (len(menteeFields[m]),len(mentorFields[m]))
    arr=[]
    for i in range(Menteerows):
        col = []
        for j in range(Mentorcols):
            if (menteeFields[m][i]==mentorFields[m][j] and menteeFields[m][i] !=0 and menteeFields[m][i] !='0' and mentorFields[m][j] !=0 and mentorFields[m][j] !='0'):
                col.append(1)
            else :
                col.append(0)
        arr.append(col)
    MatchFields.append(arr)
    print("\n",arr)
print("\n******************\n",MatchFields)
# rows=no of fields
#columns=No of mentees
# columns in the sub-array =no of mentors

#creating a 2D array
'''Menteerows, Mentorcols = (len(menteeFields[9]),len(mentorFields[9]))
arr=[]
for i in range(Menteerows):
    col = []
    for j in range(Mentorcols):
        if (menteeFields[9][i]==mentorFields[9][j] and menteeFields[9][i] !='0' and mentorFields[9][j] !='0'):
            col.append(1)
        else :
            col.append(0)
    arr.append(col)
print("\n",arr)'''
# rows=no of mentees
#columns=No of mentors

# importing library
arr = np.array(MatchFields)
column_sums = arr.sum(axis=0)
#column_sums

timezone= [
['GMT',0],
['UTC',0],
['ECT',1],
['EET',2],
['ART',2],
['EAT',3],
['MET',3.5],
['NET',4],
['PLT',5],
['IST',5.5],
['BST',6],
['VST',7],
['CTT',8],
['JST',9],
['ACT',9.5],
['AET',10],
['SST',11],
['NST',12],
['MIT',-11],
['HST',-10],
['AST',-9],
['PST',-8],
['PNT',-7],
['MST',-7],
['CST',-6],
['EST',-5],
['IET',-5],
['PRT',-4],
['CNT',-3.5],
['AGT',-3],
['BET',-3],
['CAT',-1]]

mentorTimezone=list(mentor['dropdownMenuButton'])
menteeTimezone=list(mentee['dropdownMenuButton2'])
mentorTimezone
menteeTimezone


aTime=[]
bTime=[]
for i in range(len(mentorTimezone)):
    for t in range(len(timezone)):
        if (timezone[t][0]==mentorTimezone[i]):
            aTime.append(timezone[t][1])

for i in range(len(menteeTimezone)):
    for t in range(len(timezone)):
        if (timezone[t][0]==menteeTimezone[i]):
            bTime.append(timezone[t][1])

#print('aTime',aTime)
#print('bTime',bTime)

#creating a 2D array
rows, cols = (len(bTime), len(aTime))
arr=[]
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(abs(aTime[j]-bTime[i]))
    arr.append(col)
#print("\n",arr)
# Ranking of array in reverse order
timeRank=[]

for i in range (len(arr)) :
    timeRank.append(rankdata(arr[i], method='dense'))
#print(timeRank) #Ranked 2D array'''

timeRank2=[]
for i in range (len(timeRank)) :
    timeRank2.append(max(timeRank[i]) - rankdata(arr[i], method='dense')+1)
timeRank2=np.array(timeRank2)
print(timeRank2) #Reveresed 2D Ranked array'''

mentorHour=mentor['Availability']
menteeHour=mentee['Availability2']

#creating a 2D array
rows, cols = (len(menteeHour), len(mentorHour))
arr=[]
for i in range(rows):
    col = []
    for j in range(cols):
        col.append(abs(mentorHour[j]-menteeHour[i]))
    arr.append(col)
#print("\n",arr)
# Ranking of array in reverse order
hourRank=[]

for i in range (len(arr)) :
    hourRank.append(rankdata(arr[i], method='dense'))
#print(hourRank) #Ranked 2D array'''
hourRank2=[]
for i in range (len(hourRank)) :
    hourRank2.append(max(hourRank[i]) - rankdata(arr[i], method='dense')+1)
hourRank2=np.array(hourRank2)
print(hourRank2) #Reveresed 2D Ranked array'''


# In[65]:


finalRankedArray=[]
finalRankedArray.append(column_sums)
finalRankedArray.append(timeRank2)
finalRankedArray.append(hourRank2)
finalRankedArray=np.array(finalRankedArray)
print(finalRankedArray)

finalRankedArray=finalRankedArray.sum(axis=0)
print(finalRankedArray)

#The Pairing Algo :

c = finalRankedArray
MenteeNames =mentee['email2']
MentorNames =mentor['email']

#Creating a Data Frame
match_info = pd.DataFrame(c, index=MenteeNames, columns=MentorNames)

print(match_info)

MenteeNames =mentee['email2']
MentorNames =mentor['email']
MentorIndex=[]
for i in range (len(finalRankedArray)):
    maximum=max(finalRankedArray[i])
    for j in range (len(finalRankedArray[0])):
        if maximum==finalRankedArray[i][j]:
            MentorIndex.append(j)

print(MentorIndex)

for i in range (len(finalRankedArray)):
    maximum=max(finalRankedArray[i])
    for j in range (len(finalRankedArray[0])):
        if j==MentorIndex[i]:
            print('{} and {} with Total score: {}'.format(MenteeNames[i],MentorNames[j],finalRankedArray[i][j]))

