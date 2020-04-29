library("tidyverse")
library("ggplot2")
library("dplyr")
library("lubridate")

setwd("C:\\Users\\snuñez\\Documents\\SJNM_ZE\\Cursos\\Data_analysis\\Proyecto_final\\Proyecto_Energia_BEDU\\Unir_CSV_y_eliminar_repetidos_SNM")

A1<-read.csv("dataexport_20200421T165419_Nueva_Baja_California__Baja_California.csv",skip=9,header=T)
A2<-read.csv("dataexport_20200423T222953_Nueva_Baja_California__Baja_California.csv",skip=9,header=T)
#A3
#A4
#A5
#A6
####ETC

B1 <- rbind(A1,A2)

#B2 <- rbind(A3,A4)
#B3 <- rbind(A5,A6)
#B4 <- rbind(Jul,Aug)
#B5 <- rbind(Sep,Oct)
#B6 <- rbind(Nov,Dec)
####ETC


#C1 <- rbind(B1,B2)
#C2 <- rbind(B3,B4)
#C3 <- rbind(B5,B6)

#DY <- rbind(C1,C2)
#DY <- rbind(CY,C3)

#All <- rbind(D1,D2) esto en cao de tener todos 

All <- B1

Final <- unique(All)

Final$timestamp<- strsplit(as.character(Final$timestamp),'T')

Final$timestamp =parse_date_time(Final$timestamp,"ymd HM")
 


