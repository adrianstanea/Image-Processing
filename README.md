# Image-Processing
Algorithm implementation of *Multi-focus image fusion using learning based matting with sum of the Gaussian-based modified Laplacian*

# Virtual Enviroment Setup

- Create a virtual enviroment to separate project packages from system binaries. If you are using `venv` run the following commands:

1. Create virtual environment in the current workspace:
```bash
  python3 -m venv .venv/mfif
``` 
2. Activate the virtual environment:
```bash
    .venv\mfif\Scripts\activate       # Windows
    source .venv/mfif/bin/activate    # Unix or MacOS
```
3. Once the virtual environment is activated, install the required packages:
```bash
    pip install -r requirements.txt
```


## Datasets used

- https://github.com/xingchenzhang/MFIF