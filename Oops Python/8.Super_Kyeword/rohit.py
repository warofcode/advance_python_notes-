class A:
    home_variable = "i m class home_variable in class A"
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.home_variable = "i m class A inststance home_varialbe"
        self.new_variable = "i m class A new variable"
class B(A):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)
    

