install.packages('ggplot2')
install.packages('dplyr')
install.packages('reshape')
install.packages('tseries')
install.packages('cowplot')
install.packages('forecast')

library(ggplot2)
library(dplyr)
library(reshape)
library(tseries)
library(cowplot)
library(forecast)


setwd("C:\\Users\\alapa\\Desktop\\Spring2020\\Research Project\\tesla-stock-data-from-2010-to-2020")


stock_data <-  read.table("TSLA.csv", header=T, sep=",")
str(stock_data)
stock_data$Date = as.Date(stock_data$Date)



stock_data  %>%
  select(-Volume) %>%
  melt(id.vars = c("Date")) %>%
  ggplot() +
  geom_point(aes(x = Date, y = value, col = variable),
             alpha =  0.5) +
  geom_line(aes(x = Date, y = value, col = variable, group = variable),
            alpha = 0.8) +
  xlab("Date") + ylab("Stock Price") + 
  labs(col = "Types of Price") + 
  theme_bw() +
  theme(text = element_text(size = 15, face = "bold"),
        legend.position = c(0.2,0.8))



plot(stock_ts)

decomp_glob = decompose(glob_ts)
  plot(as.ts(decomp_glob$seasonal))
plot(as.ts(decomp_glob$trend))
plot(as.ts(decomp_glob$random))
plot(decomp_glob)

es_glob_ts = HoltWinters(glob_ts, beta = FALSE, gamma = FALSE)
plot(es_glob_ts)
tes_fore = forecast(es_glob_ts,h=12)
plot(tes_fore)


layout(1:1)
plot(tes_fore$residuals)
lines(c(0, 14), c(0, 0), col = 'red')




plotForecastErrors = function(forecasterrors,forecasttitle) {
  #Function provided by Avril Coghlan
  forecasterrors = na.omit(forecasterrors)
  # make a histogram of the forecast errors:
  mybinsize = IQR(forecasterrors) / 4
  mysd = sd(forecasterrors)
  mymin = min(forecasterrors) - mysd * 5
  mymax = max(forecasterrors) + mysd * 3
  # generate normally distributed data with mean 0 and standard deviation mysd
  mynorm <- rnorm(10000, mean = 0, sd = mysd)
  mymin2 <- min(mynorm)
  mymax2 <- max(mynorm)
  if (mymin2 < mymin) { mymin <- mymin2 }
  if (mymax2 > mymax) { mymax <- mymax2 }
  # make a red histogram of the forecast errors, with the normally distributed data overlaid:
  mybins <- seq(mymin, mymax, mybinsize)
  hist(forecasterrors, col = "red", freq = FALSE, breaks = mybins, main=forecasttitle)
  # freq=FALSE ensures the area under the histogram = 1
  # generate normally distributed data with mean 0 and standard deviation mysd
  myhist <- hist(mynorm, plot = FALSE, breaks = mybins)
  # plot the normal curve as a blue line on top of the histogram of forecast errors:
  points(myhist$mids, myhist$density, type = "l", col = "blue", lwd = 2)
}

#Assess normality of residuals
plotForecastErrors(tes_fore$residuals,'Assessing Normal Distribution')




