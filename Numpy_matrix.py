import numpy as np

def singular_matrix(rows, colums):
    while True:
        singular = np.random.randint(1, 11, size=(rows, colums))
        det = np.linalg.det(singular)
        if det == 0:
            print(singular)
            break
        else:
            continue

def non_singular(rows, colums):
    while True:
        nonsingular = np.random.randint(1, 11, size=(rows, colums))
        det = np.linalg.det(nonsingular)
        if det != 0:
            print(nonsingular)
            break
        else:
            continue

def adding_matrix():
    print("Enter the matrix Data")
    row = int(input("Enter the rows: "))
    col = int(input("Enter the colums: "))
    matrix1= []
    for i in range(row):
        rows  = []
        for j in range(col):
            elements = int(input(f"Enter the position of [{i}, {j}]: "))
            rows.append(elements)
        matrix1.append(rows)
    print("For second matrix")
    matrix2 = []
    for i in range(row):
        rows  = []
        for j in range(col):
            elements = int(input(f"Enter the position of [{i}, {j}]: "))
            rows.append(elements)
        matrix2.append(rows)

    matrix1 = np.array(matrix1)
    matrix2 = np.array(matrix2)



    add_matrix = np.add(matrix1, matrix2)
    print(add_matrix)

def main():
    while True:
        print("1) Generate singular matrix")
        print("2) Generate Non-singular matrix")
        print("3) Addition of 2 matrix")
        print("4) Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            rows = int(input("Enter the rows: "))
            colums = int(input("Enter the columns: "))
            singular_matrix(rows, colums)
        elif choice == 2:
            rows = int(input("Enter the rows: "))
            colums = int(input("Enter the columns: "))
            non_singular(rows, colums)
        elif choice == 3:
            adding_matrix()

        elif choice == 4:
            break
        else:
            print("Please enter a valid option")

if __name__ == "__main__":
    main()

