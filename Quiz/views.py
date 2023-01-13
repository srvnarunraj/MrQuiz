from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import phy,chem,math 
from . import DataExtraction
from Quiz.models import FileDir
from django.core.files.storage import FileSystemStorage
import os

def startup(request):
    return redirect('exam/math')
def m_phy(request,q=1):
    x=request.path
    if any(chr.isdigit() for chr in x):
        pass
    else:
        return redirect('/exam/phy/1') 
    path='phy'
    if q<25:
        nextq=q+1
    else:
        path='chem'
        nextq=1
    mydata={
        'path':path,
        'q':nextq,
    }
    return render(request,'s_phy.html',mydata)
def m_math(request,q=1):
    x=request.path
    if any(chr.isdigit() for chr in x):
        pass
    else:
        return redirect('/exam/math/1')
    path ='math'
    if q<25:
        nextq=q+1
    else:
        path='phy'
        nextq=1
    mydata={
        'path':path,
        'q':nextq,
    }
    return render(request,'s_math.html',mydata)
def m_chem(request,q=1):
    questions=chem.objects.filter(id=q)
    sid= 'chem'+str(q)
    try:
            stu_ans = request.session[sid]['an']
    except:
            stu_ans = ''
    x=request.path
    if any(chr.isdigit() for chr in x):
        pass
    else:
        return redirect('/exam/chem/1')

    path = 'chem'
    if q<25:
        nextq=q+1
    else:
        nextq=1
    mydata={
        'n':q,
        'qe':questions,
        'sub':'chem',
        'sid':sid,
        'ans':stu_ans,
        'path':path,
        'q':nextq,
    }
    return render(request,'s_chem.html',mydata)
def submitanswer(request):
    import re
    x='/phy/1'
    path=''
    k= re.findall(r'\d+', x)
    for i in x:
        if i in k:
            p=(int(str(i)))
            p+=1
        else:
            path+=i
    nextloc=path+str(p)
    return redirect(nextloc)

# Uploading Questions

 
def method(subj):
    loc = FileDir.objects.values_list('Fileloc').filter(sub=subj).latest('id')
    k=str(loc)[2:-3]
    # with open('H:\DB Project\Exam\media\questions.txt') as f:
    with open(k) as f:
        fin = f.read()
        mylistset = DataExtraction.setExtraction(fin)
        Examquestions = DataExtraction.JsonFormat(mylistset)
    return Examquestions
def upload(subj):
        Examquestions = method(subj)
        l=(len(Examquestions))
        ql=[]
        k=1
        for i in range(l):
            q=(Examquestions[k]['question'])
            o1=(Examquestions[k]['option1'])
            o2=(Examquestions[k]['option2'])
            o3=(Examquestions[k]['option3'])
            o4=(Examquestions[k]['option4'])
            answer = (Examquestions[k]['answer'])
            if subj =='chem':
                chemq = chem(id=i+1,question=q,option1=o1,option2=o2,option3=o3,option4=o4,answer=answer)       
            if subj=='phy':
                chemq = phy(id=i+1,question=q,option1=o1,option2=o2,option3=o3,option4=o4,answer=answer)
            if subj=='math':
                chemq = math(id=i+1,question=q,option1=o1,option2=o2,option3=o3,option4=o4,answer=answer)
            chemq.save()
            k+=1

def up(request):
    if request.method =='POST':
        myfile = request.FILES['myfile_Q']
        subj = request.POST['sub']
        save_myfile=FileSystemStorage()
        name = save_myfile.save(myfile.name,myfile)
        d = os.getcwd()
        fd = d+'\media\\'+name
        input = FileDir(Fileloc=fd,sub=subj)
        input.save()
        upload(subj)
    return render(request,'uploadFile.html')


# Answer Submission & Evauation

def check(request,subj,q=1):
    try:
        sel_op = request.POST['choice']
    except:
        sel_op='0'
    finally:
        qn = str(q)
        sid= subj+str(q)
        us={
            'sub':subj,
            'qid':q,
            'an':sel_op,
        }
        request.session[sid] = us
        if q<25:
            nq = str(q+1)
        else:
            q=0
            nq = str(q+1)
        mypath = '/exam/'+subj+'/'+nq
        print('gan',request.session[sid]['an'])
        print('gan',request.session[sid])
        return redirect(mypath)

def FinalSubmission(request):
    # chem Evaluation
    questions=chem.objects.all()
    chem_ans=[]
    user_ans=[]
    totalmarks=0
    # Collect User Answers
    for i in questions:
        chem_ans.append(i.answer)
        sid= 'chem'+str(i.id)
        try:
            user_ans.append(request.session[sid]['an'])
        except:
            us={
                'sub':'chem',
                'qid':i.id,
                'an':'0',
            }
            request.session[sid] = us
            user_ans.append(request.session[sid]['an'])
    # Valuation
    crct_qus=[]
    wrng_qus_ans={
        'q':[],
        'a':[],
    }
    marks=0
    l = len(chem_ans)
    for i in range(0,l):
        if (chem_ans[i]==user_ans[i]):
            crct_qus.append(i)
            marks+=4
        elif (chem_ans[i]!=user_ans[i]) and user_ans[i]!='0' :
            wrng_qus_ans['q'].append(i+1)
            wrng_qus_ans['a'].append(user_ans[i])
            marks-=1
    totalmarks=str(marks)
    data={
        'tot_chem_marks':totalmarks,
        'crct':crct_qus,
        'uans':user_ans,
        'wrng':wrng_qus_ans,
        'q':questions
    }
    return render(request,'result.html',data)
   
