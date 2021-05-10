

def this_lineage(refdic,infdic,threshold):   # select genes within a linage with frequency above threshld
    for key in list(refdic.keys()):
        if refdic[key] >= threshold:
           infdic[key]= refdic[key]
    return infdic
def unique_this_lineage(refdic,infdic,threshold):   # select gene also below (1-threshold) in other lineage
    for key in list(refdic.keys()):  # select the 95% in lineage 4
        if (refdic[key] >= (1 - threshold) and key in list(infdic.keys())):
            del infdic[key]
    return infdic
threshold=0.90
########lineage 2,gpsc 14
test2={}
test2=this_lineage(dic14_2,test2,threshold)
test2=unique_this_lineage(dic16_4,test2,threshold)
test2=unique_this_lineage(dic14_1,test2,threshold)
test2=unique_this_lineage(dic14_3,test2,threshold)


#######lineage3, gpsc 14
test3={}
test3=this_lineage(dic14_3,test3,threshold)
test3=unique_this_lineage(dic16_4,test3,threshold)
test3=unique_this_lineage(dic14_1,test3,threshold)
test3=unique_this_lineage(dic14_2,test3,threshold)

############lineage 4 gpsc 16
test={}
test=this_lineage(dic16_4,test,threshold)
test=unique_this_lineage(dic14_1,test,threshold)
test=unique_this_lineage(dic14_2,test,threshold)
test=unique_this_lineage(dic14_3,test,threshold)


#########linegae 2 gpsc 14#####################
test1={}
test1=this_lineage(dic14_2,test1,threshold)
test1=unique_this_lineage(dic16_4,test1,threshold)
test1=unique_this_lineage(dic14_1,test1,threshold)
test1=unique_this_lineage(dic14_3,test1,threshold)





