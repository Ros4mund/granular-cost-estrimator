import numpy as np

# for i in range(0,9):
#      for j in range(0,3):
#          for k in range(0,1072):
#             file = np.load(r'C:\Users\Jiahe Zhang\Desktop\CLEO project\encoding_output\condition1s_0.np.npy')[0][i][j][0][k]
#             if file != 0:
#                 print('1',i, j,'1', k, file)

    # np.savetxt(r'C:\Users\Jiahe Zhang\Desktop\CLEO project\encoding_output\extra_info.txt',file, fmt='%s', newline='\n')
file = np.load(r'C:\Users\Jiahe Zhang\Desktop\CLEO project\encoding_output\condition_masks_0.np.npy')

print(file)
print(file.shape)