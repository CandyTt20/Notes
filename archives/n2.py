def find_word_concatenation(s, words):
    result_indices = []
    # TODO: Write your code here
    pass_map = {}
    frequency_map = {}
    point,steps=0,len(words[0])
    for i in words:
        if i not in pass_map:
            pass_map[i] = 0
        pass_map[i] += 1

    while point+steps<=len(s):
        if s[point:point + steps] in pass_map:
            temp = s[point:point + steps]
            if temp not in frequency_map:
                frequency_map[temp] = 0
            frequency_map[temp] += 1
            if frequency_map == pass_map:
                result_indices.append(point+steps-steps*len(words))
                frequency_map={temp:1}
            point += steps
            if s[point:point + steps] not in pass_map and point+steps<=len(s):
                frequency_map[temp] -= 1
                if frequency_map[temp] == 0:
                    del frequency_map[temp]
                point -= (steps - 1)
        else:
            point += 1
            
    return result_indices
                
            
String = "catcatfoxfox"
Words=["cat", "fox"]
print(find_word_concatenation(String,Words))