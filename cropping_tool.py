import cv2

img = cv2.imread('Virat Kohli test jarsey.png')
img_resize = cv2.resize(img,(512,512))

flags = False
ix = -1
iy = -1
jx = -1
jy = -1

def crop(event,x,y,flag,params):
    global flags, ix, iy , jx, jy

    if event == 1:
        flags = True
        ix = x
        iy = y

    elif event == 0:
        jx = x
        jy = y
        if flags == True:

            img_temp = img_resize.copy()
            cv2.rectangle(img_temp, pt1=(ix, iy), pt2=(jx, jy), color=(0, 0, 0), thickness=1)
            cv2.imshow("window", img_temp)

    elif event == 4:
        flags = False
        cv2.rectangle(img_resize, pt1=(ix, iy), pt2=(jx, jy), color=(0, 0, 0), thickness=1)

        x_min, x_max = min(ix, jx), max(ix, jx)
        y_min, y_max = min(iy, jy), max(iy, jy)

        cv2.imshow("cropped", img_resize[y_min:y_max, x_min:x_max])





cv2.namedWindow(winname="window")
cv2.setMouseCallback("window",crop)

while True:
    cv2.imshow("window",img_resize)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cv2.destroyAllWindows()
