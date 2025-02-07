class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        
        color_map = defaultdict(int)
        balls_map = defaultdict(int)
        answer = []

        for balls, colors in queries:

            if(balls_map[balls] != 0):

                color_map[balls_map[balls]] -= 1
                if(color_map[balls_map[balls]] == 0):
                    del color_map[balls_map[balls]]


            balls_map[balls] = colors
            color_map[colors] += 1 
            answer.append(len(color_map))

        return answer