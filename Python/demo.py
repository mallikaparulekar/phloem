#PAUSE BETWEEN PRINT
import time
import masterCode
import sqlite3

name = input("Please enter your name")
print("")

print("please wait while we load your info from the database...")
time.sleep(2)
print("")

sqlLink = ('/Users/mallika/Downloads/jobs.db')
conn = sqlite3.connect(sqlLink)
cursor = conn.cursor()
courseArr = masterCode.init_course_objs(sqlLink)
jobArr = masterCode.init_job_objs(sqlLink)
user = masterCode.init_user(sqlLink)
selected_job_arr = masterCode.refine_jobs_field(user, jobArr)
missing_skills = masterCode.find_missing_skills(user, selected_job_arr[0])
relevantCourses = masterCode.course_recommendations(missing_skills, courseArr)
coursesOne, coursesTwo = masterCode.separateMissingSkills(relevantCourses)
courseOne_msg = masterCode.print_courses(masterCode.sort_course_rec_by(coursesOne, "interactive"), "interactive")
courseTwo_msg = masterCode.print_courses(masterCode.sort_course_rec_by(coursesTwo, "averageVideoLength"), "averageVideoLength")

print("It appears that you are interested in the {} industry ".format(user.get_pref_Field()) + "and your skills are:")
for i in range(len(user.get_Skills())):
    if(i == len(user.get_Skills())-1):
        print(user.get_Skills()[i])
    else:
        print(user.get_Skills()[i], end = ", ")

print("")
response = input("Hmmm a good fit job for you might be as an {} at {}, are you interested?".format(selected_job_arr[0].get_Title(),selected_job_arr[0].get_Company()))
if response == "No":
    print("finding next role...")
else:
    print("")
    print("You do have to catch up on a few skills, namely:")
    for i in range(len(missing_skills)):
        if(i == len(missing_skills)-1):
            print(missing_skills[i])
        else:
            print(missing_skills[i], end = ", ")
    time.sleep(2)
    print("")
    print("Don't worry though!")
    print( "Here are some good and free online courses, ordered based on whether they have interactive quizzes/video length (as you requested)")
    time.sleep(2)
    print("")
    print(courseOne_msg)
    print("")
    print(courseTwo_msg)
