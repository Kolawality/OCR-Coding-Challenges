import random
from csv import writer


def append_list_as_row(file_name, list_of_elem):
    """
    Appends the students details to a new line in the csv file
    """
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_write = writer(write_obj)#
        # Add contents of list as last row in the csv file
        csv_write.writerow(list_of_elem)


# Class to create the per student object
class StudentQuiz:
    def __init__(self, name, class_group, total=0):
        self.name = name
        self.class_group = class_group
        self.total = total

    def take_test(self):
        """
        This function starts the tests for the student (object)
        """
        arithmetic_operators = ['+', '-', '*', '/']

        total = 0

        for x in range(3):
            num_1 = str(random.randint(0, 9))
            num_2 = str(random.randint(1, 9))

            operator = random.choice(arithmetic_operators)

            equation = [num_1, operator, num_2]

            result = ''.join(equation)
            print(equation)
            print()
            answer = input("What's the answer?: ")
            if float(answer) == round(eval(result), 2):
                print("That's correct")
                total += 1
            else:
                print("That's incorrect the correct answer is {}"
                      .format(round(eval(result), 2)))

        print("You scored {} out of 10".format(total))

        self.total = total

        return self.total

    def student_entry(self):
        """
        This function determines the amount of tests taken and then adds
        them to the csv file using the append_list_as_rows function
        """
        student_results = []

        for i in range(3):
            score = self.take_test()
            student_results.append(score)
            print()
            print(self.name)
            print(self.total)

        print("{} scores are {}".format(self.name, student_results))

        entry = [self.name, self.class_group]

        for i in range(len(student_results)):
            entry.append(student_results[i])

        append_list_as_row('student scores.csv', entry)
