# This module contains operations related to sets.

def unique_majors(student_list):
    """
    Return a set of unique student majors using set comprehension.
    Extract the major field from each student record.
    stds = [
   (101, "Miles", "Mathematics"),
    (102, "Laura", "Mathematics"),
    (103, "Benji", "Physics"),
    (104, "Natalia", "Physics"),
    (105, "Nadia", "Mathematics"),
]

# the `unique_majors` function should return (in no particular order):

unique_majors(stds)
# => {"Mathematics", "Physics"}
    """
    return {student[2] for student in student_list}
    pass
