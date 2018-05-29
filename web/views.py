from django.shortcuts import render
from .utils.predictor import do
from .forms import UploadFileForm
from .models import FileUpload
import os
# Create your views here.
def index(request):
    #path = os.path.dirname(os.path.realpath(__file__)) + '/utils/cancer.csv'
    #list = do(path)
    #context = {'clf_list': list}
    return render(request, 'web/index.html')

def display(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            path = os.path.dirname(os.path.realpath(__file__)) + '/utils/cancer.csv'

            file = request.FILES['file']
            list,corr_list,corr_columns = do(file)
            comb_list=zip(corr_columns,corr_list)
            context = {'list': list, 'corr_list':corr_list, 'corr_columns':corr_columns,'comb_list':comb_list}
            return render(request, 'web/display.html', context )
    else:
        form = UploadFileForm()
    return render(request, 'web/input.html', {'form': form})
