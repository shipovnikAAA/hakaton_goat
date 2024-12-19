
import time
import random

import db

#questions = list(db.get_questions())[0][1]

def GetPlayer(login, password):
    prec = list(db.get_player(login, password))[0][1]
    if prec['data'] == []:
        return False
    else:
        return prec['data']


def AddPlayer(login, name, password):
    db.add_player(login, name, 0, password)


def ChangeRaiting(login, raiting):
    db.update_rating(raiting, login)


def GetQuestion(number):
    questions = list(db.get_questions())[0][1]
    return questions[number]


def ChangeQuestion():
    questions = list(db.get_questions())[0][1]
    return questions[-1]


def FiftyFifty(number):
    questions = list(db.get_questions())[0][1]
    return questions[number]['correct'], ((questions[number]['correct'] + 1) % 4) + 1


def spectators(n = 1):
    n -= 1
    random.seed(time.time())
    correct = n
    variants = []
    for i in range(4):
        if i != n:
            variants.append(i)
    uncorrect = variants[random.randint(0, 2)]
    ans = []
    lst = 0
    for i in range(3):
        ans.append(random.randint(0, 100 - lst))
        lst += ans[i]
    ans.append(100 - lst)
    ans.sort()
    out = [0, 0, 0, 0]
    if random.randint(0, 100) > 10:
        out[correct] = ans[-1]
        out[uncorrect] = ans[-2]
    else:
        out[uncorrect] = ans[-1]
        out[correct] = ans[-2]
    ind = 0
    for i in range(4):
        if i != correct and i != uncorrect:
            out[i] = ans[ind]
            ind += 1
    return out
