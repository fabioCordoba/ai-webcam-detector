# 🧠 Flujo general

1️⃣ Conseguir dataset de placas
2️⃣ Anotar (etiquetar) las placas
3️⃣ Preparar estructura YOLO
4️⃣ Entrenar el modelo
5️⃣ Probar con imágenes / webcam

---

## 1️⃣ Dataset de placas 🚗

Puedes usar uno ya hecho o crear el tuyo.

### 📦 Datasets recomendados

- **CCPD** (muy bueno)
- **OpenALPR Benchmark**
- **UFPR-ALPR**
- **Roboflow – License Plate datasets**

👉 Recomendado si estás empezando: **Roboflow** (ya viene en formato YOLO)

---

## 2️⃣ Etiquetar las placas 🏷️

Si usas tus propias imágenes:

### Herramientas

- **LabelImg** (simple)
- **Roboflow (web)**
- **CVAT** (avanzado)

### Clase

Solo necesitas **1 clase**:

```txt
0 → license_plate
```

---

## 3️⃣ Estructura del proyecto 📁

YOLOv8 espera esta estructura:

```bash
dataset/
├── images/
│   ├── train/
│   └── val/
├── labels/
│   ├── train/
│   └── val/
└── data.yaml
```

---

## 4️⃣ Archivo `data.yaml` ⚙️

Ejemplo:

```yaml
path: dataset
train: images/train
val: images/val

names:
  0: license_plate
```

---

## 5️⃣ Instalar YOLOv8 🧩

```bash
pip install ultralytics
```

Verifica:

```bash
yolo --help
```

---

## 6️⃣ Entrenar YOLO 🚀

Usa un modelo base (transfer learning):

### Recomendado para empezar:

```bash
yolo task=detect mode=train model=yolov8n.pt data=data.yaml epochs=50 imgsz=640
```

### Opciones importantes:

| Parámetro | Recomendado           |
| --------- | --------------------- |
| model     | `yolov8n.pt` (rápido) |
| epochs    | 50–100                |
| imgsz     | 640                   |
| batch     | 8–16                  |
| device    | `cpu` o `0` (GPU)     |

---

## 7️⃣ Resultados 📊

Al terminar tendrás:

```bash
runs/detect/train/
├── weights/
│   ├── best.pt
│   └── last.pt
```

👉 **Usa `best.pt`**

---

## 8️⃣ Probar con imágenes 📸

```bash
yolo task=detect mode=predict model=best.pt source=test.jpg
```

---

## 9️⃣ Probar con webcam 🎥

```bash
yolo task=detect mode=predict model=best.pt source=0
```

---

## 🔠 OCR (leer texto de la placa)

YOLO **solo detecta la placa**, no lee el texto.

Flujo recomendado:

```
YOLO → recorta placa → OCR
```

### OCR recomendados

- **EasyOCR** (muy bueno)
- **Tesseract** (más clásico)

Ejemplo:

```python
import easyocr
reader = easyocr.Reader(['es'])
result = reader.readtext(plate_crop)
```

---

## ⚡ Mejores prácticas

✔ Aumentar datos (rotación, blur, noche)
✔ Entrenar solo **placas** (mejora precisión)
✔ Usar imágenes reales
✔ Ajustar `imgsz` a 640 o 960

---

## 🏆 Resultado final

🎯 Detección precisa
🎯 Tiempo real
🎯 Ideal para:

- Cámaras
- Webcam
- Telegram bot
- n8n
- Seguridad / parqueaderos

---

## ¿Qué sigue?

Puedo ayudarte a:

- Crear **dataset**
- Mejorar precisión
- Integrar **OCR**
- Exportar a **ONNX / TensorRT**
- Integrar con **n8n o Telegram**
