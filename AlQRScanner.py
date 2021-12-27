import pyzbar.pyzbar as pyzbar
import cv2


def AlQRScanner():
    i = 0
    cap = cv2.VideoCapture(0)
    output = []
    while i < 4:
        _, frame = cap.read()
        decoded = pyzbar.decode(frame)
        for obj in decoded:
            output.append(obj.data)
            i += 1
        cv2.imshow("QRCode", frame)
        if cv2.waitKey(1) == ord('q'):
            break
        cv2.waitKey(5)
        cv2.destroyAllWindows
    print(output[-1])


if __name__ == '__main__':
    AlQRScanner()
