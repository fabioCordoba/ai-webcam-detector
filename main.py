
import cv2
from ultralytics import YOLO
import imutils
import easyocr
import re

def clean_plate(text):
    text = text.upper()
    text = re.sub(r'[^A-Z0-9]', '', text)

    # Correcciones comunes
    text = text.replace('0', 'O')
    text = text.replace('6', 'G')
    text = text.replace('1', 'I')

    return text


def preprocess_plate(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    _, thresh = cv2.threshold(gray, 0, 255,
                              cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresh



def main():
    # model = YOLO("yolov8n.pt")  # Se descarga solo la primera vez
    # model = YOLO("yolo11n.pt")  # Se descarga solo la primera vez
    model = YOLO('runs/detect/train/weights/best.pt')
    reader = easyocr.Reader(['en'], gpu=True)

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
            placa = frame[y1-15:y2+15, x1-15:x2+15]

            # Mostrar placa recortada
            cv2.imshow("Placa detectada", placa)

            # (opcional) Guardar imagen
            # cv2.imwrite("placa.jpg", placa)

            # 🔹 Reconocimiento OCR
            # Aquí puedes integrar tu modelo OCR para reconocer el texto de la placa
            plate_proc = preprocess_plate(placa)
            cv2.imshow("Placa procesada", plate_proc)

            result = reader.readtext(
                plate_proc,
                allowlist="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
                detail=1
            )

            texto_raw = "".join([r[1] for r in result if r[2] > 0.7])
            texto = clean_plate(texto_raw)

            print("✅ PLACA FINAL:", texto)


        annotated_frame = results[0].plot()

        cv2.imshow("Detección en tiempo real", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

