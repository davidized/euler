# Problem 1: Multiples of 3 and 5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we 
# get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

library(tictoc)

tic()
total <- 0
for( i in 0:999 ) {
  if ( i %% 3 == 0 | i %% 5 == 0 ) total <- total + i
}
total
toc()

# A more efficient and more R method
tic()
total <- 0:999
sum( total[total %% 3 == 0 | total %% 5 == 0] )
toc()

