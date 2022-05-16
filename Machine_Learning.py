from fastai.vision import *
from pathlib import Path
from fastai.vision.image import open_image


def predict(image_path):
    path = Path('modelFile')
    learn = load_learner(path)
    img= open_image(image_path)
    pred_class,pred_idx,outputs = learn.predict(img)
    return pred_class.obj

# path=Path('modelFile')
# learn = load_learner(path)
# path=Path('some_image.jpg')
# print(predict(path))
