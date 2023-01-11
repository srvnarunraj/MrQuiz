from django.shortcuts import render,redirect

def startup(request):
    return redirect('/math')
def phy(request,q=1):
    x=request.path
    if any(chr.isdigit() for chr in x):
        pass
    else:
        return redirect('/phy/1') 
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
def math(request,q=1):
    x=request.path
    if any(chr.isdigit() for chr in x):
        pass
    else:
        return redirect('/math/1')
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
def chem(request,q=1):
    x=request.path
    if any(chr.isdigit() for chr in x):
        pass
    else:
        return redirect('/chem/1')

    path = 'chem'
    if q<25:
        nextq=q+1
    else:
        nextq=1
    mydata={
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
