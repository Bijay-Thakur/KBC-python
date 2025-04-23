# we are going to make KBC program here
print("Hello, We are playing KBC here!!!!!\n")


def KBCprogram(name):
    Questions=[
           "1.Who is current president of USA?\n",
               "2.What is full form of WHO?",
               "3.What is the capital city of Bhutan?",
               "4.Who is the current CEO of google?",
               "5.What is the radius of Earth in kilometer?"]
    
    Answers=[
             "Donald Trump",
             "World Health Organization",
             "Thimpu",
             "Sundar Pichai",
             "6400"]
    count=0
    for i in range(len(Questions)):
        print(Questions[i])
        ans=str(input("Answer: "))
        
    
        if ans.lower()==Answers[i].lower():
            print("Correct!!!!")
            
            count=count+1
            print("Money won= ",count*20000)
        else: 
             print("Oopss!! Wrong answer. Game over")
             break
    moneyWon=count*20000
    print("Total money won=",moneyWon)

name=str(input("Enter your name:\n"))
print("Welcome",name,"I will be your host for our KBC round\n")
KBCprogram(name)