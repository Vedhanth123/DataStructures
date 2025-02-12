class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
    
        # Step 1: Store the smallest index of each element in a lookup table
        MAX_VAL = 10**5
        smallest_index = [-1] * (MAX_VAL + 1)
        
        for j, elem in enumerate(elements):
            if smallest_index[elem] == -1:  # Store only the first occurrence (smallest index)
                smallest_index[elem] = j
        
        # Step 2: Assign elements to groups
        assigned = [-1] * len(groups)

        for i, group in enumerate(groups):
            best_index = -1  # Store the smallest element index found

            # Find divisors of `group`
            for d in range(1, int(group ** 0.5) + 1):
                if group % d == 0:  # d is a divisor
                    # Check if we have an element equal to `d`
                    if smallest_index[d] != -1:
                        if best_index == -1 or smallest_index[d] < best_index:
                            best_index = smallest_index[d]
                    
                    # Check the corresponding divisor `group/d`
                    if d != group // d and smallest_index[group // d] != -1:
                        if best_index == -1 or smallest_index[group // d] < best_index:
                            best_index = smallest_index[group // d]
            
            assigned[i] = best_index  # Assign best found index (-1 if none found)
        
        return assigned
