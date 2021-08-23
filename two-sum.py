def twoSum(nums,target):

    dictionary = {}
    for i,num in enumerate(nums):
        
        remain = target - num
        if remain not in dictionary:
            dictionary[num] = i
        else:
            print([i,dictionary[remain]])
            return [i,dictionary[remain]]
            
def main():
    i = [3,2,3]
    twoSum(i,6)


if __name__ == '__main__':
    main()
