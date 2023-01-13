def setExtraction(fin):
    res = []
    word = ''
    temp = []
    for sub in fin:
        res.append(sub.replace("\n", " "))
    for i in res:
        if i != ' ':
            word += i
        elif i == ' ':
            temp.append(word)
            word = ''
    qs = []
    question = ''
    qn = []
    TotalQuestions = 150
    for i in range(0, TotalQuestions):
        qn.append(((str(i + 1) + '.')))
    k = 0
    for i in range(0, len(temp)):
        if (temp[i] == qn[k]):
            qs.append(question)
            k += 1
            question = ''
        else:
            question += (str((temp[i] + ' ')))
    del qs[0]
    return (qs)



def JsonFormat(mylistset):
    qi=[]
    for i in range(0, len(mylistset)):
        qi.append(i)
    # Main
    questions = {}
    w=int(len(mylistset))
    for i in range(0, w):
        temp = mylistset[i]
        question = (temp[0: temp.index('(1)')])
        option1 = (temp[temp.index('(1)'):temp.index('(2)')])
        option2 = (temp[temp.index('(2)'):temp.index('(3)')])
        option3 = (temp[temp.index('(3)'):temp.index('(4)')])
        option4 = (temp[temp.index('(4)'):temp.index('ANSWER')])
        answer =  (temp[temp.index('ANSWER'):])
        answer =  (temp[temp.index('ANSWER'):])
        answer=answer.rstrip()
        answer = answer[-1]
        questions.update({
            i+1: ({
                'question': question,
                'option1': option1,
                'option2': option2,
                'option3': option3,
                'option4': option4,
                'answer' : answer,
            })
        })
    return (questions)

# with open('questions.txt') as f:
#     fin = f.read()
#     mylistset = setExtraction(fin)
#     questions = JsonFormat(mylistset)
#     lt= len(questions.keys())


# for i in range(1,lt+1):
#     print(questions[i]['question'])
#     print(questions[i]['option1'])
#     print(questions[i]['option2'])
#     print(questions[i]['option3'])
#     print(questions[i]['option4'])