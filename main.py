import cv2
import os
path = "datasets"
video = cv2.VideoCapture(0)
face = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
(images, labels, names, id) = ([], [], {}, 0)
print(os.walk(path))
for subdirs, dir, files in os.walk(path):
    for subdir in dir:
        names[id] = subdir
        subject = os.path.join(path , subdir)
        for file in os.listdir(subject):
            img = subject + "/" + file
            label = id
            images.append(cv2.imread(img))
            labels.append(label)
        id += 1
print(names)
print(labels)
print(images)
"""
count = 0
while video.isOpened():
    ret, img = video.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    person = face.detectMultiScale(gray, 1.5, 3)
    print(person)
    for x, y, w, h in person:
        cv2.rectangle(img, (x,y), (x+w, y+h), (230, 25, 189), 2)
        picture = gray[y:y+h, x:x+w]
        picture_resize = cv2.resize(picture, (150, 130))
        os.chdir(datasets)
        cv2.imwrite(f"{count}.png", picture_resize)
        count = count+1
    cv2.imshow("screen", img)
    k = cv2.waitKey(1)
    if k == 27:
        break
    if count == 30:
        break

"""