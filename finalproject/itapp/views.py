from django.shortcuts import render, redirect
from django.http import HttpResponse
from tensorflow import keras
import os


os.environ['CUDA_VISIBLE_DEVICES'] = '-1'


# Create your views here.
def home(request):
    context = {'name': 'User'}
    return render(request, 'index.html', context)


def prediction(request):
    if request.method == 'POST':
        try:
            CRIM = float(request.POST['CRIM'])
        except:
            CRIM = 0
        try:
            ZN = float(request.POST['ZN'])
        except:
            ZN = 0
        try:
            INDUS = float(request.POST['INDUS'])
        except:
            INDUS = 0
        try:
            CHAS = float(request.POST['CHAS'])
        except:
            CHAS = 0
        try:
            NOX = float(request.POST['NOX'])
        except:
            NOX = 0
        try:
            RM = float(request.POST['RM'])
        except:
            RM = 0
        try:
            AGE = float(request.POST['AGE'])
        except:
            AGE = 0
        try:
            DIS = float(request.POST['DIS'])
        except:
            DIS = 0
        try:
            RAD = float(request.POST['RAD'])
        except:
            RAD = 0
        try:
            TAX = float(request.POST['TAX'])
        except:
            TAX = 0
        try:
            PTRATIO = float(request.POST['PTRATIO'])
        except:
            PTRATIO = 0
        try:
            B = float(request.POST['B'])
        except:
            B = 0
        try:
            LSTAT = float(request.POST['LSTAT'])
        except:
            LSTAT = 0

        model = tf.keras.models.load_model("C:\\Users\\hppc\\Desktop\\finalproject\\finalproject\\data\\boston_model.h5")
		argus = np.array([[CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT]])
		result = model.predict(argus)

        context = {
            'result': result
        }
        return render(request, 'prediction.html', context)
    else:
        return redirect('/')
