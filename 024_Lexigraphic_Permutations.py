import sys

tally = 0

for i1 in range(0,10):
    for i2 in range(0,10):
        if(i2 != i1):
            for i3 in range(0,10):
                if(i3 != i2 and i3 != i1):
                    for i4 in range(0,10):
                        if(i4 != i3 and i4 != i3 and i4 != i2 and i4 != i1):
                            for i5 in range(0,10):
                                if(i5 != i4 and i5 != i3 and i5 != i2 and i5 != i1):
                                    for i6 in range(0,10):
                                        if(i6 != i5 and i6 != i4 and i6 != i3 and i6 != i2 and i6 != i1):
                                            for i7 in range(0,10):
                                                if(i7 != i6 and i7 != i5 and i7 != i4 and i7 != i3 and i7 != i2 and i7 != i1):
                                                    for i8 in range(0,10):
                                                        if (i8 != i7 and i8 != i6 and i8 != i5 and i8 != i4 and i8 != i3 and i8 != i2 and i8 != i1):
                                                            for i9 in range(0,10):
                                                                if(i9!= i8 and i9 != i7 and i9 != i6 and i9 != i5 and i9 != i4 and i9 != i3 and i9 != i2 and i9 != i1):
                                                                    for i10 in range(0,10):
                                                                        if(i10 != i9 and i10!= i8 and i10 != i7 and i10 != i6 and i10 != i5 and i10 != i4 and i10 != i3 and i10 != i2 and i10 != i1):
                                                                           tally = tally +1
                                                                           if(tally == 1000000):
                                                                               print (str(i1)+str(i2)+str(i3)+str(i4)+str(i5)+str(i6)+str(i7)+str(i8)+str(i9)+str(10))
                                                                               sys.exit()
                                                                           
