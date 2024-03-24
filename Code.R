library(dplyr)
library(tidyr)
library(tidyverse)
library(ggplot2)

checkpoint_eoc <- read_csv('./Random Sample of Data Files_03_04/checkpoints_eoc.csv')
checkpoints_pulse <- read_csv('./Random Sample of Data Files_03_04/checkpoints_pulse.csv')


checkpoints <- inner_join(drop_na(checkpoint_eoc), drop_na(checkpoints_pulse), by = c('student_id', 'class_id', 'book', 'chapter_number'))
head(checkpoint_eoc)
head(checkpoints_pulse)
head(checkpoints)

# renaming the columns in checkpoints

checkpoints <- inner_join(checkpoints_pulse, checkpoint_eoc, by = c('student_id', 'class_id', 'chapter_number', 'book')) %>% drop_na()

df <- checkpoints %>% 
  pivot_wider(values_fn = {mean},
              names_from = construct,
              values_from = response) %>%
  drop_na()

names(df) = c('book', 'release', 'institution_id', 'class_id', "student_id", 'chapter_number', "EOC", "n_possible", "n_correct", "n_attempt", "Cost", "Expectancy", "Intrinsic_Value", "Utility_Value")

model <- lm(EOC ~ Expectancy, data = df)

summary(model)

