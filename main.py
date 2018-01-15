from source_code import *
ch='I'
while(ch=='I' or ch=='i'):
    print('\nENTER THE NUMBERS SEPARATED BY ","(ENTER WHOLE NUMBERS ONLY)\nEXAMPLE:\u2211-1,2,3,4,5,6')
    x=take_input()
    o=get_order()
    i=1
    while i<=o+1:
        x=combiner(x,i)
        i=i+1
    generatepic()
    y=get_pic()
    print_chart(y)
    s1=1
    s2=0
    while get_totreduc()!=1 and s1!=s2:
        reduce(y)
        s1=get_size(y)
        print("AFTER REDUCTION-")
        print_chart(y)
        c_dom(y)
        print("AFTER APPLYING COLUMN DOMINANCE-")
        print_chart(y)
        r_dom(y)
        print("AFTER APPLYING ROW DOMINANCE-")
        print_chart(y)
        s2=get_size(y)
    print("\nRESULT-")      
    if get_totreduc()==1:    
        get_result()
    else:
        get_result()
        prin()
    ch=input("\nPRESS I or i FOR NEW INPUT OR ANY OTHER KEY FOR EXIT-")    
exit()





    



