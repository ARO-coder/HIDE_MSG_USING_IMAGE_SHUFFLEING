import numpy as np
from PIL import Image

#def shuffleImage(im, seed=42):

    # Get pixels and put in Numpy array for easy shuffling
i = Image.open('d.png').convert('RGB')
seed=42
pix = np.array(i.getdata())

    # Generate an array of shuffled indices
    # Seed random number generation to ensure same result
np.random.seed(seed)
indices = np.random.permutation(len(pix))

    # Shuffle the pixels and recreate image
shuffled = pix[indices].astype(np.uint8)
 
r=Image.fromarray(shuffled.reshape(i.width,i.height,3))

#orig = Image.open('d.png').convert('RGB')

#result = shuffleImage(orig)
r.save('s.png')
