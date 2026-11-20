from .grades import Avg

def status(grades):
    if Avg(grades)>10:
        return "Accepted"
    else:
        return "Rejected"
