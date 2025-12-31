class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_board = []
        total_score = 0
        for op in operations:
            if op == "C":
                score_board.pop()
            elif op == "D":
                last_score = score_board[len(score_board) - 1]
                score_board.append(2 * last_score)
            elif op == "+":
                last_score = score_board[len(score_board) - 1]
                second_last_score = score_board[len(score_board) - 2]
                total = last_score + second_last_score
                score_board.append(total)
            else:
                score_board.append(int(op))
        total_score = sum(score_board) 
        return total_score

  # Runtime: Beats 100%
  # Memory: Beats 94.67%
