import json
import os

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
image_size = 224

CLASS_INDEX = json.load(open('./bau/input/resnet/imagenet_class_index.json'))
