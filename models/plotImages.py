import matplotlib.pyplot as plt
import numpy as np

def plot_random_images(dataset, num_images):
    # Bestimme die Anzahl der Bilder im Dataset
    total_images = dataset.n
    
    # Wähle zufällige Indizes basierend auf der gewünschten Anzahl an Bildern
    random_indices = np.random.choice(total_images, num_images, replace=False)
    
    # Initialisiere einen Zähler, um die Anzahl der geplotteten Bilder zu verfolgen
    plotted_images = 0
    
    # Iteriere über das Dataset und plotte die Bilder mit den ausgewählten Indizes
    for i, (images, labels) in enumerate(dataset):
        for j in range(images.shape[0]):  # Gehe durch den aktuellen Batch
            # Plotte nur, wenn der aktuelle Index in den zufälligen Indizes enthalten ist
            if i * dataset.batch_size + j in random_indices:
                plt.figure(figsize=(5, 5))
                # Bilder können entweder in Graustufen oder in Farbe sein
                if images.shape[-1] == 1:  # Graustufenbild
                    plt.imshow(images[j].reshape(images[j].shape[0], images[j].shape[1]), cmap='gray')
                else:  # Farbbild
                    plt.imshow(images[j].astype('uint8'))
                plt.title(f'Label: {labels[j]}')
                plt.axis('off')
                plt.show()
                
                plotted_images += 1
                if plotted_images >= num_images:
                    return  # Beende die Funktion, wenn die gewünschte Anzahl an Bildern geplottet wurde
        
        if plotted_images >= num_images:
            break  # Beende die äußere Schleife, wenn die gewünschte Anzahl an Bildern geplottet wurde