def solutionG(txt):
    txt = txt.lower()
    new = txt
    for symbol in txt:
        if not symbol.isalpha():
            new = new.replace(symbol, '')
    if new[::-1] == new:
        return True
    return False


txt = 'A man, a plan, a canal: Panama'
print(solutionG(txt))
