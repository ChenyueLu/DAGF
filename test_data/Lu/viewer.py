import numpy as np
import cv2

pred = np.load("/Users/luchenyue/DeepX/Code/DAGF/test_data/Lu/pred/6.npy")
gt = np.load("/Users/luchenyue/DeepX/Code/DAGF/test_data/Lu/gt/6.npy")
rgb = np.load("/Users/luchenyue/DeepX/Code/DAGF/test_data/Lu/rgb/6.npy")

# normalize depth image
gt = cv2.normalize(gt, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)

cv2.imshow("rgb", pred)
# cv2.imshow("gt", gt)
cv2.waitKey()