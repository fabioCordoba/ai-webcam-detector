
from paddleocr import PaddleOCR
import re

def limpiar_texto(texto):
    return re.sub(r"\s+", " ", texto.strip())


ocr = PaddleOCR(
    use_doc_orientation_classify=False, 
    use_doc_unwarping=False, 
    use_textline_orientation=False)

# #para Dockerfile optimizado
# ocr = PaddleOCR(
#     text_detection_model_name="PP-OCRv5_mobile_det",
#     text_recognition_model_name="PP-OCRv5_mobile_rec",
#     use_doc_orientation_classify=True,
#     use_doc_unwarping=True,
#     use_textline_orientation=True
# )

# ocr = PaddleOCR(use_doc_orientation_classify=True, use_doc_unwarping=True) # 文本图像预处理+文本检测+方向分类+文本识别
# ocr = PaddleOCR(use_doc_orientation_classify=False, use_doc_unwarping=False) # 文本检测+文本行方向分类+文本识别
# ocr = PaddleOCR(
#     text_detection_model_name="PP-OCRv5_mobile_det",
#     text_recognition_model_name="PP-OCRv5_mobile_rec",
#     use_doc_orientation_classify=False,
#     use_doc_unwarping=False,
#     use_textline_orientation=False) # 更换 PP-OCRv5_mobile 模型
# result = ocr.predict("./general_ocr_002.png")

result = ocr.predict("./imagen_test_001.jpg")
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
