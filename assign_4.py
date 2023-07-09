class Loop:
    def loop():
        n1=1
        while n1 == 1:
            print("\n This is menu driven program")
            print("1) For with else \n2) While with else ")
            num=int(input("Enter your choice: "))
            if num == 1:
                c=1
                while c==1:
                    print("For loop with: \n 1) With pass \n 2) With break \n 3) With continue \n 4) With All of them ")
                    num1 = int(input("Enter your choice:"))
                    if num1 ==1:
                        a ="Prathmesh"
                        for i in a:
                            if i=="e":
                             pass
                            else :
                             print(i)
                        else:
                         print("Else statement of for loop")

                    elif num1 == 2:
                        a ="Prathmesh"
                        for i in a:
                            if i=="e":
                             break 
                            else :
                             print(i)
                        else:
                         print("Else statement of for loop")
                    
                    elif num1 == 3:
                        a ="Prathmesh"
                        for i in a:
                            if i=="e":
                             continue
                            else :
                             print(i)
                        else:
                         print("Else statement of for loop")

                    elif num1 == 4:
                        a ="Prathmesh"
                        for i in a:
                            if i=="e":
                             break 
                             continue
                             pass
                            else :
                             print(i)
                        else:
                         print("Else statement of for loop")
                    
                    else:
                       print("You did not enter a valid number \n Going to previous menu...")
                       c=num1
                       

            elif num==2:
                c=1
                while c==1:
                    print("While loop with: \n 1) With pass \n 2) With break \n 3) With continue \n 4) With All of them")
                    num1 = int(input("Enter your choice:"))
                    if num1 ==1:
                        a=1
                        while a<=5:
                            if a==3:
                                pass
                            else:
                                print(a)
                            a+=1
                        else:
                            print("Else statement of while loop")

                    elif num1 == 2:
                        a=1
                        while a<=5:
                            if a==3:
                                break
                            else:
                                print(a)
                            a+=1
                        else:
                            print("Else statement of while loop")
                    
                    elif num1 == 3:
                        a=1
                        while a<=5:
                            if a==3:
                                a+=1
                                continue
                            else:
                                print(a)
                            a+=1
                        else:
                            print("Else statement of while loop")

                    elif num1 == 4:
                        a=1
                        while a<=5:
                            if a==3:
                                break
                                continue
                                pass
                            else:
                                print(a)
                            a+=1
                        else:
                            print("Else statement of while loop")
                    
                    else:
                       print("You did not enter a valid number \n Going to previous menu...")
                       c=num1
                       


            else:
                print("Wrong choice")
            n=input("If you want to continue press 1 \n otherwise press any key ")
            if n!="1":
                print("You choose to exit. Exiting...")
                exit()
            n1=int(n)
            
    
c=Loop
c.loop()

