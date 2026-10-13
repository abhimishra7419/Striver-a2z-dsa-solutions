'''Solution'''
class Solution:
    def expressionAddOperators(self, num, target):
        result = []
        n = len(num)

        def backtrack(index, expression, total, last_operand):
            if index == n:
                if total == target:
                    result.append(expression)
                return
            for end in range(index, n):
                if end > index and num[index] == "0":
                    break
                operand_str = num[index:end + 1]
                operand = int(operand_str)
                if index == 0:
                    backtrack(end + 1, operand_str, operand, operand)
                else:
                    backtrack(end + 1, expression + "+" + operand_str, total + operand, operand)
                    backtrack(end + 1, expression + "-" + operand_str, total - operand, -operand)
                    new_total = total - last_operand + last_operand * operand
                    backtrack(end + 1, expression + "*" + operand_str, new_total, last_operand * operand)
        backtrack(0, "", 0, 0)
        return result


if __name__ == "__main__":
    num = "123"
    target = 6
    print(Solution().expressionAddOperators(num, target))
