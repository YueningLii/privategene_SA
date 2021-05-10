#import dataset
import pandas as pd
roary=pd.read_csv("/Users/yueningli/gene_presence_absence_roary.csv",low_memory=False)

#create dictionary for lineages and count the number of isolates in each lineages
with open("/Users/yueningli/PopPUNK/gpsc16_alt_dis/gpsc16_lineages/gpsc16_select_lineages.txt","r") as f:
     dic16 = dict([line.split() for line in f])

#count the number of ids in each lineage
count = 0
lineage = "1" #change
for x in dic16:
    if dic16[x] == lineage:
        count += 1

# split the dataset to lineages, here is gpsc16 only
roary.rename(columns=dic16,inplace=True)

 #check whether the column is empty,if its empty then gene is not present in this ID
 #counting gene frequency for lineage 1
gpsc16 = roary[["Gene",lineage]] #lineage 1
empty=gpsc16.apply(lambda x: x.isnull().sum(), axis='columns')
empty = empty.tolist()#convert to list
empty[:] = [((count-x) / count) for x in empty]#get percentage
gene = list(gpsc16["Gene"])# gene list

#create a dictionary
dic16_1 = {gene[i]: empty[i] for i in range(len(gene))}

##gene frequency for lineage 2###################################################
count = 0
lineage = '2' #change
for x in dic16:
    if dic16[x] == lineage:
        count += 1
 #counting gene frequency
gpsc16 = roary[["Gene",lineage]] #lineage
empty=gpsc16.apply(lambda x: x.isnull().sum(), axis='columns')
empty = empty.tolist()#convert to list
empty[:] = [((count-x) / count) for x in empty]#get percentage
gene = list(gpsc16["Gene"])# gene list
#create a dictionary
dic16_2 = {gene[i]: empty[i] for i in range(len(gene))}


##gene frequency for lineage 3##############################
count = 0
lineage = '3' #change
for x in dic16:
    if dic16[x] == lineage:
        count += 1
 #counting gene frequency
gpsc16 = roary[["Gene",lineage]] #lineage
empty=gpsc16.apply(lambda x: x.isnull().sum(), axis='columns')
empty = empty.tolist()#convert to list
empty[:] = [((count-x) / count) for x in empty]#get percentage
gene = list(gpsc16["Gene"])# gene list
#create a dictionary
dic16_3 = {gene[i]: empty[i] for i in range(len(gene))}

###gene frequency for lineage 4 ##############################
count = 0
lineage = '4' #change
for x in dic16:
    if dic16[x] == lineage:
        count += 1
 #counting gene frequency
gpsc16 = roary[["Gene",lineage]] #lineage
empty=gpsc16.apply(lambda x: x.isnull().sum(), axis='columns')
empty = empty.tolist()#convert to list
empty[:] = [((count-x) / count) for x in empty]#get percentage
gene = list(gpsc16["Gene"])# gene list
#create a dictionary
dic16_4 = {gene[i]: empty[i] for i in range(len(gene))}

######5###############################################
count = 0
lineage = '5' #change
for x in dic16:
    if dic16[x] == lineage:
        count += 1
 #counting gene frequency
gpsc16 = roary[["Gene",lineage]] #lineage
empty=gpsc16.apply(lambda x: x.isnull().sum(), axis='columns')
empty = empty.tolist()#convert to list
empty[:] = [((count-x) / count) for x in empty]#get percentage
gene = list(gpsc16["Gene"])# gene list
#create a dictionary
dic16_5 = {gene[i]: empty[i] for i in range(len(gene))}

#########6############################################
count = 0
lineage = '6' #change
for x in dic16:
    if dic16[x] == lineage:
        count += 1
 #counting gene frequency
gpsc16 = roary[["Gene",lineage]] #lineage
empty=gpsc16.apply(lambda x: x.isnull().sum(), axis='columns')
empty = empty.tolist()#convert to list
empty[:] = [((count-x) / count) for x in empty]#get percentage
gene = list(gpsc16["Gene"])# gene list
#create a dictionary
dic16_6 = {gene[i]: empty[i] for i in range(len(gene))}

##########7###########################################
count = 0
lineage = '7' #change
for x in dic16:
    if dic16[x] == lineage:
        count += 1
 #counting gene frequency
gpsc16 = roary[["Gene",lineage]] #lineage
empty=gpsc16.apply(lambda x: x.isnull().sum(), axis='columns')
empty = empty.tolist()#convert to list
empty[:] = [((count-x) / count) for x in empty]#get percentage
gene = list(gpsc16["Gene"])# gene list
#create a dictionary
dic16_7 = {gene[i]: empty[i] for i in range(len(gene))}
###########8##########################################
count = 0
lineage = '8' #change
for x in dic16:
    if dic16[x] == lineage:
        count += 1
 #counting gene frequency
gpsc16 = roary[["Gene",lineage]] #lineage
empty=gpsc16.apply(lambda x: x.isnull().sum(), axis='columns')
empty = empty.tolist()#convert to list
empty[:] = [((count-x) / count) for x in empty]#get percentage
gene = list(gpsc16["Gene"])# gene list
#create a dictionary
dic16_8 = {gene[i]: empty[i] for i in range(len(gene))}

##########9###########################################
count = 0
lineage = '9' #change
for x in dic16:
    if dic16[x] == lineage:
        count += 1
 #counting gene frequency
gpsc16 = roary[["Gene",lineage]] #lineage
empty=gpsc16.apply(lambda x: x.isnull().sum(), axis='columns')
empty = empty.tolist()#convert to list
empty[:] = [((count-x) / count) for x in empty]#get percentage
gene = list(gpsc16["Gene"])# gene list
dic16_9 = {gene[i]: empty[i] for i in range(len(gene))} #create dictionary

#########10############################################
count = 0
lineage = '10' #change
for x in dic16:
    if dic16[x] == lineage:
        count += 1
 #counting gene frequency
gpsc16 = roary[["Gene",lineage]] #lineage
empty=gpsc16.apply(lambda x: x.isnull().sum(), axis='columns')
empty = empty.tolist()#convert to list
empty[:] = [((count-x) / count) for x in empty]#get percentage
gene = list(gpsc16["Gene"])# gene list
#create a dictionary
dic16_10 = {gene[i]: empty[i] for i in range(len(gene))}

#####################################################
count = 0
lineage = '11' #change
for x in dic16:
    if dic16[x] == lineage:
        count += 1
 #counting gene frequency
gpsc16 = roary[["Gene",lineage]] #lineage
empty=gpsc16.apply(lambda x: x.isnull().sum(), axis='columns')
empty = empty.tolist()#convert to list
empty[:] = [((count-x) / count) for x in empty]#get percentage
gene = list(gpsc16["Gene"])# gene list
#create a dictionary
dic16_11 = {gene[i]: empty[i] for i in range(len(gene))}

#####################################################
count = 0
lineage = '12' #change
for x in dic16:
    if dic16[x] == lineage:
        count += 1
 #counting gene frequency
gpsc16 = roary[["Gene",lineage]] #lineage
empty=gpsc16.apply(lambda x: x.isnull().sum(), axis='columns')
empty = empty.tolist()#convert to list
empty[:] = [((count-x) / count) for x in empty]#get percentage
gene = list(gpsc16["Gene"])# gene list
#create a dictionary
dic16_12 = {gene[i]: empty[i] for i in range(len(gene))}

#####################################################
count = 0
lineage = '13' #change
for x in dic16:
    if dic16[x] == lineage:
        count += 1
 #counting gene frequency
gpsc16 = roary[["Gene",lineage]] #lineage
empty=gpsc16.apply(lambda x: x.isnull().sum(), axis='columns')
empty = empty.tolist()#convert to list
empty[:] = [((count-x) / count) for x in empty]#get percentage
gene = list(gpsc16["Gene"])# gene list
#create a dictionary
dic16_13 = {gene[i]: empty[i] for i in range(len(gene))}

#####################################################
count = 0
lineage = '14' #change
for x in dic16:
    if dic16[x] == lineage:
        count += 1
 #counting gene frequency
gpsc16 = roary[["Gene",lineage]] #lineage
empty=gpsc16.apply(lambda x: x.isnull().sum(), axis='columns')
empty = empty.tolist()#convert to list
empty[:] = [((count-x) / count) for x in empty]#get percentage
gene = list(gpsc16["Gene"])# gene list
#create a dictionary
dic16_14 = {gene[i]: empty[i] for i in range(len(gene))}

#####################################################
count = 0
lineage = '15' #change
for x in dic16:
    if dic16[x] == lineage:
        count += 1
 #counting gene frequency
gpsc16 = roary[["Gene",lineage]] #lineage
empty=gpsc16.apply(lambda x: x.isnull().sum(), axis='columns')
empty = empty.tolist()#convert to list
empty[:] = [((count-x) / count) for x in empty]#get percentage
gene = list(gpsc16["Gene"])# gene list
#create a dictionary
dic16_15 = {gene[i]: empty[i] for i in range(len(gene))}

#####################################################
count = 0
lineage = '16' #change
for x in dic16:
    if dic16[x] == lineage:
        count += 1
 #counting gene frequency
gpsc16 = roary[["Gene",lineage]] #lineage
empty=gpsc16.apply(lambda x: x.isnull().sum(), axis='columns')
empty = empty.tolist()#convert to list
empty[:] = [((count-x) / count) for x in empty]#get percentage
gene = list(gpsc16["Gene"])# gene list
#create a dictionary
dic16_16 = {gene[i]: empty[i] for i in range(len(gene))}

