def isAnagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    freq_map={}
    for ch in s1:
        freq_map[ch]=freq_map.get(ch,0)+1
    for ch in s2:
        if ch not in freq_map:
            return False
        freq_map[ch]-=1
        if freq_map[ch]==0:
            del freq_map[ch]
    return len(freq_map)==0
s1="HEART" 
s2="EARTH"
result=isAnagram(s1,s2)
print(result)
