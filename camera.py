import cv2 # pip3 install opencv-python

def main():
    # Kamerayı açıcak
    cap = cv2.VideoCapture(0)
    while True:
        # Kare okuma kodu
        ret, frame = cap.read()
        # ekrana verme
        cv2.imshow('Kamera', frame)
        # 'q' tuşu ile döngü kırılıyor
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release() # kamera serbest bırakılıyor
    cv2.destroyAllWindows() # pencere kapatılıyor

if __name__ == '__main__':
    main()
