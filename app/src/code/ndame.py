import sys
import requests
import json

class QueenChessBoard:
    def __init__(self, size):
        self.size = size
        self.columns = []
 
    def get_size(self):
        return self.size
 
    def get_queens_count(self):
        return len(self.columns)
 
    def place_in_next_row(self, column):
        self.columns.append(column)
 
    def remove_in_current_row(self):
        return self.columns.pop()
 
    def is_this_column_safe_in_next_row(self, column):
        row = len(self.columns)
 
        for queen_column in self.columns:
            if column == queen_column:
                return False

        for queen_row, queen_column in enumerate(self.columns):
            if queen_column - queen_row == column - row:
                return False

        for queen_row, queen_column in enumerate(self.columns):
            if ((self.size - queen_column) - queen_row
                == (self.size - column) - row):
                return False
 
        return True
    
def rabbit(solutions):
    APIENDPOINT = "http://172.17.0.1:5000"

    task = {
        "pid":sys.argv[2],
        "id": sys.argv[3],
        "solutions":solutions
    }

    payload= {}
    queue2 = 'DONE'
    payload['task'] = task
    mydata = {"data": json.dumps(payload)}
    r = requests.post("{}/rabbit/{}".format(APIENDPOINT,queue2), data=mydata)
 

def write_in_logs(message):
    payload= {}
    payload['message'] = message
    mydata = {"data": json.dumps(payload)}
    r = requests.post("{}/rabbit/logs/{}".format(APIENDPOINT,'logs'), data=mydata)
 
def print_all_solutions_to_n_queen(size):
    board = QueenChessBoard(size)
    number_of_solutions = print_all_solutions_helper(board)

    return number_of_solutions
 
def print_all_solutions_helper(board):
    size = board.get_size()
 
    if size == board.get_queens_count():
        return 1
 
    number_of_solutions = 0

    for column in range(size):
        if board.is_this_column_safe_in_next_row(column):
            board.place_in_next_row(column)
            number_of_solutions += print_all_solutions_helper(board)
            board.remove_in_current_row()
 
    return number_of_solutions
 
n = int(sys.argv[1])
solutions = print_all_solutions_to_n_queen(n)
rabbit(solutions)