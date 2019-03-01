%%time
import numpy as np
import pandas as pd
from PIL import Image

def locate_repeated_area(img_path, search_width=20, work_size=(400,300), min_shift=5, max_shift=50):
    """
    Locate vertical strap on image with highest repeated strucrure
    
    Arguments:
    
    Returns:
    results -- x-coordinate of strap and repeate period
    """
    img = Image.open(img_path).resize(work_size) # Open an image
    img = np.array(img.convert("L"), dtype=float)/255 # Convert to black-wight
    results = [0, 1] # List of results: 
    kmax = 0
    
    # Iterate along width of the image
    for x in range(0, img.shape[1]-search_width, int(search_width/2)):
        amax = 0
        amin = 1
        # Iterate among different values of shift
        for sh in range(min_shift, max_shift):
            # Calculation of the aim
            w = img[:,x:x+search_width].mean(axis=1) # Average along width of strap
            aim = (pd.DataFrame(w)-pd.DataFrame(w).shift(sh))[sh:].abs().median().values[0] # Calc aim
            
            # Estimating max reduce of the aim having current shift sh
            if aim>amax:
                amax = aim
                amin = amax
            if aim<amin:
                amin = aim
            aim_k = amax/amin
            if aim_k>kmax:
                results = [x, sh]
                kmax = aim_k
                
    pylab.imshow(img, 'gray');
    plt.plot([x_opt[0]]*2, [0, 200], c='yellow', linewidth=2)    
    return results
    
x, shift = locate_repeated_area('rough_data/14.jpg')
print('coordinate x: {0}, period: {1}'.format(x, shift))
