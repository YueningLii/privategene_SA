#import lineage information
with open("/Users/yueningli/PopPUNK/gpsc14_alt_dis/gpsc14_lineages/gpsc14_select_lineages.txt", "r") as f:
    dic14 = dict([line.split() for line in f])
count = 0
lineage = "1" #change
for x in dic14:
    if dic14[x] == lineage:
        count += 1
#import gene data
import pandas as pd
roary=pd.read_csv("/Users/yueningli/gene_presence_absence_roary.csv",low_memory=False)
roary = roary.drop(roary.columns[1:14],axis=1)
roary.rename(columns=dic14,inplace=True)

#counting gene frequency for lineage 1
gpsc14 = roary[["Gene",lineage]] #lineage 1
empty=gpsc14.apply(lambda x: x.isnull().sum(), axis='columns')
empty = empty.tolist()#convert to list
empty[:] = [((count-x) / count) for x in empty]#get percentage
gene = list(gpsc14["Gene"])# gene list
dic14_1 = {gene[i]: empty[i] for i in range(len(gene))}


#counting gene frequency for lineage 2
count = 0
lineage = '2' #change
for x in dic14:
    if dic14[x] == lineage:
        count += 1
 #counting gene frequency
gpsc14 = roary[["Gene",lineage]] #lineage
empty=gpsc14.apply(lambda x: x.isnull().sum(), axis='columns')
empty = empty.tolist()#convert to list
empty[:] = [((count-x) / count) for x in empty]#get percentage
gene = list(gpsc14["Gene"])# gene list
dic14_2 = {gene[i]: empty[i] for i in range(len(gene))}


#####################################################
count = 0
lineage = '3' #change
for x in dic14:
    if dic14[x] == lineage:
        count += 1
 #counting gene frequency
gpsc14 = roary[["Gene",lineage]] #lineage
empty=gpsc14.apply(lambda x: x.isnull().sum(), axis='columns')
empty = empty.tolist()#convert to list
empty[:] = [((count-x) / count) for x in empty]#get percentage
gene = list(gpsc14["Gene"])# gene list
#create a dictionary
dic14_3 = {gene[i]: empty[i] for i in range(len(gene))}

#####################################################
count = 0
lineage = '4' #change
for x in dic14:
    if dic14[x] == lineage:
        count += 1
 #counting gene frequency
gpsc14 = roary[["Gene",lineage]] #lineage
empty=gpsc14.apply(lambda x: x.isnull().sum(), axis='columns')
empty = empty.tolist()#convert to list
empty[:] = [((count-x) / count) for x in empty]#get percentage
gene = list(gpsc14["Gene"])# gene list
#create a dictionary
dic14_4 = {gene[i]: empty[i] for i in range(len(gene))}

#####################################################
count = 0
lineage = '5' #change
for x in dic14:
    if dic14[x] == lineage:
        count += 1
 #counting gene frequency
gpsc14 = roary[["Gene",lineage]] #lineage
empty=gpsc14.apply(lambda x: x.isnull().sum(), axis='columns')
empty = empty.tolist()#convert to list
empty[:] = [((count-x) / count) for x in empty]#get percentage
gene = list(gpsc14["Gene"])# gene list
#create a dictionary
dic14_5 = {gene[i]: empty[i] for i in range(len(gene))}


