
import cv2
from ultralytics import YOLO
import imutils
import easyocr

image = cv2.imread("foto.jpg")


model = YOLO('runs/detect/train/weights/best.pt')
reader = easyocr.Reader(['en'], gpu=True)

results = model(image)

for result in results:
    print(f'==> 1 Processing result with {len(result.boxes)} boxes.')
    index_plates = (result.boxes.cls == 0).nonzero(as_tuple=True)[0]

    for idx in index_plates:
        print(f'==> 2 Processing box index: {idx}')
        conf = result.boxes.conf[idx].item()
        print(f'==> 3 Box confidence: {conf}')
        if conf > 0.6:
            print('==> 4 Confidence above threshold, processing plate.')
            x1, y1, x2, y2 = map(int, result.boxes.xyxy[idx])
            # 🔹 Recorte de la placa
            placa = image[y1-15:y2+15, x1-15:x2+15]

            print(f'==> 5 Detected plate with confidence {conf}: [{x1}, {y1}, {x2}, {y2}]')
            # Mostrar placa recortada
            cv2.imshow("Placa detectada", placa)
            print("==> 6 Placa detectada mostrada.")
           
            # 🔹 Reconocimiento OCR    
            placa_rgb = cv2.cvtColor(placa, cv2.COLOR_BGR2RGB)
            result = reader.readtext(placa)
            texto = "".join([r[1] for r in result])
            print("==> 7 Resultado OCR:", texto)


cv2.imshow("Imagen original", imutils.resize(image, width=720))
cv2.waitKey(0)
cv2.destroyAllWindows()