class Student:
    def __init__(self,name, hometown, age, height, favorite_icecream):

        self.name=name
        self.hometown=hometown
        self.age=age
        self.height=height
        self.favorite_icecream=favorite_icecream

    
    def print_summary (self):
        print (' my name is '+self.name + ' I live in '+self.hometown +' I am ' +str(self.age) + ' years old '+' my hight is '+str(self.height) +' meters '+ ' my favorite icecream is ' + self.favorite_icecream)

    #def get_giraffe_gap()
       #return(500-self.height)
    
