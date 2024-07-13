def election(votes):
    ones=[i for i, val in votes.items() if val ==1]
    zeroes=[i for i, val in votes.items() if val ==0]

    if len(ones) > len(zeroes):
        print("1")
        print(" ".join(sorted(ones)))


    elif len(zeroes) > len(ones):
        print("0")
        print(" ".join(sorted(zeroes)))

        
    else:
        print("1")
        print(" ".join(sorted(ones)))
        print("0")
        print(" ".join(sorted(zeroes)))

votes_of_election={}        

num_of_ep=int(input("Enter number of people "))

for _ in range(num_of_ep):
    Name=input("Enter name: ")
    vote=int(input("Enter vote: [1>>>yes ,  0>>>no] "))
    votes_of_election[Name]=vote



election(votes_of_election)