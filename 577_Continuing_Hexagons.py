#just testing to see if the pattern that I've found holds for higher order triangles

def hex(n):
    if(n==3):
        return 1
    if(n==4):
        return 3
    else:
        return hex(n-1)+3*(n-4)
