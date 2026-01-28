# 🎯 OBJETIVO FINAL

Desde una **cámara de seguridad**, obtener algo como:

```json
{
  "vehiculo": "motocicleta",
  "placa": "UJX54H",
  "confianza": 0.92
}
```

---

# 🧠 ARQUITECTURA CORRECTA (LA CLAVE)

❌ Error común: “Un solo modelo que haga todo”
✅ Correcto: **2 etapas**

---

## 🔹 ETAPA 1 — DETECCIÓN DE PLACA (YOLO)

Modelo:

- **YOLOv8 / YOLO11**
- Entrenado para detectar:

  ```
  license_plate
  ```

Salida:

- Bounding box de la placa

---

## 🔹 ETAPA 2 — LECTURA DE TEXTO (OCR)

Modelo OCR especializado:

- **PaddleOCR** (RECOMENDADO)
- EasyOCR
- Tesseract (menos preciso)

Salida:

- Texto de la placa

---

# 🥇 STACK RECOMENDADO (MEJOR OPCIÓN)

| Componente | Tecnología      |
| ---------- | --------------- |
| Detección  | YOLOv8          |
| OCR        | PaddleOCR       |
| Video      | OpenCV          |
| Lenguaje   | Python          |
| Cámara     | IP / RTSP / USB |

---

# 🧩 PIPELINE COMPLETO (CÓMO FUNCIONA)

```text
Cámara RTSP
   ↓
Frame (imagen)
   ↓
YOLO detecta placa
   ↓
Recorte de la placa
   ↓
OCR lee texto
   ↓
Resultado final
```

---

# 🛠️ IMPLEMENTACIÓN PASO A PASO

## 🟢 PASO 1 — Detectar la placa con YOLO

Ejemplo:

```python
from ultralytics import YOLO

model = YOLO("license_plate.pt")
results = model(frame)

for box in results[0].boxes:
    x1, y1, x2, y2 = map(int, box.xyxy[0])
    plate_img = frame[y1:y2, x1:x2]
```

---

## 🟢 PASO 2 — OCR con PaddleOCR

Instalar:

```bash
pip install paddleocr paddlepaddle
```

Uso:

```python
from paddleocr import PaddleOCR

ocr = PaddleOCR(lang='en')

result = ocr.ocr(plate_img)

text = result[0][0][1][0]
confidence = result[0][0][1][1]
```

---

## 🟢 PASO 3 — Filtrar texto

Placas tienen formato fijo:

```python
import re

pattern = r"[A-Z0-9]{5,7}"
match = re.search(pattern, text)

if match:
    plate = match.group()
```

---

# 📹 SOPORTE PARA CÁMARA DE SEGURIDAD

Para cámaras IP:

```python
cap = cv2.VideoCapture("rtsp://user:pass@ip:554/stream")
```

Para webcam:

```python
cap = cv2.VideoCapture(0)
```

---

# ⚠️ IMPORTANTE (REALIDAD)

✔ Funciona bien de día
✔ Funciona bien con ángulo moderado
❌ Difícil de noche sin IR
❌ Difícil si la placa está borrosa

Esto es normal incluso en sistemas comerciales.

---

# 🧪 MODELOS LISTOS (SI NO QUIERES ENTRENAR)

Puedes usar:

- Modelos YOLO de placas en Roboflow
- OpenALPR (pago)
- PlateRecognizer (pago)

---

# 🚀 SIGUIENTE PASO (RECOMENDADO)

Dime:
1️⃣ ¿País de las placas?
2️⃣ ¿Cámara IP o webcam?
3️⃣ ¿PC o servidor?
4️⃣ ¿Tiempo real o capturas?

Con eso te doy:
✔ Modelo exacto
✔ Código listo para ejecutar
✔ Configuración RTSP
✔ Optimización de rendimiento
