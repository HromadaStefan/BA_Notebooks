def load_images_and_labels(directory, target_size):
    images = []
    labels = []  

    for label, class_dir in enumerate(['fake', 'real']):
        class_dir_path = os.path.join(directory, class_dir)
        for file_name in os.listdir(class_dir_path):
            img_path = os.path.join(class_dir_path, file_name)
            img = load_img(img_path, target_size=target_size)
            img_array = img_to_array(img)
            images.append(img_array)
            labels.append(label)

    return np.array(images), np.array(labels)