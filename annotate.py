import numpy as np
import stardist

from stardist.models import Config2D, StarDist2D
from stardist import random_label_cmap
import tifffile
import matplotlib.pyplot as plt
from csbdeep.utils import normalize


def annotate(imagedata):

    n_rays = 32

    #import gputools
    # Use OpenCL-based computations for data generator during training (requires 'gputools')
    use_gpu = stardist.gputools_available()

    # Predict on subsampled grid for increased efficiency and larger field of view
    grid = (2,2)

    conf = Config2D (
        n_rays       = n_rays,
        grid         = grid,
        use_gpu      = use_gpu,
        n_channel_in = 1,
    )

    if use_gpu:
        from csbdeep.utils.tf import limit_gpu_memory
        # adjust as necessary: limit GPU memory to be used by TensorFlow to leave some to OpenCL-based computations
        limit_gpu_memory(0.8)
        # alternatively, try this:
        # limit_gpu_memory(None, allow_growth=True)

    model = StarDist2D(None, name='stardist', basedir='models')

    X = normalize(imagedata)
    pred,details = model.predict_instances(X)

    np.random.seed(6)
    lbl_cmap = random_label_cmap()

    #plt.figure(figsize=(8,8))
    fig, (i1,i2) = plt.subplots(1,2, figsize=(12,5))
    i1.imshow(X if X.ndim==2 else X[...,0], clim=(0,1), cmap='gray')
    i2.imshow(pred, cmap=lbl_cmap, alpha=0.5)
    plt.axis('off')

    # fig, (i1,i2) = plt.subplots(1,2, figsize=(20,10))
    # im = i1.imshow(X)
    # i2.imshow(pred)
    plt.show()

def loadimage(filename):
    return tifffile.imread(filename)


if __name__ == "__main__":
    data = loadimage("images/0bda515e370294ed94efd36bd53782288acacb040c171df2ed97fd691fc9d8fe.tif")
    annotation = annotate(data)
