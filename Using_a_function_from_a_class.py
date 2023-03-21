class my_class:
    def cat_laugh(self):
        print("The cat laught")
    
    def dog_laugh(self):
        print("The dog laugh")

a = int(input("Enter 1 for dog laugh 2 for cat laugh"))

output=my_class()

if a ==1:
    print(output.cat_laugh())
elif a== 2:
    print(output.dog_laugh())