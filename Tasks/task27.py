voter=[]
vote_cnt={}
n=int(input("Enter no of votes :"))

for i in range(n):
    names=input("Enter Voter Name : ")
    voter.append(names)


    if names in vote_cnt:
        vote_cnt[names] +=1
    else:
        vote_cnt[names] =1

print(f"Voter counts:{vote_cnt}")

fraud=[]
print(f"People who voted more than once:")
for names, cnt in vote_cnt.items():
   if cnt > 1 :
      fraud.append(names)
print(fraud)
      
unique=set(voter)
print(f"Total unique voters:{len(unique)}")
