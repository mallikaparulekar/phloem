 ##Connecting to what we learned in the backend tutorial to python
import sqlite3

def init_course_objs(sqlLink):
    courseArr = []
    conn = sqlite3.connect(sqlLink)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM courses")
    rows = cursor.fetchall()
    for i in range(len(rows)):
        row = rows[i]
        course = Course(row)
        courseArr.append(course)
    return courseArr



class Course:
    def __init__(self, row):
        self.name = row[0]
        self.link = row[1]
        self.platform = row[2]
        self.rating = row[3]
        self.captions = row[4]
        self.interactive = row[5]
        self.averageLectureLength = row[6]
        self.skill = row[7]


    def get_Name(self):
        return self.name

    def get_Skill(self):
        return self.skill

    def get_Platform(self):
        return self.platform

    def get_Link(self):
        return self.link

def init_job_objs(sqlLink):
    jobArr = []
    conn = sqlite3.connect(sqlLink)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jobs")
    rows = cursor.fetchall()
    for i in range(len(rows)):
        row = rows[i]
        job = Job(row)
        jobArr.append(job)
    return jobArr

def string_to_arr_comma_delim(strng):
    arr = []
    word = ""
    #adding skipNext to get the string to skip over the character after the comma, which would be a space
    skipNext = False
    for i in range(len(strng)):
        char = strng[i]
        if(char != "," and skipNext == False):
            word = word+char
        elif(char == ","):
            arr.append(word)
            word = ""
            skipNext = True

        #moves the skip Next back to false after successfully skipping the space
        if(skipNext == True and char == " "):
            skipNext = False

    #adding the last word, which may or may not have a comma at the end (either work)
    if(word != ""):
        arr.append(word)
    return arr

class Job:
    def __init__(self, row):
        self.company = row[0]
        self.title = row[1]
        self.summary = row[2]
        self.hours = row[3]
        #separate out skills into an array, instead of one piece of text
        self.skills = string_to_arr_comma_delim(row[4])
        self.location = row[5]
        self.link = row[6]
        self.degree = row[7]
        self.salary = row[8]
        self.benefits = row[9]
        #skip id
        self.field = row[11]


    def get_Title(self):
        return self.title

    def get_Skills(self):
        return self.skills

    def get_Field(self):
        return self.field

    def get_Company(self):
        return self.company

def init_user(sqlLink):
    conn = sqlite3.connect(sqlLink)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    row = cursor.fetchall()
    #print("row", row)
    user = User(row[0])
    return user


class User:
    def __init__(self, row):
        self.name = row[0]
        self.email= row[1]
        self.password = row[2]
        self.skills = string_to_arr_comma_delim(row[3])
        self.pref_state = row[4]
        self.pref_field = row[5]

    def get_Name(self):
        return self.name

    def get_Skills(self):
        return self.skills

    def get_pref_Field(self):
        return self.pref_field




#courseArr = init_course_objs(sqlLink)
'''
for i in range(len(courseArr)):
    print(courseArr[i].get_Skills())
'''

#jobArr = init_job_objs(sqlLink)
'''
for i in range(len(jobArr)):
    print(jobArr[i].get_Skills())
'''
#user = init_user(sqlLink)
'''
print(user.get_Name())
print(user.get_pref_Field())
print(user.get_Skills())
'''

def refine_jobs_field(user, jobArr):
    #returs a list of jobs that satisfy the users choice of field. If the user is ambivalent, simply returns the original job array
    #i.e. if the user selects a field they want to transition to, only pic jobs from those fields
    if(user.get_pref_Field()!= ''):
        userField = user.get_pref_Field()
        selected_job_arr = []
        for i in range(len(jobArr)):
            if(userField == jobArr[i].get_Field()):
                selected_job_arr.append(jobArr[i])
    else:
        selected_job_arr = jobArr

    return selected_job_arr


def find_missing_skills(user, job):
    #using dictionary to keep o(n) runtime
    userSkills = user.get_Skills()
    dict = {}
    for i in range (len(userSkills)):
        dict[userSkills[i]]= "present"
    missing_skills= []
    jobSkills = job.get_Skills()
    for i in range(len(jobSkills)):
        if(jobSkills[i] not in dict.keys()):
            missing_skills.append(jobSkills[i])
    return missing_skills

#print(find_missing_skills(user, refine_jobs_field(user, jobArr)[0]))


def course_recommendations(missing_skills, courseArr):
    dict = {}
    for i in range(len(missing_skills)):
        dict[missing_skills[i]] = "missing"
    relevantCourses = []
    for i in range(len(courseArr)):
        if(courseArr[i].get_Skill() in dict.keys()):
            relevantCourses.append(courseArr[i])
    return relevantCourses

def separateMissingSkills(relevantCourses):
    #print("len", len(relevantCourses))
    coursesOne = []
    coursesTwo = []
    skillStart = relevantCourses[0].get_Skill()
    currentSkill = relevantCourses[0].get_Skill()
    i = 0
    while(currentSkill == skillStart):
        #print(relevantCourses[i].get_Name())
        coursesOne.append(relevantCourses[i])
        #print("i","courseOne", i)
        i +=1
        currentSkill = relevantCourses[i].get_Skill()



    #adding remaining to other
    while(i < len(relevantCourses)):
        coursesTwo.append(relevantCourses[i])
        #print("i","courseTwo", i)
        i +=1
    return coursesOne, coursesTwo



def sort_course_rec_by(sepRelevantCourses, factor):
    if(factor == "captions"):
        return sorted(sepRelevantCourses, key=lambda course: course.captions, reverse = True)

    elif(factor == "interactive"):
        return sorted(sepRelevantCourses, key=lambda course: course.interactive, reverse = True)

    elif(factor == "averageVideoLength"):
        return sorted(sepRelevantCourses, key=lambda course: course.averageLectureLength)





def print_courses(courseArr, factor = None):
    return_statement = "These are the courses we recommend to learn {}: ".format(courseArr[0].get_Skill()) + "\n"
    for i in range(len(courseArr)):
        return_statement +=  '{} at {}'.format(courseArr[i].get_Name(), courseArr[i].get_Link()  + "\n")

    if(factor == "captions"):
        return_statement += ( "Sorted by presence of captions as requested, with top courses having captions"+ "\n")

    elif(factor == "averageVideoLength"):
        return_statement += ("Sorted by average video length as requested, with top courses having the lowest average length"+ "\n")

    elif(factor == "interactive"):
        return_statement += ( "Sorted by presence of captions as requested, with top courses being more interactive"+ "\n")
    return return_statement



##TESTING THE SELECTION
#courseArr = init_course_objs(sqlLink)
#jobArr = init_job_objs(sqlLink)
#user = init_user(sqlLink)
#selected_job_arr = refine_jobs_field(user, jobArr)
#modify for if more than one in selected_job_arr
#missing_skills = find_missing_skills(user, selected_job_arr[0])
#relevantCourses = course_recommendations(missing_skills, courseArr)
#print_courses(relevantCourses)
#print("")
#sorted_courses = sort_course_rec_by(relevantCourses, "interactive")
#print_courses(sorted_courses, factor = "interactive")



sqlLink = '/Users/mallika/Downloads/jobs.db'
def execute_and_send_to_html(sqlLink):
    conn = sqlite3.connect('/Users/mallika/Downloads/jobs.db')
    cursor = conn.cursor()
    courseArr = init_course_objs(sqlLink)
    jobArr = init_job_objs(sqlLink)
    user = init_user(sqlLink)
    hello_msg = "Hello {}!".format(user.get_Name())
    selected_job_arr = refine_jobs_field(user, jobArr)
    recommended_job_msg = selected_job_arr[0].get_Title()
    missing_skills = find_missing_skills(user, selected_job_arr[0])
    skills_to_catch_msg = missing_skills
    relevantCourses = course_recommendations(missing_skills, courseArr)
    coursesOne, coursesTwo = separateMissingSkills(relevantCourses)
    courseOne_msg = print_courses(sort_course_rec_by(coursesOne, "interactive"), "interactive")
    courseTwo_msg = print_courses(sort_course_rec_by(coursesTwo, "averageVideoLength"), "averageVideoLength")
    #cursor.execute('''INSERT INTO results ('Hello', 'Recommended Job', 'Skills to Catch Up', 'Course Recs for Skill 1', 'Course Recs for Skill 2') VALUES (?, ?, ?, ?, ?)''', (str(hello_msg), str(recommended_job_msg), str(skills_to_catch_msg), str(courseOne_msg) ,str(courseTwo_msg)))
    conn.commit()
    cursor.close()


execute_and_send_to_html(sqlLink)
















#def recommend_courses_for_job(user, job, courseArr):


#print(string_to_arr_comma_delim("Track Wise, Microsoft Project, Microsoft Excel, Microsoft Word, Empower, LabWare, Analytical Skills, Writing (Documentation), Problem Solving"))



'''
#printing a specific data point of each row, say everyone's name. My users table is the one from the workshop, which has name age height weight etc
cursor.execute("SELECT name FROM users")
#fetchall returns a tuple
names = cursor.fetchall()
for name in names:
    #the reason I print name[0] instead of just name is that name is a tuple, and we really only want the first string
    print(name[0])
'''



'''
class Course:
    courseName = None
    link = None
    platform = None
    skillsTaughtArr = []
    captions = False

    def __init__(self, courseName, link, platform , courseRating = None, skillsTaughtArr = [], captions = False, interactive = False, averageLectureLength = None):
        self.skillsTaughtArr = skillsTaughtArr
        self.courseName = courseName
        self.link = link
        self.platform = platform
        self.courseRating = courseRating
        #default caption if no arg given (so false) is set as the captions. unless platform is coursera (where it has captions in all primary languages)
        if(self.platform == "Coursera"):
            self.captions = True
        else:
            self.captions = captions
        self.interactive = interactive
        self.averageLectureLength = averageLectureLength


    def addSkill(self, skill):
        self.skillsTaughtArr.append(skill)



#test case
#name the course variable with course Name--standardized way to shorten--and just use a get name??
#implement a sort by course rating

excelSkillsforBusinessSpecialization = Course("excelSkillsforBusinessSpecialization", "https://www.coursera.org/specializations/excel","Coursera", 4.8,
                                              skillsTaughtArr= ["Data Validation", "Microsoft Excel", "Microsoft Excel Macro", "Pivot Table", "Graphs",
                                                                "Spreadsheet", "Chart", "Concatenation", "Spreadsheet", "Chart","Concatenation", "Consolization",
                                                                "Pivot Chart", "Lookup Table","Microsoft Excel Vba"])




'''









