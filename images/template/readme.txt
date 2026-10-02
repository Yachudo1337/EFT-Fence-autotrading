img = cv2.imread('images/skupshik.png')

def loading_displaying_saving():
    img = cv2.imread('images/skupshik.png', cv2.IMREAD_GRAYSCALE)
    cv2.imshow('skupshik', img)
    cv2.waitKey(0)
    cv2.imwrite('images/grayskupshik.png', img)





cv2.imshow('images/grayskupshik.png', img)

cv2.waitKey(0)