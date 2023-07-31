from django.shortcuts import render

from .models import UserImage
# Create your views here.
from myapp.forms import UserImageForm
import cv2
from clustimage import Clustimage
from PIL import Image

from django.conf import settings
import os
import pickle


def home(request):
    image_path = os.path.join(settings.MEDIA_ROOT, 'user_images/jacket.jpg')

    if os.path.exists(image_path) and os.path.isfile(image_path):
        image = cv2.imread(image_path, 0)
        cv2.imwrite(image_path, image)
    cl = Clustimage(method='pca')

    feature_path = os.path.join(settings.MEDIA_ROOT, 'clustimage_model')
    face_results1 = cl.extract_faces(image_path)
    cl.load(feature_path)
    results_find = cl.find(
        face_results1['pathnames_face'], k=1, alpha=0.05, metric='euclidean')

    data_path = os.path.join(settings.MEDIA_ROOT, 'person_data.pkl')
    face_results = pickle.load(open(data_path, 'rb'))
    name = list(results_find[list(results_find.keys())[1]]['y_pathnames'])
    number = face_results['pathnames_face'].index(name)

    result_image = './result/' + 'image' + \
        str(face_results['filenames'][number])
    result_image_path = os.path.join(settings.MEDIA_ROOT, 'person_data.pkl')

    picture = UserImage.objects.get(pk=9)
    picture = picture.image.url
    form = UserImageForm()

    if request.method == 'POST':
        form = UserImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    return render(request, 'index.html', {
        'form': form,
        'picture': picture,

    })
