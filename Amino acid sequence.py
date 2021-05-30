import pandas as pd
import numpy as np
roary=pd.read_csv("/Users/yueningli/gene_presence_absence_roary.csv",low_memory=False)
reader=pd.read_csv("/Users/yueningli/gene_data.csv",low_memory=False)

##subset roary for only gene names and annotation ids
roary = roary.drop(roary.columns[1:14],axis=1)
#import common gene list (should be based on previous result, but save seperately)
pri = pd.read_csv("/Users/yueningli/private_gene_list .csv")#read the data frame
list_pri=pri['Gene'].tolist()#convert to list
roary=roary[roary['Gene'].isin(list_pri)]# subset the dara frame

#####subset reader(gene_data.csv )
reader = reader[["annotation_id","prot_sequence"]]
ref=roary.set_index("Gene").T.to_dict('list') #convert to dictionary

newref = {}
for key, value in ref.items():
    for string in value:
       newref.setdefault(string, []).append(key)  #revert the dictionary

del newref[np.nan]   #remove na

d1=list(newref.keys())
reader=reader[reader['annotation_id'].isin(d1)]

#replace dict values
reader=reader.replace({"annotation_id":newref})

#group by and mutate
reader["prot_length"] = reader["prot_sequence"].str.len()
seq=reader.groupby("annotation_id",as_index=False)["prot_length"].median()
seq_new = pd.merge(seq, reader[['annotation_id', 'prot_length','prot_sequence']], how="left", left_on=['annotation_id', 'prot_length'], right_on=['annotation_id', 'prot_length']);
seq_new =seq_new.groupby("annotation_id",as_index=False).first()

