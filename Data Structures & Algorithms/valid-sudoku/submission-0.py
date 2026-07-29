class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # loop through the entire matrix board and 
        # 1 use a hash set to check if a value already exists.
        # but we wil ldo so for each row, column and 3x3 grid
        # we will build a 3x3 grid with a ahsh for each. 

        row_col_length = 9

        #Build row and col hash sets
        row_hash = [ set() for i in range(row_col_length) ]
        col_hash = [ set() for i in range(row_col_length) ]

        #3x3 grid hash
        grid_hash = [
            [set(), set(), set()],
            [set(), set(), set()],
            [set(), set(), set()]
        ]

        #iterate through entire board
        for i in range(row_col_length):
            for j in range(row_col_length):

                #skip if not filled in
                if board[i][j] == ".":
                    continue

                #check if row already exists
                if board[i][j] in row_hash[i]:
                    return False
                #add to the set and keep moving
                else:
                    row_hash[i].add(board[i][j])
                
                  #check if col already exists
                if board[i][j] in col_hash[j]:
                    return False
                #add to the set and keep moving
                else:
                    col_hash[j].add(board[i][j])

                #check if in 3x3. Floor diviision to get index
                grid_row = i // 3
                grid_col = j // 3

                if board[i][j] in  grid_hash[grid_row][grid_col]:
                    return False
                #add to the set and keep moving
                else:
                    grid_hash[grid_row][grid_col].add(board[i][j])
        return True



