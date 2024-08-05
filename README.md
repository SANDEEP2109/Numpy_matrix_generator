1. Generating a Singular Matrix:
Function: singular_matrix(rows, columns)

How It Works:
The function uses np. random. r.matrix to generate a matrix of random numbers with an integer value between 1 to 10.
It calculates the determinant using np Every step gets calculated using the original matrix and the determinant value. linalg. det.
If the determinant is then it prints the matrix and exits. If not, it proceeds to produce new matrices in order to determine another singular one.
2. Generating a Non-Singular Matrix:
Function: non_singular(rows, columns)
Purpose: To share with everybody a random non-singular matrix, that is a matrix with a determinant other than zero.
How It Works:
It is similar to singular_matrix, it firstly generates a random matrix and then calculate the determinant of the matrix.
If the determinant is non zero, then it prints the matrix and terminates the program. If not, it carries on generating new matrices until a non-singular one is generated.
[non-singular matrices] If not, then the function proceeds to create new matrices until such time that one for it is non-singular.
3. Adding Two Matrices:
Function: adding_matrix()
Purpose: To accept two matrices from the user, then add them and then return the computed matrix.
How It Works:
The user enters the dimensions and values of the matrices A and B that they want the system to utilize or operate on.
It reads the given input, transforms the lists to the NumPy type through the use of np, and then adds the corresponding elements in the arrays dependent on the position. add.
Then, it displays matrix: which refers to the entire matrix that has been formulated to arrive at the final value.
4. Main Function and User Interaction:Main Function and User Interaction:
Function: main()
Purpose: in order to make the work less dependent on the external environment, it is proposed to implement the options to be launched through the command line.
How It Works:
Displays a menu with four options:Displays a menu with four options:
Generate a singular matrix
Generate a non-singular matrix
Add two matrices
Exit the program
Since the final decision of the user is to input a digit, it goes to the functions array at that index or the program terminates.
5. Program Execution:
The script includes the standard Python if __name__ == "__main__": to prevent calling main() when the script is imported as a module and runs only when the script is called directly.
Example Usage:
Generate Singular Matrix:

Choose option 1.
Input the matrix size that the user wants their matrix to have.
See the randomly created matrix with the determinant equal to zero.
Generate Non-Singular Matrix:

Choose option 2.
To exit the program, you need to type the negative value of any of the matrix sides – in other words, the program will offer you to enter the number of rows and columns of your matrices, and you should type ‘-n’ where n is the number of rows or columns if you want to exit the program.
Look at a specific example of a matrix of order n and containing elements that are non-zero with having a determinant of non-zero value.
Add Two Matrices:

Choose option 3.
Input the dimensions and values for two matrices.
Look at the result of elements added according to their position.
Exit:

Select the option 4 on the program to stop the program.
