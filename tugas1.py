class student:
    def __init__(self,n,a,t):
        self.full_name = n
        self.age = a
        self.address = t
    def get_age(self):
        return self.age 
    def address(self):
        return self.address

f = student("Raihan",20,'bandung')

print(f.full_name)
print(f.get_age())
print(f.address())
