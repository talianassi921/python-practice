# nested_list = [[1,2,3],[4,5,6],[7,8,9]]
# nested_list[0][1] # 2
# nested_list[1][-1] # 6

# for l in nested_list:
#     for val in l:
#         print(val)
        
board = [[num for num in range(1,4)] for val in range(1,4)]
print(board)