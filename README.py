class Person:

    def __init__(self):
        self.name = 'Zakhele Ndlovu'
        self.age = 24
        self.qualification = 'Marketing Management'
        self.languages_spoken = ['IsiZulu','English','IsiXhosa','Pedi','Setswana','Swati']
	self.tools = ['Python','Html & CSS','Javascript','MySQL','Salesforce']

    def getName(self):
        name=self.name
        return name

    def getAge(self):
        age = self.age
        return age

    def getQualification(self):
        qual = self.qualification
        return qual

    def getLaguagesSpoken(self):
        ls = self.languages_spoken
        return ls

    def thankYou(self):
	print('Thanks for dropping by! :)')

 me = Me()
 me.thanYou()
