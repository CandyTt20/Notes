def find_word_concatenation(s, words):
    result_indices = []
    # TODO: Write your code here
    pass_map = {}
    frequency_map={}
    for i in words:
        if i not in pass_map:
            pass_map[i] = 0
        pass_map[i] += 1
    
    window_start,window_end = 0,len(words[0])
    while window_end <= len(s):
        current_word = s[window_start:window_end]
        next_word = s[window_start + len(words[0]):window_end + len(words[0])]
        
        if current_word in pass_map and next_word in pass_map:
            if current_word not in frequency_map:
                frequency_map[current_word] = 0
            frequency_map[current_word] += 1
            
            if frequency_map == pass_map:
                result_indices.append(window_end - len(words) * len(words[0]))
                frequency_map={current_word:1}
            window_start, window_end = window_start + len(words[0]), window_end + len(words[0])
        else:
            if frequency_map == pass_map:
                result_indices.append(window_end - len(words) * len(words[0]))
                frequency_map={current_word:1}
            window_start, window_end = window_start + 1, window_end + 1
            
        
            
    return result_indices
String = "catcatfoxfox"
Words=["cat", "fox"]
print(find_word_concatenation(String,Words))