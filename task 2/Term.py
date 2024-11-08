from Subject import Subject
from typing import Dict
from Grades import Grade


class Term:

    def __init__(self, subj_dict: Dict[Subject, Grade]):
        self._subjects: Dict[Subject, Grade] = subj_dict
        self._term_credit_hrs = 0
        for subject in self._subjects.keys():
            self._term_credit_hrs += subject.get_credit_hours()
        self._term_GPA = 4

    def get_term_credit_hrs(self):
        return self._term_credit_hrs

    def get_subjects(self) -> Dict[Subject, Grade]:
        return self._subjects

    def set_term_GPA(self, GPA: float):
        self._term_GPA = GPA

    def get_term_GPA(self):
        return self._term_GPA

    # need improve
    def __repr__(self):
        termstr = ""

        for subject, grade in self._subjects.items():
            termstr += f"{subject}: {grade} \n"
        return termstr
