from deepface import DeepFace

def verify_faces(img1_path, img2_path):
    try:
        result = DeepFace.verify(img1_path, img2_path, model_name='VGG-Face')
        return result
    except Exception as e:
        return {"error": str(e)}