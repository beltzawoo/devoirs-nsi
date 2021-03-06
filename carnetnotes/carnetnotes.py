from typing import List


def create_grades() -> List[float]:
    return []


def create_weights() -> List[float]:
    return []


def add_grade(grades: List, weights: List, grade: float, weight=1.0):
    return grades.append(grade), weights.append(weight)


def edit_grade(grades: List, rank: int, new_grade: float):
    try:
        grades[rank] = new_grade
        return grades
    except IndexError:
        print("Il n'y a pas de note à ce rang, impossible à modifier")


def edit_weight(weights: List, rank: int, new_weight: float):
    try:
        weights[rank] = new_weight
        return weights
    except IndexError:
        print("Il n'y a pas de coeff à ce rang, impossible de modifier")


def remove_grade(grades: List, weights: List, rank: int):
    try:
        grades.pop(rank)
        weights.pop(rank)
    except IndexError:
        print("Il n'y a pas de notes à ce rang !")


def get_average(grades: List, weights: List):
    numerateur = 0
    rank = 0
    for grade in grades:
        numerateur += grade * weights[rank]
        rank += 1
    try:
        average = numerateur / sum(weights)
    except ZeroDivisionError:
        average = "Il n'y a pas de notes, impossible de donner la moyenne !"
    return average


def count_grades(grades: List, threshold=10.0) -> int:
    grades_counted = 0
    for grade in grades:
        if grade < 10:
            grades_counted += 1
    return grades_counted


def delete_list(list_name: str):
    del globals()[list_name]


def give_mentions(grades: List[float]):
    mentions = []
    for grade in grades:
        if grade >= 16.0:
            mentions.append("TB")
        elif grade >= 14.0:
            mentions.append("B")
        elif grade >= 12.0:
            mentions.append("AB")
        else:
            mentions.append("Aucune")
    return mentions


def give_color(grades: List[float], weights: List[float]) -> str:
    average = get_average(grades, weights)
    red_hex = "#FF0000"
    orange_hex = "#FFA500"
    blue_hex = "#008BFF"
    green_hex = "#008000"
    if average < 10:
        return red_hex
    elif average < 12:
        return orange_hex
    elif average < 14:
        return blue_hex
    else:
        return green_hex


def save_list():
    pass


def save_everything(grades, weights):
    save_list(grades)
    save_list(weights)
