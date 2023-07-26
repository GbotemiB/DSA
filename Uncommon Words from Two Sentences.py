class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        str_connected = s1.split() + s2.split()
        str_dict  = {}
        uncommon = []

        for i in str_connected:
            if i not in str_dict.keys():
                str_dict[i] = 1
            else:
                str_dict[i] += 1
        
        for i in str_dict:
            if str_dict[i] == 1:
                uncommon.append(i)
        
        return uncommon

