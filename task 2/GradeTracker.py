from Student import Student
import pickle
from Term import Term


class GPATracker:
    def __init__(self, student: Student):
        self._student = student

    def _calculate_current_term_GPA(self):
        term = self._student.get_current_term()
        grades_list = [4, 4, 3.7, 3.3, 3, 2.7, 2.3, 2, 1.7, 1.3, 1, 0]
        credit_hrs_sum = 0
        honor_points_sum = 0
        for subject, grade in term.get_subjects().items():
            honor_points = grade.value * subject.get_credit_hours()
            credit_hrs_sum += subject.get_credit_hours()
            honor_points_sum += honor_points
        term_GPA = float("{:.2f}".format(honor_points_sum / credit_hrs_sum))
        self._student.get_current_term().set_term_GPA(term_GPA)
        return term_GPA

    def add_term(self, new_term: Term):
        # append term list
        self._student.append_term_list(new_term)
        for subject in new_term.get_subjects().keys():
            self._student.increment_total_credit_hrs(subject.get_credit_hours())
        # incrememnt term num
        self._student.increment_current_term_number()
        self._calculate_current_term_GPA()
        self._student.set_cgpa(self._calculate_cgpa())
        self.save_data()

    def _calculate_cgpa(self):
        total_credit_hours = self._student.get_total_credit_hours()
        total_honor_points = 0
        for term in self._student.get_term_list():
            total_honor_points += term.get_term_credit_hrs()/term.get_term_GPA()
        cgpa = float("{:.2f}".format(total_credit_hours / total_honor_points))

        return cgpa

    def save_data(self):
        try:
            with open(f"{self._student.get_student_information()}.pickle", "wb") as f:
                pickle.dump(self._student, f, protocol=pickle.HIGHEST_PROTOCOL)
        except Exception as ex:
            print("Error during pickling object (Possibly unsupported):", ex)


    def get_student_CGPA(self):
        return self._student.get_CGPA()

    def get_student_current_term_GPA(self):
        return self._student.get_current_term().get_term_GPA()

    def print_student_details(self):
        print(self._student)