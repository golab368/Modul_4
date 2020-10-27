def palindromy(slowo):
    if slowo == slowo[::-1]:
        print("True")
        return True
    else:
        print("False")
        return False
        
palindromy("kajak")