skillsAndKnowledge=["Basic Math","Microsoft Excel","Microsoft Word","Customer Service","Retail Operations","Merchandising Procedures","Basic Computer Skills","Writing Reports","Time Management","Interpersonal Communication"]

jobSkills=["Microsoft Excel","Basic Computer Skills","Interpersonal Skills","Writing Reports"]
userSkills=["Basic Math","Merchandising Procedures","Interpersonal Skills"]

def checkSkills(userSkills,jobSkills):
  completedSkills=[]
  incompleteSkills=[]


  for jobSkill in jobSkills:
    if jobSkill in userSkills:
      completedSkills.append(jobSkill)
    else:
      incompleteSkills.append(jobSkill)
  return [completedSkills,incompleteSkills]
  
  jobSkills=["Microsoft Excel","Basic Computer Skills","Interpersonal Skills","Writing Reports"]
userSkills=["Basic Math","Merchandising Procedures","Interpersonal Skills"]

checkSkills(userSkills,jobSkills)
