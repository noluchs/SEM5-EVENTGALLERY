from deepface import DeepFace

import os
from deepface.commons import distance as dst

def match_faces(query_path, gallery_dir):
    try:
        query_vec = DeepFace.represent(img_path=query_path, model_name="VGG-Face")[0]["embedding"]
    except Exception as e:
        return {"error": f"Fehler beim Encoding: {str(e)}"}

    results = []

    for filename in os.listdir(gallery_dir):
        img_path = os.path.join(gallery_dir, filename)
        if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
            continue
        try:
            rep = DeepFace.represent(img_path=img_path, model_name="VGG-Face")[0]
            dist = dst.findCosineDistance(query_vec, rep["embedding"])
            if dist <= 0.4:
                results.append({
                    "filename": filename,
                    "distance": round(dist, 4)
                })
        except:
            continue

    results.sort(key=lambda x: x["distance"])
    return results

def verify_faces(img1_path, img2_path):
    try:
        result = DeepFace.verify(img1_path, img2_path, model_name='VGG-Face')
        return result
    except Exception as e:
        return {"error": str(e)}