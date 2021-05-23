#=
aufg_5_4:
- Julia version:
- Author: guido
- Date: 2021-05-22
=#

println(" 1. Create two matrices of the same layout and test if addition and subtraction of the matrix works as expected: C = A + B.", "\n")

A = rand( 2, 2 )
B = rand( 2, 2 )
print("A: ", A, "\n\n")
print("B: ", B, "\n\n")

C = A + B
print("C = A + B = ", C, "\n\n")

C = C - B
print("C = C - B so should be C = A: ", C, "\n\n")

if C == A
    print("Yes, both work as expected. \n\n")
else
    print("No, something went wrong")
end

println("2. Now compare matrix multiplication either this way A * B and this way A .* B. Whats the difference?!", "\n")

M = A * 4 # multiply each element with 4
print("A * 4 = ", M, "\n\n")

M1 = A * B
print("A * B = ", M1, "\n\n")
# normal matrice multiplication

M2 = A .* B
print("A .* B = ", M2, "\n\n")
# element-wise multiplication

println("3. What about matrix division with '/' or '\\' ?! \n\n")

println("Matrice division \n")
D1 = A / B
print("D1 = A / B = ", D1, "\n\n")

println("Inverse divion (equals inv(A) / inv(B)) \n")
D2 = A \ B
print("D2 = A \\ B = ", D2, "\n\n")

println("Close to the same as D2 (floating point inprecision) \n")
D3 = inv(A) / inv(B)
print("D3 = inv(A) / inv(B) = ", D3, "\n\n")

println("Different to D3 \n")
D4 = B / A
print("D4 = B / A = ", D4, "\n\n")

println("4. Create a 3x3 integer matrix A with useful numbers.")
println(" Now try A+1, A-1, A*2, A/2. \n")

A = [1 2 3; 4 5 6; 7 8 9]

# elementwise operations

#display( A + 1 ) # throws an error
display( A .+ 1 ) # same as before, so elementwise scalar addition
println("\n")
#display( A - 1 ) # throws an error
display( A .- 1 )
println("\n")
display( A * 2 )
println("\n")
display( A / 2 ) # same as * 0.5
println("\n")
display( A * 0.5 )
println("\n\n")
println("5. Now multiply a 3x4 matrix with a suitable (4)vector.\n")

B = [1 2 3 4; 5 6 7 8; 9 10 11 12]
V = [1, 2, 3, 4]

println("3x4 matrix multiplied with vector(4), results in vector(3).\n")
MV = B * V
print("B * V = ", MV, "\n")

println("Elementwise, each matrix row is multiplied with the associated vector row, this stays a 3x4 matrix.")
M3 = B .* [1, 2, 3]
print("B .* [1, 2, 3] = ", M3,"\n")