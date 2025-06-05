#Second Variant Solution will not work if each has different column
#First Count the MaxDiameter
#Calcuate the column from r and d where r+c = d


def third_variant_1424_print_anti_diagonal(nums):
    maxDiagonal = 0
    for r in range(len(nums)):
        maxDiagonal = max(r + len(nums[r])-1,maxDiagonal)    

    for d in range(maxDiagonal+1):
        for r in range(len(nums)):
            c = d-r #cause r+c = d
            if c < 0:break
            if c > -1 and c < len(nums[r]):
                print(nums[r][c],end=' ')
        print('\n')
        


if __name__ == '__main__':   
    nums = [[1,2,3],[4,5,6],[7,8,9]]
    third_variant_1424_print_anti_diagonal(nums)

    nums = [[1],[2],[3]]
    third_variant_1424_print_anti_diagonal(nums)

    nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
    third_variant_1424_print_anti_diagonal(nums)    
    

    
