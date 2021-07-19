import cv2

cap = cv2.VideoCapture('test_video/1.mp4')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 25, (854,480)) #25프레임 , (높이 너비)

while(True):
    ret, frame = cap.read()
    print(cap.get(cv2.CAP_PROP_POS_FRAMES))
    out.write(frame)

    #print(out.get(cv2.CAP_PROP_FPS))

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if cap.get(cv2.CAP_PROP_POS_FRAMES) == 10:
        break

