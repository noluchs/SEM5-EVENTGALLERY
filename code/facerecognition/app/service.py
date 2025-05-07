from deepface import DeepFace
import os
from numpy import dot
from numpy.linalg import norm

def find_cosine_distance(source, target):
    return 1 - (dot(source, target) / (norm(source) * norm(target)))

def match_faces(query_path, gallery_dir):
    try:
        query_vec = DeepFace.represent(img_path=query_path, model_name="VGG-Face")[0]["embedding"]
    except Exception as e:
        return {"error": f"Fehler beim Encoding: {str(e)}"}

    # 💡 DEBUG: Pfad prüfen und anzeigen, welche Dateien da sind
    print(f"[DEBUG] Galeriepfad: {gallery_dir}")
    try:
        files = os.listdir(gallery_dir)
        print(f"[DEBUG] Dateien gefunden: {files}")
    except Exception as e:
        print(f"[ERROR] Konnte Galerie nicht lesen: {e}")
        return {"error": f"Galerie konnte nicht geladen werden: {str(e)}"}

    results = []

    for filename in files:
        print(f"[DEBUG] Prüfe Datei: {filename}")

        img_path = os.path.join(gallery_dir, filename)
        if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
            print(f"[SKIP] Nicht unterstützter Dateityp: {filename}")
            continue

        try:
            rep = DeepFace.represent(img_path=img_path, model_name="VGG-Face")[0]
            dist = find_cosine_distance(query_vec, rep["embedding"])
            print(f"[DEBUG] Distanz zu {filename}: {dist:.4f}")

            if dist <= 0.6:
                results.append({
                    "filename": filename,
                    "distance": round(dist, 4)
                })
        except Exception as e:
            print(f"[ERROR] Fehler bei {filename}: {e}")
            continue

    if not results:
        print("[INFO] Kein Match gefunden.")
        return {"message": "Kein passendes Gesicht gefunden."}

    results.sort(key=lambda x: x["distance"])
    return results

def verify_faces(img1_path, img2_path):
    try:
        result = DeepFace.verify(img1_path, img2_path, model_name='VGG-Face')
        return result
    except Exception as e:
        return {"error": str(e)}