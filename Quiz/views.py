from django.shortcuts import render,redirect

def startup(request):
    return redirect('/math')
def phy(request,q=1):
    if q<25:
        nextq=q+1
    else:
        nextq=25
    mydata={
        'path':'phy',
        'q':nextq,
    }
    return render(request,'s_phy.html',mydata)
def math(request,q=1):
    if q<25:
        nextq=q+1
    else:
        nextq=25
    mydata={
        'path':'math',
        'q':nextq,
    }
    return render(request,'s_math.html',mydata)
def chem(request,q=1):
    if q<25:
        nextq=q+1
    else:
        nextq=25
    mydata={
        'path':'chem',
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
