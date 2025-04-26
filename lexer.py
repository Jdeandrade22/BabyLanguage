def tokenize(SrcCode):
    Token = []
    stored_num = []

    for char in SrcCode: 
        if char in "0123456789":
            if len(stored_num) == 0:
                stored_num = [char, "NUMBER"]
            else:
                stored_num = [stored_num[0] + char, "NUMBER"]
            
        if len(stored_num) > 0 and char not in "0123456789":
            Token.append(stored_num)
            stored_num = []

        if char in "+-*/()":
            lookup = {
                "+": "PLUS",
                "-": "MINUS",
                "*": "MULTIPLICATION",
                "/": "DIVISION",
                "(": "LPAREN",
                ")": "RPAREN"
            }
            Token.append([char, lookup.get(char)])
        
    if len(stored_num) > 0:
        Token.append(stored_num)

    return Token

