class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # apporach 1

        answers = defaultdict(list)

        # 1) sort the strings first
        # 2) Find the frequency of each character
        # 3) Create a tuple out of that frequency
        # 4) Use that tuple as dictionary key
        # 5) Place all those words who have the same tuple
        # 6) convert that dictionary to list of lists

        for x in range(len(strs)):

            sorted_str = "".join(sorted(strs[x]))

            freq = tuple(Counter(sorted_str).items())

            print(freq)
            answers[freq].append(strs[x])
        
        return list(answers.values())


