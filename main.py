import lexer

srcCode = "((12+3*5)+5/4)"
tokSeq = lexer.tokenize(srcCode)
for token in tokSeq:
    print(token[1], token[0]) 