def tokenize(SrcCode):
    Token = []
    stored_num = []

    for char in SrcCode: 
        if char in "0123456789":
            if len(stored_num) == 0:
                stored_num = [char, "num"]

            else:
                stored_num = [stored_num[0] + char, "num"]
            
        if len(stored_num) > 0 and char not in "0123456789":
            Token.append(stored_num)
            stored_num = []

        if char in "+-*/()":
            lookup = {
                "+": "plus",
                "-": "minus",
                "*": "multiply",
                "/": "divide",
                "(": "lparen",
                ")": "rparen"
            }
            Token.append([char, lookup.get(char)])
        
    if len (stored_num)>0:
        Token.append(stored_num)
        print(stored_num)

    return Token