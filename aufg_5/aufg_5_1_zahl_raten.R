get_number <- function()
{ 
  my_number <- readline(prompt="Please enter a number: ")
  if(!grepl("^[0-9]+$",my_number))
  {
    return(get_number())
  }
  return(as.integer(my_number))
}

try_get_number <- function()
{ 
  tryCatch(
    {
      my_number <- readline(prompt="Please enter a number: ")
      return(integer(my_number))
    },
    error = function(e)
      {
      message('Caught an error!')
      print(e)
      }
  )
}

cat("Nummer", try_get_number())

# real program start here

random_number <- round(runif(1) * 100, digits = 0)
guess <- -1

("Guess a number between 0 and 100.\n")

while(guess != random_number)
{ 
  guess <- get_number()
  if (guess == random_number)
  {
    cat("Congratulations,", random_number, "is correct!\n")
  }
  else if (guess < random_number)
  {
    cat("It's bigger!\n")
  }
  else if(guess > random_number)
  {
    cat("It's smaller!\n")
  }
}