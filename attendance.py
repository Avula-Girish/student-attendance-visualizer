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
subject_wise_attendence=[]
rollno_subjectwise_data=[]
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
    subject_wise_attendence.append(present)
    for k in present:
        total_present.append(k)
total_present.sort()
attendence_count=[]

for i in class_rollno:
    attendence_count.append(total_present.count(i))
print(attendence_count)
print("1. Full class data\n2. individual student data")
ans=int(input("enter your choice: "))
if(ans==1):
    plt.figure(figsize=(15,5))
    plt.bar(class_rollno,attendence_count,color='skyblue',edgecolor="black")
    plt.title("Total class attendence data")
    plt.xlabel(f"Roll no\nSEC: {sec}")
    plt.ylabel("No of classes")
    plt.grid(axis='y')
    plt.xticks(class_rollno,rotation=90)
    plt.ylim(0,periods)
    plt.show()
elif(ans==2):
    num=int(input("enter roll no: "))
    for i in range(len(subjects)):
        c= subject_wise_attendence[i].count(num)
        if(c>0):
            rollno_subjectwise_data.append(1)
        else:
            rollno_subjectwise_data.append(0)
    print(rollno_subjectwise_data)
    p=rollno_subjectwise_data.count(1)
    ab=rollno_subjectwise_data.count(0)

    plt.pie([p,ab],labels=["PRESENT","ABSENT"],colors=['green','red'],autopct="%1.1f%%",startangle=90,wedgeprops={'width':0.4})
    plt.title(f"Attendance of Roll No {num}")
    plt.show()
        