class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        left = 0
        right = k-1

        white_count = 0
        for x in range(left, right+1):
            if(blocks[x] == 'W'):
                white_count += 1
        
        # print(blocks[left:right+1])
        # print(white_count)  

        min_count = white_count
        if(k == len(blocks)):
            return min_count

        while(right < len(blocks)):

            if(blocks[left] == 'W'):
                white_count -= 1
            
            left += 1

            right += 1
            if(right < len(blocks)):

                if(blocks[right] == "W"):
                    white_count += 1


            print(blocks[left:right+1])
            print(white_count, min_count)

            min_count = min(min_count, white_count)
        
    
        return min_count