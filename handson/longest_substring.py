def length_of_longest_substring(s):
    '''
    Given a string, find the length of the longest substring without repeating characters.
    :param s:
    :return:
    '''


    _str=s[0]
    li =[]
    for e in s[1:] :
        if _str.find(e) == -1:
            _str+=e
        elif _str == e:
            _str = ""
        else :
            li.append(_str)
            _str =e

    li.append(_str)
    li.sort(key= lambda x: len(x))
    return li[-1]

if __name__ =='__main__':
    s = "abcabcabcdebbabcdefg"
    print(length_of_longest_substring(s))