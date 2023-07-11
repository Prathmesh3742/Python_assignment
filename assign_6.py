def ds(roll_no,name):

    ls =[roll_no,name]
    print(ls)
    ls[0] = input("Enter name to be changed in list :")
    ls[1] = int(input("Enter roll to be changed in list :"))
    print(ls)    

    tup = (roll_no,name)
    print(tup)
    tup = list(tup)
    tup[0] = input("Enter name to be changed in tuple :")
    tup[1] = int(input("Enter roll to be changed in tuple :"))
    tup = tuple(tup)
    print(tup)

    sets = {roll_no,name}
    print(sets)
    name1 = input("Enter name to be changed in set :")
    roll = int(input("Enter roll to be changed in set :"))
    sets = {roll,name1}
    print(sets)

    dictionary = {
        "Name" : name,
        "Roll no" : roll_no
    }
    print(dictionary)
    dictionary["Name"] = input("Enter name to be changed in dictionary :")
    dictionary["Roll no"] = int(input("Enter roll to be changed in dictionary :"))
    print(dictionary)

    del ls,tup,sets,dictionary

ds(36,"Prathmesh")