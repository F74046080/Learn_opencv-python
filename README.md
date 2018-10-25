# Learn_opencv-python

## Image Proceesion
* load image: ``cv2.imread(path, num)``
	* path: the relative or absolute path of the image
	* num: 0->color, 1->gray, 2->unchanged
* show image: ``cv2.imshow(name, src)``
	* name: the window name
	* src: the target image
* flip image: ``cv2.flip(src, dst)``
	* src: the target image
	* dst: set 0, -1, 1 to rotate the image
* linear transformation: ``cv2.addWeighted``

## Adaptive Threshold
* global threshold: ``cv2.threshold(src, thres, max, method)``
	* src: target image
	* thres: the threshold value
	* max: the value replace the threshold value
	* method:  cv2.THRESH_BINARY, cv2.THRESH_BINARY_INV, cv2.THRESH_TRUNC,  cv2.THRESH_TOZERO, cv2.THRESH_TOZERO_INV 
* local theshold: ``cv2.adaptiveThreshold(src, dst, max, method, type, blocksize, constant)``
	* src: target image(input)
	* dst: the output image
	* max: maximum the threshold will separate the image into 0 and max
	* method: ADAPTIVE_THRESH_MEAN_C or ADAPTIVE_THRESH_GAUSSIAN_C
	* type: THRESH_BINARY or THRESH_BINARY_INV
	* blocksize: use odd number to decide the threshold value
	* constant: after do the threshold, it may minus some constant value

## Transform
* rows, cols, channel = img.shape (color); rows, cols = img.shape (gray)
    * rows -> height   
    * columns -> width

### translation: ``cv2.warpAffine(src, H, (rows, columns))``
* src: the image which you want to transform
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
### resize the image: ``cv2.resize(src, size)``
	* src: target image
	* size: the new size of the image
