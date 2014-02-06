from random import randint
replay = "YES"
while replay == "YES":
    current=0
    i=1
    times=[]
    wegood = "NO"
    understand = "NO"
    while len(times) < 12:
        temp=randint(1,12)
        #print("DEBUG - " + temp)
        if temp not in times:
            #print("DEBUG - Adding")
            times.append(temp)
            i=i+1
            #print("DEBUG - " + times)
        #else:
            #print("DEBUG - Already got that!")
            #print("DEBUG - " + times)
    #print("DEBUG - FINAL LIST: " + times)
    table = raw_input("Enter the times table you want to learn/practice: ")

    while len(times)>0:
        while wegood == "NO":
            ans = raw_input("What is " + str(times[current]) + " times " + str(table) + "? ")
            try:
                int(ans)
            except ValueError:
                print("Please just enter whole numbers ;) \n")
            else:
                wegood = "YES"

        wegood = "NO"
        #print("DEBUG - ACTUAL ANSWER: " + str(int(times[current])*int(table)))
        #print("DEBUG - USER ANSWER: " + ans)

        if str(ans) == str(int(times[current])*int(table)):
            print("CORRECT :) \n")
            del times[current]
        else:
            print("Nearly :( \n")
    print("We're done - GREAT JOB! \n")
    while understand == "NO":
        replay = raw_input("Do you want to learn again? Yes/No answer ;) ")
        replay = replay.upper()
        if replay == "NO":
            print("Awww, OK then.")
            understand = "YES"
        elif replay == "YES":
            print("Let's play again! \n")
            understand = "YES"
        else:
            print("Not sure what you mean :S \n")
            understand = "NO"

