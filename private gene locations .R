#packages 
chooseCRANmirror()
install.packages("BiocManager")
BiocManager::install("ballgown")
install.packages("grid")
library(ballgown)
library(circlize)
library(gridBase)
library(ComplexHeatmap)
library(gridExtra)
library("grid")

#read reference gff
ref<-gffReadGR("4311_3#9.velvet.gff",identifier = "gene_id")
#read gene id data 
geneid<-read.csv("geneid.csv")
names(geneid)[2]<-"ID"


####create data frame 
ID=ref$ID
gene_name=ref@elementMetadata$gene
start=as.numeric(ref@ranges@start)
end=as.numeric(ref@ranges@start + ref@ranges@width + 1)
strand = ifelse(ref@strand == "+",1,0)

ref.df<-data.frame(
  "start" = start,
  "end" = end,
  "strand" = strand,
  "gene_name" = gene_name,
  "ID" = ID
)

#append the private gene list 
#join by id 
ref.df<-dplyr::left_join(ref.df,geneid,by="ID")
not_listed<-dplyr::anti_join(geneid,ref.df,by="ID") # the list of genes which can not be found on this gff

#data transformation,add a column called "private",if gene is present : "1",if not:"0"

vec=ref.df$Gene
n = length(vec)
for(i in 1:n){if(is.na(vec[i])== TRUE){vec[i]= 0}else{vec[i]= 1}}
length(which(vec == 0))
ref.df$private=vec

##sort the start position 
ref.df$start<-sort(ref.df$start)

###making a circos plot 
circos.clear()
plot.new()
circle_size = unit(1, "snpc") # snpc unit gives you a square region
pushViewport(viewport(x = 0,
                      y = 0,
                      width = circle_size,
                      height = circle_size,
                      just = c("center", "top")))
par(new = TRUE)
circos.par("start.degree" = 90, "track.margin" = c(0,0))
circos.genomicInitialize(ref.df)
