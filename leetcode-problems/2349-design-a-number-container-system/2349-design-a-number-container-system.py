class NumberContainers:

    def __init__(self):
        
        self.number_to_index = defaultdict(SortedSet)
        self.index_to_number = {}

    def change(self, index: int, number: int) -> None:

        if(index in self.index_to_number):

            curr_number = self.index_to_number[index]
            self.number_to_index[curr_number].remove(index)

            if(not self.number_to_index[curr_number]):
                del self.number_to_index[curr_number]

        self.index_to_number[index] = number
        self.number_to_index[number].add(index)
  

    def find(self, number: int) -> int:
        
        if(number in self.number_to_index and self.number_to_index[number]):
            return self.number_to_index[number][0]
        else:
            return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)