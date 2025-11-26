import tkinter as tk


class Person:
    def __init__(self, name):
        self.name = name

# 1-2 class Student(Person)
class Student(Person):
    # Person 클래스를 상속받는다 (is-a 관계).
    def __init__(self, name):
        super().__init__(name)
        self.classes = [] # has-a 관계: 수강 과목 리스트

    # enrollCourse(subject): 과목을 리스트에 추가한다. (중복 방지)
    def enrollCourse(self, subject):
        if subject not in self.classes:
            self.classes.append(subject)

    # clearCourses(): 과목 리스트를 초기화한다.
    def clearCourses(self):
        self.classes = []

# 학생 객체 생성
student = Student("홍길동")
COURSES = ["Python", "AI", "DataScience"]

# 2. Tkinter UI 구성
class Problem4App:
    def __init__(self, master):
        master.title("문제 4") # 제목: "문제 4"
        master.geometry("380x280") # 창 크기: 380x280
        
        # 상단 라벨: "학생: 홍길동"
        tk.Label(master, text=f"학생: {student.name}", font=('Arial', 12, 'bold')).pack(pady=10)
        
        # Checkbutton 상태 변수 딕셔너리
        self.check_vars = {}
        
        # Checkbutton 3개
        for course in COURSES:
            var = tk.IntVar() # 체크박스의 상태를 저장할 변수
            self.check_vars[course] = var
            # Checkbutton을 GUI에 표시
            tk.Checkbutton(master, text=course, variable=var).pack(anchor='w', padx=50)

        # 버튼 프레임
        button_frame = tk.Frame(master)
        button_frame.pack(pady=20)

        # "등록하기" 버튼
        tk.Button(button_frame, text="등록하기", command=self.enroll_courses).pack(side=tk.LEFT, padx=10)
        
        # "초기화" 버튼
        tk.Button(button_frame, text="초기화", command=self.clear_selections).pack(side=tk.LEFT, padx=10)
        
        # 하단 라벨: 현재 등록된 과목을 표시
        self.result_label = tk.Label(master, text="과목을 선택하고 [등록하기]를 누르세요.", fg="blue")
        self.result_label.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

    def enroll_courses(self):
        # 등록 버튼 클릭 시 Student 객체의 has-a 리스트(classes)에 반영
        for course, var in self.check_vars.items():
            if var.get() == 1: # 체크된 과목만
                student.enrollCourse(course)
        
        # 결과 Label에 출력
        if student.classes:
            result_text = f"등록된 과목: {', '.join(student.classes)}"
        else:
            result_text = "등록된 과목이 없습니다."
            
        self.result_label.config(text=result_text)

    def clear_selections(self):
        # 과목 리스트를 비움
        student.clearCourses()
        
        # 모든 체크박스를 해제
        for var in self.check_vars.values():
            var.set(0)
        
        # 결과 출력
        self.result_label.config(text="모든 선택을 해제했습니다.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Problem4App(root)
    root.mainloop()