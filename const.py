KERNEL_SIZE = 7                     # size of the kernel window used by SGML
SIGMA = 2                           # standard deviation used in SGML byt the gaussian kernel
PADDING = (KERNEL_SIZE - 1) // 2    # neccesary padding to keep the image size


VERBOSE = False                      # print information about the process

STRUCTURING_ELEM_SIZE = 3           # size of the structuring element used in the morphological operations\
MORPH_NUM_ITERATIONS = 7            # number of iterations used in the morphological operations