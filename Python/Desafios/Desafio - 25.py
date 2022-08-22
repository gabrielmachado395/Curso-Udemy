# Write a function which makes a list of strings representing all of the ways you can balance n pairs of parentheses

# Examples
# balanced_parens(0) => [""]
# balanced_parens(1) => ["()"]
# balanced_parens(2) => ["()()","(())"]
# balanced_parens(3) => ["()()()","(())()","()(())","(()())","((()))"]

table = [['']]
def balanced_parens(n):
    if n < len(table):
        return table[n]

    result = []
    for i in range(n):
        for x in balanced_parens(i):
            for y in balanced_parens(n - i - 1):
                result.append('(' + x + ')' + y)

    table.append(result)
    return table[n]