import view
main_dct = {}
student_name = []
lesson = []

def start():
    while True:
        op = view.get_op()

        if op == 1:
            student = view.add_student()
            main_dct[student]={}
            student_name.append(student)
            if lesson:
                for less in lesson:
                    main_dct[student][lesson] = {}
        if op == 2:
            lesson.append(less)
            less = view.add_lesson()
            for name in  student_name:
                main_dct[name][lesson] ={}
        if op == 3:
            name, less, mark = view.imput_mark()
            main_dct[name][lesson].append(mark)
        
        if op == 4:
            print(main_dct)
        
        if op == 5:
            name = view.get_name_and_mark()
            print(f"Оценка: {name} - {main_dct[name]}")

        if op == 6:
            break
        print(main_dct)
    
