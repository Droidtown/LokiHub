library(tidyverse)
library(tidytext)
library(quanteda)
library(stringr)
library(jiebaR)
library(readtext)
library(readxl)
library(data.table)


person1<-read_excel("response_ch.xlsx", 1, col_names = FALSE)%>%
  mutate(index = "1")%>%
  rename("sent1"="...1",
         "ENG"="...2",
         "sent2"="...3",
         "CHIN"="...4")

person2<-read_excel("response_ch.xlsx", 2, col_names = FALSE)%>%
  mutate(index = "2")%>%
  rename("sent1"="...1",
         "ENG"="...2",
         "sent2"="...3",
         "CHIN"="...4")
person3<-read_excel("response_ch.xlsx", 3, col_names = FALSE)%>%
  mutate(index = "3")%>%
  rename("sent1"="...1",
         "ENG"="...2",
         "sent2"="...3",
         "CHIN"="...4")

REA_EXCEL<- function(x, i){
  read_excel(x, i, col_names = FALSE)%>%
    mutate(index = i)%>%
    rename("sent1"="...1",
           "ENG"="...2",
           "sent2"="...3",
           "CHIN"="...4")
}

REA_EXCEL("response_ch.xlsx", 1)

REA_EXCEL("response_ch.xlsx", 2)

personAll <- data.frame()
for (i in c(1:21)){
  person_i = REA_EXCEL("response_ch.xlsx", i)
  personAll = rbind(person_i, personAll)
  
}
personAll%>%
  group_by(index)%>%
  count(ENG)%>%
  write.csv("ENG_count.csv")

personAll%>%
  group_by(index)%>%
  count(CHIN)%>%
  write.csv("CHIN_count.csv")
