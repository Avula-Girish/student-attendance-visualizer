import matplotlib.pyplot as plt

print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("\n🎓GIT🏫\n")
print("____________________________________________________________________________________________________________________________________________________________________")
print("\nGirish Institute of Technology\n")
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

sec=input("Enter SEC: ").upper()
class_stating,class_ending=map(int,input("Enter roll no range (ex: 1-100): ").split("-"))
class_rollno=[]
subjects=[]
total_present=[]
for i in range(class_stating,class_ending+1):
    class_rollno.append(i)
periods=int(input("Enter how many peroids : "))
for i in range(0,periods):
    class_rollno_temp=class_rollno.copy()
    print("period :",i+1)
    subjects.append(input("Enter your subject : "))

    key=input("What you want to enter (Enter 'p' for presentes and any key for absentees) : ").upper()
    if key =='P':
        print("Enter presentees with spaces")
        present=list(map(int,input().split()))
    else:
        print("Enter absentees with spaces")
        absent=list(map(int,input().split()))
        for j in absent:
            try:
                class_rollno_temp.remove(j)
                present=class_rollno_temp
            except ValueError:
                pass
    for k in present:
        total_present.append(k)
total_present.sort()
attendence_count=[]

for i in class_rollno:
    attendence_count.append(total_present.count(i))
print(attendence_count)
plt.figure(figsize=(15,5))
plt.bar(class_rollno,attendence_count,color='skyblue',edgecolor="black")
plt.title("Total class attendence data")
plt.xlabel(f"Roll no\nSEC: {sec}")
plt.ylabel("No of classes")
plt.grid(axis='y')
plt.xticks(class_rollno,rotation=90)

plt.ylim(0,periods)
plt.show()

    
