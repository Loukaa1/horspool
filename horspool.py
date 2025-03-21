def naive_search(text, pattern, case_sensitive=True) :
    t = len(text)
    p = len(pattern)
    result = []
    for i in range(t-p+1) :
        j = 0
        if case_sensitive :
            while j<p and text[j+i] == pattern[j] :
                j += 1
        else :
            while j<p and text[j+i].upper() == pattern[j].upper() :
                j += 1
        if j == p :
            result.append(i)
    return result
