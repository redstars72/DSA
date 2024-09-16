class Utensil:
    #constructor
    #instance variables
    def __init__(self,Material,Colour,Shape,Capacity):
        self.material=Material
        self.colour=Colour
        self.shape=Shape
        self.capacity=Capacity
    def fill(self,quantity,action_failed_statement,action_complete_statement):
        if self.capacity==None or self.capacity<quantity:
            print(action_complete_statement)
        else:
            print(action_failed_statement)
            self.capacity=self.capacity-quantity
    def full(self,action_failed_statement,action_complete_statement):
        if self.capacity==0:
            print(action_complete_statement)
        else:
            print(action_failed_statement)

#create objects

fork=Utensil("metal","grey","handle tipped with multiple sharp tips",None)
print(fork.material,fork.colour,fork.shape)
fork.fill(10,"not filled","filled")

knife=Utensil("plastic","white","handle with a serrated edge on one side near the tip",None)
print(knife.material,knife.colour,knife.shape)
knife.fill(99999999,"not filled","filled")

bowl=Utensil("porcelain","white","hollow semisphere with a flat base for stability",700)
print(bowl.material,bowl.colour,bowl.shape,bowl.capacity)
bowl.fill(375,"not filled","filled")
print(bowl.capacity)
bowl.full("not full","full")
bowl.fill(325,"not filled","filled")
bowl.full("not full","full")