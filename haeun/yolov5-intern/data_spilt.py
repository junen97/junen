import os
from sklearn.model_selection import train_test_split

dir_path = "./images"
img_root = []


def file_find(dir_path) :

    for (path, dir, file) in os.walk(dir_path) :

        for file_name in file :
            root = os.path.join(dir_path, file_name)
            img_root.append(root)

    return img_root

dataset = file_find(dir_path)

train_img_list, val_img_list = train_test_split(dataset, test_size=0.1, random_state=7777)

train_img_len = len(train_img_list)
val_img_len = len(val_img_list)

print("train len >> " , train_img_len)
print("val len >> " , val_img_len )

with open("./train.txt" , 'a') as f :
    f.write("\n".join((train_img_list)) + "\n")

with open("./val.txt" , 'a') as f :
    f.write("\n".join((val_img_list)) + "\n")