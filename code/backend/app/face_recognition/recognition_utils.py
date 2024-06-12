"""
import boto3
import os
from PIL import Image
import io
from dotenv import load_dotenv

# Load environment variables from the provided environment file
load_dotenv("aws.env")

rekognition = boto3.client(
    'rekognition',
    region_name=os.getenv("AWS_DEFAULT_REGION"),  # Use the environment variable from environment.env
    aws_access_key_id=os.getenv("S3_KEY"),
    aws_secret_access_key=os.getenv("S3_SECRET"),
)

s3 = boto3.client(
    "s3",
    region_name=os.getenv("AWS_DEFAULT_REGION"),  # Use the environment variable from environment.env
    aws_access_key_id=os.getenv("S3_KEY"),
    aws_secret_access_key=os.getenv("S3_SECRET"),
)

def resize_image(image, basewidth=300):
    img = Image.open(image)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    return img

def compare_faces(uploaded_file_path):
    bucket = os.getenv("COMPARE_BUCKET")
    matches = []
    for obj in s3.list_objects(Bucket=bucket)['Contents']:
        response = rekognition.compare_faces(
            SourceImage={
                'S3Object': {
                    'Bucket': os.getenv("UPLOAD_BUCKET"),
                    'Name': uploaded_file_path
                }
            },
            TargetImage={
                'S3Object': {
                    'Bucket': bucket,
                    'Name': obj['Key']
                }
            },
            SimilarityThreshold=99
        )
        if response['FaceMatches']:
            matches.append(obj['Key'])
    return matches

    """