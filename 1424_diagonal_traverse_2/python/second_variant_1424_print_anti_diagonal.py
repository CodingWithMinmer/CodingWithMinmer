
def second_variant_1424_print_anti_diagonal(nums):
    m =len(nums)

    def helper(row,col):
        while row < m and col > -1:
            print(nums[row][col],end=' ')
            row+=1
            col-=1
        print('\n')
        
    for c in range(0,len(nums[row])):
        helper(0,c)
        

    for r in range(1,m):
        helper(r,len(nums[r])-1)
        

if __name__ == '__main__':
    nums = [[1,2,3],[4,5,6],[7,8,9]]
    second_variant_1424_print_anti_diagonal(nums)

    nums = [[1],[2],[3]]
    second_variant_1424_print_anti_diagonal(nums)

    nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
    second_variant_1424_print_anti_diagonal(nums)


    