# Aufg_5_3
# Create a 2x4 two dimensional matrix with random floats in it
# and in the next step determine the biggest element.

matrix = rand(2,4)
println("Matrix: ", matrix, "\n")

max = findmax(matrix)
println(max)
println("Biggest value: ", max[1], " at index ", max[2])
println(matrix[max[2]])