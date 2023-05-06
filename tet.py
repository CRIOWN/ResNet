import os

if __name__ == '__main__':
    data_root = os.path.abspath(os.path.join(os.getcwd(), "../"))  # get data root path
    image_path = os.path.join(data_root, "data_set", "flower_data")  # flower data set path
    print(data_root)
    print(image_path)