from flask import Blueprint, request, jsonify
from .service import verify_faces
import traceback

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