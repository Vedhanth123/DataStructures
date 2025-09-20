class Router:

    def __init__(self, memoryLimit):
        self.size = memoryLimit
        self.table = []
        self.dest_table = defaultdict(list)
        self.duplicate_table = set()


    def addPacket(self, source, destination, timestamp):

        if((source, destination, timestamp) in self.duplicate_table):
            return False
        
        else:
            if(self.size != 0):
                self.table.append((source, destination, timestamp))
                self.duplicate_table.add((source, destination, timestamp))
                self.dest_table[destination].append(timestamp)
                self.size -= 1
            else:
                self.forwardPacket()

                self.table.append((source, destination, timestamp))
                self.duplicate_table.add((source, destination, timestamp))
                self.dest_table[destination].append(timestamp)  
                self.size -= 1
            return True


    def forwardPacket(self):

        if(self.table):
            old_src, old_dest, old_time = self.table.pop(0)
            self.duplicate_table.remove((old_src, old_dest, old_time))
            temp_list = self.dest_table[old_dest]
            temp_list.remove(old_time)
            self.dest_table[old_dest] = temp_list
            self.size += 1
            return [old_src, old_dest, old_time]
        else:
            lister = []
            return lister


    def getCount(self, destination, startTime, endTime):
        # Get the sorted list of timestamps
        timestamps = self.dest_table.get(destination, [])
        
        # Find the insertion point for startTime (first element >= startTime)
        left_index = bisect.bisect_left(timestamps, startTime)
        
        # Find the insertion point for endTime (first element > endTime)
        right_index = bisect.bisect_right(timestamps, endTime)
        
        # The count is the difference between the indices
        return right_index - left_index


# Your Router object will be instantiated and called as such:
# obj = Router(3)
# param_1 = obj.addPacket(1,4,90)
# param_1 = obj.addPacket(2,5,90)
# param_1 = obj.addPacket(1,4,90)
# param_1 = obj.addPacket(3,5,95)
# param_1 = obj.addPacket(4,5,105)
# param_2 = obj.forwardPacket()
# param_1 = obj.addPacket(5,2,110)
# param_1 = obj.getCount(5,100,110)