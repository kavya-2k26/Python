class multiple(): 
    def Subfields():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")

    def oddEven():
            num = int(input("Enter a Number:"))
            if num % 2 == 0:
                print(num,"is Even number")
            else:
                print(num,"is Odd number")

    def Elegible():
            Gender = input("Your Gender:")
            Age = int(input("Your Age:"))
            
            if Gender == 'Male' and Age >= 21:
                print("Eligible")
            elif Gender == 'Female' and Age >= 18:
                print("Eligible")
            else:
                print("Not Eligible")                

    def percentage():
            s1 = 98
            print("Subject1:",s1)
            s2 = 87
            print("Subject2:",s2)
            s3 = 95
            print("Subject3:",s3)
            s4 = 95
            print("Subject4:",s4)
            s5 = 93
            print("Subject5:",s5)
            
            Total = s1 + s2 + s3 + s4 + s5
            print("Total", Total)
            
            Percentage = Total / 500 * 100
            print("Percentage:", Percentage)

    def triangle():
            Height = int(input("Height:"))
            Breadth = int(input("Breadth:"))
            print("Area formula: (Height*Breadth)/2")
            Area = (Height * Breadth) / 2
            print("Area of Triangle:", Area)
        
            # Perimeter calculation
            Height1 = int(input("Height1:"))
            Height2 = int(input("Height2:"))
            Breadth = int(input("Breadth:"))
            print("Perimeter formula: Height1 + Height2 + Breadth")
            Perimeter = Height1 + Height2 + Breadth
            print("Perimeter of Triangle:", Perimeter)
        