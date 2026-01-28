import os
os.environ["FLAGS_enable_onednn"] = "0"

import cv2
from ultralytics import YOLO
# from paddleocr import PaddleOCR
import easyocr


def main():
    # model = YOLO("yolov8n.pt")  # Se descarga solo la primera vez
    # model = YOLO("yolo11n.pt")  # Se descarga solo la primera vez
    model = YOLO('runs/detect/train/weights/best.pt')
    # ocr = PaddleOCR(lang='en')
    reader = easyocr.Reader(['es'], gpu=False)

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ No se pudo acceder a la cámara")
        return

    print("📷 Cámara iniciada. Presiona 'q' para salir.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Error al leer la cámara")
            break

        results = model(frame)

        for box in results[0].boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # 🔹 Recorte de la placa
            placa = frame[y1:y2, x1:x2]
            placa = cv2.resize(placa, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

            # Mostrar placa recortada
            cv2.imshow("Placa detectada", placa)

            # (opcional) Guardar imagen
            # cv2.imwrite("placa.jpg", placa)
            # 🔹 Reconocimiento OCR
            # result = ocr.predict(placa)
            result = reader.readtext(placa)
            for (_, text, conf) in result:
                print(f"===> Placa: {text}, Confianza: {conf}")

            # if result and len(result[0]) > 0:
            #     text = result[0][0]['text']
            #     confidence = result[0][0]['score']
            #     print(f"===> Placa: {text} (Confianza: {confidence:.2f})")
            # else:
            #     print("No se pudo leer texto")

        annotated_frame = results[0].plot()

        cv2.imshow("Detección en tiempo real", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

