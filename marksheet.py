sub1=int(input("enter sub1 marks="))
sub2=int(input("enter sub2 marks="))
sub3=int(input("enter sub3 marks="))
sub4=int(input("enter sub4 marks="))

if(sub1>=33 and sub2>=33 and sub3>=33 and sub4>=33):
    total_marks=sub1+sub2+sub3+sub4
    print(total_marks)
    percentage=(sub1+sub2+sub3+sub4)/4
    print(percentage)
    print("congrulations you are pass")
else:
    total_marks=sub1+sub2+sub3+sub4
    print(total_marks)
    percentage=(sub1+sub2+sub3+sub4)/4
    print(percentage) 
    print("bad luck but you fail")   

