# SAE Binarization

Repository of the Rodan wrapper for SAE Binarization

Original Code at https://github.com/ajgallego/document-image-binarization by Jorge Calvo-Zaragoza and Antonio-Javier Gallego

# Python dependencies:
  * tensorflow (2.5.1)
  * opencv-python (4.5.5.64)
  * numpy (1.22.4)
  * keras (2.5.0rc0)

# Rodan Job

This background removal task belongs inside gpu-celery container.

# Local Usage 

The `binarize.py` script performs the binarization of an input image using a trained model. The parameters of this script are the following:


| Parameter    | Default | Description                      |
| ------------ | ------- | -------------------------------- |
| `-imgpath`   |         | Path to the image to process     |
| `-modelpath` |  (*)       | Path to the model to load        |
| `-w`         |  256    | Input window size                |
| `-s`         |  -1     | Step size. -1 to use window size |
| `-f`         |  64     | Number of filters                |
| `-k`         |  5      | Kernel size                      |
| `-drop`      |  0      | Dropout percentage               |
| `-stride`    |  2      | Convolution stride size          |
| `-every`     |  1      | Residual connections every x layers |
| `-th`        |  0.5    | Selectional threshold            |
| `-save`      |         | Output image filename            |

> (*) By default, the model trained with all datasets will be used.

The only mandatory parameter is `-imgpath`, the rest are optional. You also have to choose if you want to save (`-save`) the binarized image.

For example, to binarize the image `img01.png` you can run the following command:

```
$ python binarize.py -imgpath img01.png -save out.png
```