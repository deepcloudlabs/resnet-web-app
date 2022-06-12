import os

from bau.resnet_util import read_and_prep_images, decode_predictions, resnet_model

samples_path = './bau/input/sample-images'
samples_path = [os.path.join(samples_path, filename) for filename in os.listdir(samples_path)]
image_data = read_and_prep_images(samples_path)

my_predictions = resnet_model.predict(image_data)
labels = decode_predictions(my_predictions, top=1)
for i, image_path in enumerate(samples_path):
    print(f"%32s %24s %1.2f" % (image_path, labels[i][0][1], labels[i][0][2]))
