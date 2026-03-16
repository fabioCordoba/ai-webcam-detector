
import cv2
from ultralytics import YOLO
from paddleocr import PaddleOCR
import re

def limpiar_texto(texto):
    return re.sub(r"\s+", " ", texto.strip())


def main():
    # model = YOLO("yolov8n.pt")  # Se descarga solo la primera vez
    # model = YOLO("yolo11n.pt")  # Se descarga solo la primera vez
    model = YOLO('runs/detect/train/weights/best.pt')
    ocr = PaddleOCR(
        use_doc_orientation_classify=False, 
        use_doc_unwarping=False, 
        use_textline_orientation=False)

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
            result = ocr.predict(placa)
            for res in result:
                print("==== RESULTADO OCR ====")
                # Salida original
                res.print()
                # res.save_to_img("output")
                res.save_to_json("output")

                print("----- Diferentes formatos de salida -----")
                # Texto simple
                print("Texto detectado:", limpiar_texto(str(res['rec_texts'][0])))
                print("Confianza:", round(float(res['rec_scores'][0]), 3))

        annotated_frame = results[0].plot()

        cv2.imshow("Detección en tiempo real", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

