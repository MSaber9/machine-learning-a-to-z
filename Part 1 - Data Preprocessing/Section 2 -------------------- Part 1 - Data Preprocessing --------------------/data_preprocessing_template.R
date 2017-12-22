# Data Preprocessing

# Importing the dataset
dataset = read.csv('Data.csv')

# Taking care of missing data
# There are some missing values on the dataset. We could eliminate the rows, but those rows could have valuable information.
# Instead of that, we need to replace it with some other values. For example, the mean value of the column or the most frequent value.
# In this case, the we replace them with the mean.
dataset$Age = ifelse(is.na(dataset$Age), 
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Age
                     )

dataset$Salary = ifelse(is.na(dataset$Salary), 
                        ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                        dataset$Salary
                        )

# Encoding categorical data
dataset$Country = factor(dataset$Country,
                         levels = c('France', 'Spain', 'Germany'),
                         labels = c(1, 2, 3)
                         )

dataset$Purchased = factor(dataset$Purchased,
                           levels = c('No', 'Yes'),
                           labels = c(0, 1)
                           )