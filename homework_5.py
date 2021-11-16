# Find All Numbers Disappeared in an Array
from collections import Counter

def find_disappeared_numbers(nums):
  return list(set(Counter([i for i in range(1, len(nums)+1)]))^ set(Counter(nums)))

  
print(find_disappeared_numbers([4,3,2,7,8,2,3,1]))
########################################################################################



#  Keyboard Row
ROWS_DICT = {
    "first": "qwertyuiop",
    "second": "asdfghjkl",
    "third": "zxcvbnm"
}

def checking_word(word):
  for _, value in ROWS_DICT.items():
    for char in word:
      if char.lower() not in value:
        break
    else:
      return True
  return False


def find_words(words):
  return [word for word in words if checking_word(word)]


print(find_words(["Hello","Alaska","Dad","Peace"]))
#############################################################################################


# Transpose Matrix
import numpy as np

def transpose_matrix(matrix):
  # np.array(matrix).T.tolist()
  # [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
  arr_transpose = np.transpose(matrix)
  return arr_transpose.tolist()

# transpose_matrix([[1,2,3],[4,5,6],[7,8,9]])
transpose_matrix([[1,2,3],[4,5,6]])
###################################################################################



# Reshape the Matrix

def matrix_to_row(mat):
  row = []
  for r_m in mat:
    row += r_m
  return row


def matrix_reshape(mat, r, c):
  row = matrix_to_row(mat)
  if r * c != len(row):
    return f" This conn't reshape row {r}, column {c}"
  return [row[i*c: (i+1)*c] for i in range(r)]

# solution second
import numpy as np

def reshape_matrix_used_numpy(mat, r, c):
  arr = np.array(mat)
  return arr.reshape(r, c).tolist()

reshape_matrix_used_numpy(mat, r, c)


mat = [[1,2],[3,4]]
r = 4
c = 1
matrix_reshape(mat, r, c)
####################################################################################




def count_battle_ships( board):
    if not board:
        return 0

    count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ".":
                continue
            if i > 0 and board[i - 1][j] == "X":
                continue
            if j > 0 and board[i][j - 1] == "X":
                continue
            count += 1
    return count

# board = [["."]]
board =[["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
count_battle_ships( board)


