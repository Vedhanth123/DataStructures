class ProductOfNumbers:

    def __init__(self):
        
        self.array = []
        self.prefix_product = []

    def add(self, num: int) -> None:

        ptr = 1
        if(len(self.array) >= 3):
            pre_pro = num
            while(ptr <= 3):
                pre_pro = self.array[-ptr] * pre_pro
                self.prefix_product[-ptr] = pre_pro
                ptr += 1
        elif(len(self.array) == 2):
            pre_pro = num
            while(ptr <= 2):
                pre_pro = self.array[-ptr] * pre_pro
                self.prefix_product[-ptr] = pre_pro
                ptr += 1
        elif(len(self.array) == 1):
            self.prefix_product[-ptr] = self.array[-ptr] * num
        

        self.array.append(num)
        self.prefix_product.append(num)
        
        print(f"array {self.array}")
        print(f"prefix {self.prefix_product}")

    def getProduct(self, k: int) -> int:
        
        return self.prefix_product[-k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)