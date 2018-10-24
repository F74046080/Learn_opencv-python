# Learn_opencv-python

## Image Proceesion
* load image: ``cv2.imread('image', num)``
	* image: the path of the image
	* num: 0->color, 1->gray, 2->unchanged
* flip image: ``cv2.flip``
* linear transformation: ``cv2.addWeighted``

## Adaptive Threshold
* global threshold: ``cv2.threshold``
* local theshold: ``cv2.adaptiveThreshold``

## Transform
* rows, cols, channel = img.shape (color); rows, cols = img.shape (gray)
    * rows -> height   
    * columns -> width

### translation: ``cv2.warpAffine(img, H, (rows, columns))``
* img: the image which you want to transform
* H: transform matrix
* (rows, columns): the size after transform

### rotation: ``cv2.getRotationMatrix2D((x, y), angle, scale)``
* (x, y): the central of the rotation image
* angle(theta): the angle of the rotation
* scale: the size of the image zoomed

## Perspective transformation
### ``cv2.getPerspectiveTransform(position1, position2)``
* position1: the origin position(4 points)
* position2: the position you want to wrap(4 points)