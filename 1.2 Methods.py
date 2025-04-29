#def pas():
#    print('pass')
#    return 'semester done'

class Student :
    id=113
    cgpa=3.91
    name='Ira'
    activity=['sleep','eat','play']

    def __str__(self):
        return f"Student(id={self.id}, cgpa={self.cgpa}, name='{self.name}', activity={self.activity})"

    def pas(self):
        print('pass all subjects')

    def result(self,sub,mark):
        text=f'subject :{sub}mark : {mark}'
        return text
    
s1 = Student()
print(s1)
print(s1.name)
s1.pas()
a=s1.result('english',98)
print(a)
