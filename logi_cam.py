# # https://github.com/Smart-Recycling-Garbage/hw.git

# # pip install opencv-python-headless
import cv2

# 웹캠 영상 캡쳐를 위한 VideoCapture 객체 생성
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(1)

while True:
    # 웹캠에서 프레임을 읽어옴
    ret, frame = cap.read()

    # 프레임이 정상적으로 읽어왔을 경우 화면에 표시
    if ret:
        cv2.imshow('Webcam', frame)

    # q를 누르면 프로그램 종료
    if cv2.waitKey(1) == ord('q'):
        break

# 객체와 창 닫기
cap.release()
cv2.destroyAllWindows()

# import cv2

# cap = cv2.VideoCapture(1)

# if not cap.isOpened():
#     print("Could not open camera")
# else:
#     print("Camera is ready")

# cap.release()
# cv2.destroyAllWindows()
