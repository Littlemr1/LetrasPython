#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *                                                                      
#  *****

for i in range(7):
    for j in range(7):
        if 0 <= i <= 5 and j == 1:
            print('*', end='')
        elif i == 6 and 1 <= j <= 5:
            print('*', end='')
        else:
            print(' ', end='')
    print()
