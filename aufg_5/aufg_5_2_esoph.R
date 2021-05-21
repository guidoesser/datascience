data()
data("esoph")
esoph
getwd ()
list.files ()
dir ()
head (esoph)
head (esoph, n=10)
class (esoph)
colnames (esoph)
dim (esoph)
length (esoph$agegp)
length (esoph[3,])
str (esoph)
tail (esoph)
summary (esoph)
mean (esoph$ncases)
median (esoph$ncontrols)
mean (esoph$ncases[1:15])
median (esoph[16:30,4])
min (esoph$ncases)
max (esoph[,5])
mean (subset(esoph$ncases, esoph$tobgp == "30+"))
tobgp30_data <- esoph[which(esoph[,"tobgp"] == "30+"),]
tobgp30_noZero <- tobgp30_data[which(tobgp30_data[, "ncases"] > 0 ),]
sum (tobgp30_noZero$ncases)
var (esoph$ncases)
sd (esoph$ncases)^2
sqrt (var (esoph$ncases))
esoph$cat_ncases <- cut (esoph$ncases,3,labels=c("rare","med","freq"))
summary (esoph)
plot (esoph$ncases, esoph$ncontrols)
plot(esoph$ncases, esoph$ncontrols, xlab="Cases", ylab="Controls",
main="Cases vs Controls", pch=15, col="red")
hist(esoph$ncases, xlab="Nr of Cases", main="Esoph data", col="orange")
boxplot (esoph$ncases ~ esoph$agegp,main="Esoph dataset",
border="gray",lwd=1,col=rainbow(5))
par(mfrow=c(3,2))
boxplot (esoph$ncases ~ esoph$agegp, xlab="agegp",border="gray", lwd=1,
col=rainbow(5))
boxplot (esoph$ncontrols ~ esoph$agegp,xlab="agegp", border="gray", lwd=1,
col=rainbow(5))
boxplot (esoph$ncases ~ esoph$alcgp,border="gray",xlab="alcgp", lwd=1,
col=rainbow(4))
boxplot (esoph$ncontrols ~ esoph$alcgp,border="gray", xlab="alcgp", lwd=1,
col=rainbow(4))
boxplot (esoph$ncases ~ esoph$tobgp,border="gray",xlab="tobgp", lwd=1,
col=rainbow(4))
boxplot (esoph$ncontrols ~ esoph$tobgp,border="gray", xlab="tobgp", lwd=1,
col=rainbow(4))
title("Boxplots of Cases (left) and Controls (right)",outer=TRUE, line=-2, cex.main=2)
par (mfrow=c(1,1))
pdf ("esoph_boxplots.pdf", width=7, height=5)
boxplot (esoph$ncases ~ esoph$agegp, main="Cases per Age group",xlab="agegp",
border="gray", lwd=1, col=rainbow(5))
boxplot (esoph$ncontrols ~ esoph$agegp, xlab="agegp",main="Controls per Age group",
border="gray", lwd=1, col=rainbow(5))
boxplot (esoph$ncases ~ esoph$alcgp,border="gray",xlab="alcgp",
main="Cases per Alcohol group",lwd=1, col=rainbow(4))
boxplot (esoph$ncontrols ~ esoph$alcgp,border="gray", xlab="alcgp",
main="Controls per Alcohol group", lwd=1, col=rainbow(4))
boxplot (esoph$ncases ~ esoph$tobgp,border="gray", xlab="tobgp",
main="Cases per Tobacco group", lwd=1, col=rainbow(4))
boxplot (esoph$ncontrols ~ esoph$tobgp,border="gray", xlab="tobgp",
main="Controls per Tobacco group", lwd=1, col=rainbow(4))
dev.off ()

