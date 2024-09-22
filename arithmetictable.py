class maths:
    def __init__(self):
        m=0
        n=0
    def addition(self):   # addition function 
     
        m=int(input('Enter which addition table you want :'))
        n=int(input('Enter how much length you want :'  ))
        self.m=m      # Instance variable 
        self.n=n         # Instance variable 
        print('The addition table for ', self.m, ' is','\n')
        print('******************************')
        for i in range(1,self.n+1):
             print( i ,'+', self.m,' = ', self.m+i)
        print('******************************')
        print('The addition table for ' ,self.m,'is completed ')
        print('******************************')
       
        conn(1)
            
    def substration(self):  #substration function 
        
        m=int(input('Enter which substration table you want :'))
        n=int(input('Enter how much length you want :'  ))
        self.m=m      # Instance variable 
        self.n=n         # Instance variable
        print('The substration table for ', self.m, ' is','\n')
        print('******************************')
        for i in range(1,self.n+1):
           print( self.m ,'-', i,' = ', self.m-i)
        print('******************************')
        print('The substration table for ' ,self.m,'is completed ')
        print('******************************')
        conn(2)
    def multi(self):  # multiplication  function 
        
        m=int(input('Enter  which multiplication table you want :'))
        n=int(input('Enter how much length you want :'  ))
        self.m=m      # Instance variable 
        self.n=n         # Instance variable 
        print('The multiplication table for ', self.m, ' is','\n')
        print('******************************')
        for i in range(1,self.n+1):
           print( i ,' x ', self.m,' = ', self.m*i)
        print('******************************')
        print('The  multiplication  table for ' ,self.m,'is completed ')
        print('******************************')
        conn(3)
    def div(self):  # division  function 
        
        m=int(input('Enter which division table you want :'))
        n=int (input('Enter how much length you want :'  ))
        self.m=m      # Instance variable 
        self.n=n         # Instance variable 
        print('The division table for ', self.m, ' is','\n')
        print('******************************')
        for i in range(1,self.n+1):
           print( i ,' ÷ ', self.m,' = ', round(i/self.m,2))
        print('******************************')
        print('The  division  table for ' ,self.m,'is completed ')
        print('******************************')
        conn(4)
        
def asmd():  # operation selection 
    opp= input("""hint: a-->addition, s -->substration, m-->multiplication, d-->division
    Enter the operation to perform :""")
    if opp == 'a' or opp == 'A':
        math.addition()
    elif opp == 's' or opp =='S':
        math.substration()
    elif opp== 'm' or opp=='M':
        math.multi()
    elif opp == 'd' or opp=='D':
        math.div()
    else:
        print('Invalid input ')

def choice(o):    
    if o=='s' or o=='S':
       asmd()
    elif o=='e' or o=='E':
       print('You ended this program, Thank you ')
    else:
       print('Invalid input ')

def conn(g):               
        h=input("Do you want to continue this with the same operation(y-->yes, a --> i want another operation, e -->exit):")
        if h=='y' or h=='Y':
            if g==1:
                math.addition()
            elif g==2:
                math.substration()
            elif g==3:
                math.multi()
            else :
                math.div()
        elif h=='a' or h== 'A':
            asmd()
        elif h=='e' or h== 'E':
            choice(h)
        else:
             print ('invalid input, please try again')



math=maths()
print('******************************')
o=input("""hint: s -->start ,  e -->end
Enter  the option:""")
print('******************************')
choice(o)
