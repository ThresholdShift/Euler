from numpy import genfromtxt

#open the source grid file
gridlist = genfromtxt(r'C:\Users\jwrus_000\Google Drive\Documents\Python Scripts\Euler\011_Grid.csv', delimiter=',')


#create variables to store results
HighestProduct = 1
TempProduct = 1
HighestString = [0,0,0,0]
HighCoordinates = [0,0]

for row in range(len(gridlist)):
    for col in range(len(gridlist[row])):
        if row < 17:
            TempProduct =  gridlist[row][col] * gridlist[row+1][col] * gridlist[row+2][col] * gridlist[row+3][col]
            if TempProduct > HighestProduct:
                HighestProduct = TempProduct
                HighestString =  [gridlist[row][col], gridlist[row+1][col], gridlist[row+2][col], gridlist[row+3][col]]
                HighCoordinates = [row, col]

        if  col < 17:
            TempProduct =  gridlist[row][col] * gridlist[row][col+1] * gridlist[row][col+2] * gridlist[row][col+3]
            if TempProduct > HighestProduct:
                HighestProduct = TempProduct
                HighestString = [gridlist[row][col], gridlist[row][col+1], gridlist[row][col+2], gridlist[row][col+3]]
                HighCoordinates = [row, col]

        if row < 17 and col < 17:
            TempProduct =  gridlist[row][col] * gridlist[row+1][col+1] * gridlist[row+2][col+2] * gridlist[row+3][col+3]
            if TempProduct > HighestProduct:
                HighestProduct = TempProduct
                HighestString = [gridlist[row][col], gridlist[row+1][col+1], gridlist[row+2][col+2], gridlist[row+3][col+3]]
                HighCoordinates = [row, col]

        if row > 3 and col < 17:
            TempProduct =  gridlist[row][col] * gridlist[row-1][col+1] * gridlist[row-2][col+2] * gridlist[row-3][col+3]
            if TempProduct > HighestProduct:
                HighestProduct = TempProduct
                HighestString = [gridlist[row][col], gridlist[row-1][col+1], gridlist[row-2][col+2],  gridlist[row-3][col+3]]
                HighCoordinates = [row, col]

print(HighestProduct)
print(HighestString)
print(HighCoordinates)
