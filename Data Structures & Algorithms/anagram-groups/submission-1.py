class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        an = []
        for idx_s, s in enumerate([''.join(sorted(st)) for st in strs]):
            s_arr = []
            for idx_oth, oth in enumerate(strs):
                if ''.join(sorted(oth)) == s:
                    s_arr.append(oth)
            if not s_arr in an:
                an.append(s_arr)
        return an