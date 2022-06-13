library(tidyverse)
library(ggplot2)
library(tidyr)
library(moments)
library(caret)
library(glmnet)
#####importation
####Exploration
getwd()
setwd("C:\\Users\\Aymen\\Desktop\\Datasets")
df= read.table('home_data.csv', sep=',', header = TRUE, fill = TRUE, quote="\"")
head(df)
summarize(df)
dim(df)
view(df)
df=as_tibble(df)
f_names=colnames(df)#getting column names in a vector
sapply(df, class)   #date is a string
#this part is optional because we're going to drop date and id
Date=as.Date(substring(df$date,0,8), tryFormats = c("%Y%m%d","%Y-%m-%d", "%Y/%m/%d"),
             optional = FALSE)
df=subset(df, select= -c(date))
head(df)
cbind(df,Date)
#displaying correlation heatmap
cormat <-round(cor(df),2)
head(cormat)
col<- colorRampPalette(c("blue", "white", "red"))(20)
heatmap(cormat, col=col, symm=TRUE)

##we could rename the columns if we had better documentation/description 
#but for this dataset the meaning is clear
####preprocessing :
cormat1=cormat[1>abs(cormat)] #removing the diagonal
cormat1[abs(cormat1)>0.7]     #we choose 0.8 as the significant linear corrlation level
head(cormat)
#by reading the dendrogram we can choose a representative of a class based on the depth in the hierarchy
df_new=data.frame(df$price,df$sqft_living,df$sqft_above,df$bathrooms,df$bedrooms,df$lat,df$sqft_basement,df$view,df$floors)
colnames(df_new) <-c("price","sqft_living","sqft_above","bathrooms","bedrooms","lat","sqft_basement","view","floors")
#we choose 8 variables that best describe the desicion of what price to give a house



head(df_new)
#handling missing variables
col_names=colnames(df_new)

NA2mean <- function(x) replace(x, is.na(x),  mean(x, na.rm = TRUE))
replace(df_new, TRUE, lapply(df_new, NA2mean))

head(df_new)
#replacing with the mean has made the floor feature contain non sensical data(1.5 floors)
lapply(df_new$floors, floor)
head(df_new)

#scaling and normalizing the features
#normalize <- function(myVar) zVar <- (myVar - mean(myVar)) / sd(myVar)
#df_n_scaled=lapply(df_new, normalize)
df.scaled <- as.data.frame(scale(df_new))

#checking for outliers
library(reshape)
meltData <- melt(df.scaled)
boxplot(data=meltData, value~variable)


for (col in c("price","sqft_living","sqft_above","bathrooms","bedrooms","lat","sqft_basement","view","floors")){
  L <- quantile(df.scaled[[col]] ,  probs = seq(0, 1, 0.25))
  Q1<-L[1]
  Q3<-L[3]
  iqr <- Q3-Q1
  
  upper_limit <- Q3 + (iqr*1.5)
  lower_limit <- Q1 - (iqr*1.5)
  
  for (value in df.scaled$col)  
  {print(value )
    if ((value > upper_limit) | (value < 0)) 
    {
      df.scaled<- df.scaled[-(which(df.scaled$col == value)),]
    }
  }
}
dim(df.scaled)
remove_outliers(df.scaled)
dim(df.scaled)
meltData <- melt(df.scaled)
boxplot(data=meltData, value~variable)
remove_outliers(df.scaled)
#checking the skew and kurtosis of the features
summary(df.scaled)
skewness(df.scaled) #we have values skewed to the right(above the mean)
kurtosis(df.scaled)
#If the kurtosis is greater than 3, then the dataset has heavier tails than a normal distribution (more in the tails).
#meaning alot of  outliers 
#If the kurtosis is less than 3, then the dataset has lighter tails than a normal distribution (less in the tails).
#meaning there's not alof of outliers 

###visualisations
f<-ggplot(df.scaled,aes())
f+geom_col(x=df.scaled[2:9],y=df.scaled$price)+coord_cartesian()+stat_sf_coordinates()
last_plot()
#hist
p<-ggplot(df.scaled, aes(x=df.scaled[2:9],y=y=df.scaled$price)) + 
  geom_histogram(color="black", fill="white")
last_plot()
#bar chart
meltData <- melt(df.scaled, id.vars = "features") # melt the dataframe to long form

ggplot(meltData) +
  geom_histogram(aes(x = df.scaled[2:9], y = df.scaled$price), stat = "identity", fill = "red", width = 0.4) +
  geom_histogram(aes(x = df.scaled[2:9], y = df.scaled$price), stat = "identity", fill = "blue", width = 0.5, position = "dodge") +
  ggtitle("features to price contribution")
last_plot()
#scatter plot
scatterplot(mpg ~ wt | cyl, data=df.scaled,
            xlab="feature name", ylab="price",
            main="Enhanced Scatter Plot",
            labels=column.names(df.scaled))
#the vizualization section didn't work .
#I check the ggplot2 cheatsheet and didn't understand the parameters
#the code above is copies of what ppl suggested on stackoverflow

###
## 75% of the sample size
smp_size <- floor(0.75 * nrow(df.scaled))

## set the seed to make your partition reproducible
set.seed(123)
train_ind <- sample(seq_len(nrow(df.scaled)), size = smp_size)

train <-df.scaled[train_ind, ]
test <- df.scaled[-train_ind, ]

#linear model
lm_vanilla = lm(formula=price~ sqft_living+sqft_above+bathrooms+bedrooms+lat+sqft_basement+view+floors , data = train) #Create the linear regression
sm1<-summary(lm_vanilla)
print(sm1)

pred1 <- predict(lm_vanilla, newdata = test)
rmse <- sqrt(sum((exp(pred1) - test$price)^2)/length(test$price))
c(RMSE = rmse, R2=summary(lm_vanilla)$r.squared)
MSE0=mean(sm1$residuals^2)
RSE=sqrt(deviance(lm_vanilla)/df.residual(lm_vanilla))#calculate residual standard error

#K fold cross validation
set.seed(123) 
train.control <- trainControl(method = "repeatedcv", 
                              number = 10, repeats = 3)
# Train the model
lm_k_cv <- train(formula=price~ sqft_living+sqft_above+bathrooms+bedrooms+lat+sqft_basement+view+floors, data = df.scaled, method = "lm",
                 trControl = train.control)
# Summarize the results
print(lm_k_cv)

#Exploring regularized regressors:
cols_reg = col_names[2:9]

dummies <- dummyVars(formula=price~ sqft_living+sqft_above+bathrooms+bedrooms+lat+sqft_basement+view+floors, data = df.scaled[,cols_reg])

train_dummies = predict(dummies, newdata = train[,cols_reg])

test_dummies = predict(dummies, newdata = test[,cols_reg])

print(dim(train_dummies)); print(dim(test_dummies))


#### Ridge Regression
#Loss function = OLS + alpha * summation (squared coefficient values)

x = as.matrix(train_dummies)
y_train = train$unemploy

x_test = as.matrix(test_dummies)
y_test = test$unemploy

lambdas <- 10^seq(2, -3, by = -.1)
ridge_reg = glmnet(x, y_train, nlambda = 25, alpha = 0, family = 'gaussian', lambda = lambdas)

summary(ridge_reg)

#finding the best hyper parameter lambda
cv_ridge <- cv.glmnet(x, y_train, alpha = 0, lambda = lambdas)
optimal_lambda <- cv_ridge$lambda.min
optimal_lambda


##Lasso Regression
#Lasso regression, or the Least Absolute Shrinkage and Selection Operator
#Loss function = OLS + alpha * summation (absolute values of the magnitude of the coefficients)
lambdas <- 10^seq(2, -3, by = -.1)

# Setting alpha = 1 implements lasso regression
lasso_reg <- cv.glmnet(x, y_train, alpha = 1, lambda = lambdas, standardize = TRUE, nfolds = 5)

# Best hyper-parameter
lambda_best <- lasso_reg$lambda.min 
lambda_best

###predicting with the lasso model
lasso_model <- glmnet(x, y_train, alpha = 1, lambda = lambda_best, standardize = TRUE)

predictions_train <- predict(lasso_model, s = lambda_best, newx = x)

predictions_test <- predict(lasso_model, s = lambda_best, newx = x_test)

#####Elastic Regression :
#Elastic Net combines feature elimination from Lasso and feature coefficient reduction from the Ridge model to improve the model's predictions.
elastic_reg <- train(formula=price~ sqft_living+sqft_above+bathrooms+bedrooms+lat+sqft_basement+view+floors,
                     data = train,
                     method = "glmnet",
                     preProcess = c("center", "scale"),
                     tuneLength = 10,
                     trControl = train_cont)


# Best tuning parameter
elastic_reg$bestTune

# Make predictions on training set
predictions_train <- predict(elastic_reg, x)

# Make predictions on test set
predictions_test <- predict(elastic_reg, x_test)

