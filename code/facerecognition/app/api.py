from flask import Blueprint, request, jsonify
from .service import verify_faces
import traceback
import os

face_bp = Blueprint("face", __name__)

@face_bp.route("/face/verify", methods=["POST"])
def verify():
    try:
        img1 = request.files.get("img1")
        img2 = request.files.get("img2")

        if not img1 or not img2:
            return jsonify({"error": "Missing images"}), 400

        img1_path = f"/tmp/{img1.filename}"
        img2_path = f"/tmp/{img2.filename}"
        img1.save(img1_path)
        img2.save(img2_path)

        result = verify_faces(img1_path, img2_path)
        return jsonify(result)

    except Exception as e:
        print("Fehler in /face/verify:", e)
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


# --- /face/match route ---
@face_bp.route("/face/match", methods=["POST"])
def match():
    try:
        img = request.files.get("img")

        if not img:
            return jsonify({"error": "Kein Bild hochgeladen"}), 400

        temp_path = f"/tmp/{img.filename}"
        img.save(temp_path)

        # Verzeichnis der Vergleichsbilder im Container
        gallery_path = os.environ.get("GALLERY_PATH", "/app/gallery")

        from .service import match_faces
        matches = match_faces(temp_path, gallery_path)
        return jsonify(matches)

    except Exception as e:
        print("Fehler in /face/match:", e)
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500