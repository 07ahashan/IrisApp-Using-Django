from django.shortcuts import render

from joblib import load

model=load('./SavedModel/model.joblib')

# Create your views here.

def predictor(request):
    if request.method== 'POST':
        sepal_length=request.POST['sepal_length']
        sepal_Width=request.POST['sepal_Width']
        petal_length=request.POST['petal_length']
        petal_Width=request.POST['petal_Width']

        y_pred = model.predict([[sepal_length,sepal_Width,petal_length,petal_Width]])
        
        if y_pred[0]==0:
            y_pred='Setosa'
        elif y_pred[0]==1:
            y_pred='versicolor'
        else:
            y_pred ='virginica'        
        return render(request,'main.html',{'result': y_pred })
    return render(request,'main.html')

    