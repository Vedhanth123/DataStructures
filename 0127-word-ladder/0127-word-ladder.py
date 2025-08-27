class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # approach:
        # I am considering BFS as I have to find out shortest path between two nodes
        # I will use queue as I need it for BFS
        # I will also use visited set so that I will not put myself in an infinite loop
        # If I reach the endWord I will stop the queue and return the level
        # Else I will directly return 0

        answer = 0

        # this is done so that I can easily check if the word is present in the list or not in O(1) time
        wordList = set(wordList)    
        visited = {beginWord}

        queue = [(beginWord,1)] # starting point of the word ladder 

        while(queue):

            curr_word, curr_level = queue.pop(0)

            if(curr_word == endWord):
                answer = curr_level
                break
            
            for x in range(len(curr_word)):

                for y in range(97, 97+26):
                    
                    new_word = curr_word[:x] + chr(y) + curr_word[x+1:]
                    if(new_word in wordList and new_word not in visited):
                        queue.append((new_word, curr_level + 1))
                        visited.add(new_word)
        
        return answer