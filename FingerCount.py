import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # ROI: Kameranın orta kısmı
        roi = frame[100:400, 100:400]
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

        # Histogram Eşitleme ile Gri Ton Dengesi
        gray = cv2.equalizeHist(gray)

        # Gaussian Blur ile Gürültü Azaltma
        blur = cv2.GaussianBlur(gray, (15, 15), 0)

        # Eşikleme
        _, thresh = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY_INV)

        # Kontur Bulma
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            max_contour = max(contours, key=cv2.contourArea)

            # Alan Kontrolü: Çok küçük ya da çok büyük konturları ele
            if 3000 < cv2.contourArea(max_contour) < 20000:
                # Konturun Pürüzlerini Azaltma
                epsilon = 0.01 * cv2.arcLength(max_contour, True)
                approx = cv2.approxPolyDP(max_contour, epsilon, True)


                try:
                    hull = cv2.convexHull(approx, returnPoints=False)
                    if len(hull) >= 4:
                        defects = cv2.convexityDefects(approx, hull)
                        if defects is not None:
                            count_defects = 0
                            for i in range(defects.shape[0]):
                                s, e, f, d = defects[i, 0]
                                start = tuple(approx[s][0])
                                end = tuple(approx[e][0])
                                far = tuple(approx[f][0])

                                # Üçgen Kenar Uzunlukları
                                a = np.linalg.norm(np.array(end) - np.array(start))
                                b = np.linalg.norm(np.array(far) - np.array(start))
                                c = np.linalg.norm(np.array(far) - np.array(end))

                                # Cosine Kuralı ile Açıyı Hesapla
                                angle = np.arccos((b**2 + c**2 - a**2) / (2 * b * c))

                                if angle <= np.pi / 2 and d > 5000:
                                    count_defects += 1

                            # Parmak Sayısı
                            fingers = count_defects + 1
                            cv2.putText(frame, f"Fingers: {fingers}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                except cv2.error as e:
                    print(f"Convexity Error: {e}")

        # Görüntüleri Göster
        cv2.rectangle(frame, (100, 100), (400, 400), (0, 255, 0), 2)  # ROI Alanı
        cv2.imshow("Threshold", thresh)
        cv2.imshow("Gray ROI", gray)
        cv2.imshow("Frame", frame)

        # Çıkış için 'q'ya bas
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
