# eligible_for_vote name ka function likho jo ki user ko bataye ki vo (he/she) vote de sakta hai ya nahi.
# ( Consider minimum age of voting to be 18. ) Example:- Agar user input me 18 se kam deta hai to “not eligible “ print kare aur agar user 18 ya 18 se jyaada input kare to “you are eligible” print kare. Input:- Output :-


def eligible_for_vote(num,num2):
    if num=="she" and num=="he":
        print("Okey")
    if num2>=18:
        print("You are eligible")
    else:
        print("Not eligible")
a=input("enter your gender:")
b=int(input("enter you age:")) 
eligible_for_vote(a,b)           

