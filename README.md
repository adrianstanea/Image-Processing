# Image-Processing
Project focused on image segmentation

# Virtual enviroment management

- Create a conda enviroment to separate project packages from system binaries

```bash
    conda update conda
    conda create -n ENV_NAME python=3.10
```

- Project dependencies were listed using:

```bash
    conda env export --from-history > requirements_conda.txt
    pip-chill > requirements_pip.txt
```

## Datasets used

- https://github.com/xingchenzhang/MFIF