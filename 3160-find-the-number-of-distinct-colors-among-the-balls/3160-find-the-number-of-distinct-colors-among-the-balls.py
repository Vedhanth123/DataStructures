class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        
        color_map = defaultdict(int)
        balls_array = [0] * (limit+1)
        answer = []

        for balls, colors in queries:

            if(balls_array[balls] != 0):

                color_map[balls_array[balls]] -= 1
                if(color_map[balls_array[balls]] == 0):
                    del color_map[balls_array[balls]]


            balls_array[balls] = colors
            color_map[colors] += 1 
            answer.append(len(color_map))

        return answer