"""class Solution:
	# @param A : tuple of integers
	# @return an integer
    my_dict = {}
	def majorityElement(A): 
        for count,i in enumerate(A):
            if i not in my_dict:
                my_dict[i]= count+1
            else:
                my_dict[i]= count+1
                
        for key in my_dict:
                if my_dict[key] == len(A)/2:
                    return key
                    
        """

def majorityElement(A):
    my_dict = {}
    for count,i in enumerate(A):
        if i in my_dict:
            # print(count)
            my_dict[i] = count
        else:
            my_dict[i] = count

    print(my_dict)

    # for key in my_dict:
    #     for i in len(A):
    #         if my_dict[key] == (len(A)//2):
    #             print(key)

    max_key = max(my_dict, key=my_dict.get)
    print(max_key)



majorityElement([2,1,2])
# obj = Solution()
# number = obj.majorityElement([2,1,2])
# print(number)