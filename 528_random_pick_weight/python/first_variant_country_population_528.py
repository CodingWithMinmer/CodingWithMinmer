import random

class SolutionVariant528:
    def __init__(self, weights):
        self.weights = weights
        self.prefix_sum = []
        prefix = 0
        for _,weight in weights:
            self.prefix_sum.append(prefix+weight)
            prefix += weight
        print(self.prefix_sum,prefix)
        self.totalSum = prefix

        
    # def pickIndexWrapper(self, target_value):
    #     pass

    def pickIndexWrapper(self,target):
        print(f'finding target {target}')
        l =0
        r = len(self.prefix_sum)
        while l < r:
            mid =(l+r) //2
            print(self.prefix_sum[mid],mid,self.prefix_sum[mid] <= target,f'target {target}')
            if target >= self.prefix_sum[mid]:
                print('move l')
                l = mid +1
            else:
                print('move r')
                r = mid
            print((l,r))

        return self.weights[l][0]
       
       
       
# --- Test Cases ---
if __name__ == "__main__":
    input_data = [
        ("US", 300),
        ("VN", 100),
        ("BR", 200)
    ]
    s = SolutionVariant528(input_data)

    print("Testing US range (0-299):")
    assert s.pickIndexWrapper(0) == "US"
    assert s.pickIndexWrapper(150) == "US"
    assert s.pickIndexWrapper(299) == "US"
    print("US tests passed!")

    print("\nTesting VN range (300-399):")
    assert s.pickIndexWrapper(300) == "VN"
    assert s.pickIndexWrapper(375) == "VN"
    assert s.pickIndexWrapper(399) == "VN"
    print("VN tests passed!")

    print("\nTesting BR range (400-599):")
    assert s.pickIndexWrapper(400) == "BR"
    assert s.pickIndexWrapper(420) == "BR"
    assert s.pickIndexWrapper(599) == "BR"
    print("BR tests passed!")

    print("\nAll tests passed successfully!")