class Course:
    courseName = None
    link = None
    platform = None
    skillsTaughtArr = []
    captions = False

    def __init__(self, courseName, link, platform, courseRating, skillsTaughtArr = [], captions = False):
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


    def addSkill(self, skill):
        self.skillsTaughtArr.append(skill)



#test case
#name the course variable with course Name--standardized way to shorten--and just use a get name??
#implement a sort by course rating
excelSkillsforBusinessSpecialization = Course("excelSkillsforBusinessSpecialization", "https://www.coursera.org/specializations/excel","Coursera", 4.8,
                                              skillsTaughtArr= ["Data Validation", "Microsoft Excel", "Microsoft Excel Macro", "Pivot Table", "Graphs",
                                                                "Spreadsheet", "Chart", "Concatenation", "Spreadsheet", "Chart","Concatenation", "Consolization",
                                                                "Pivot Chart", "Lookup Table","Microsoft Excel Vba"])





