import numpy as np
from PIL import Image

i = Image.open('s.png').convert('RGB')

seed=42

# Get shuffled pixels in Numpy array
shuffled = np.array(i.getdata())
nPix = len(shuffled)

# Generate unshuffler
np.random.seed(seed)
ind = np.random.permutation(nPix)
unshuffler = np.zeros(nPix, np.uint32)
unshuffler[ind] = np.arange(nPix)

unshuffledPix = shuffled[unshuffler].astype(np.uint8)
r=Image.fromarray(unshuffledPix.reshape(i.width,i.height,3))

# Load image and ensure RGB, i.e. not palette image

r.save('uns.png')

