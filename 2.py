class computer:
    def __init__(self,cpu,name):
        self.cpu=cpu
        self.name=name
    def config(self):
        print('the config is :',self.cpu,self.name)
    def name1(self):
        print('the name is :',self.name)
com1=computer('i7','game1')
com2=computer('ryzen7','game2')
com1.config()
com2.name1()