from apiflask import Schema
from marshmallow import fields

class EventSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    date = fields.Date(required=True)

class PhotoSchema(Schema):
    id = fields.Int(dump_only=True)
    filename = fields.Str(dump_only=True)  # Only dump the filename, do not require it in the input
    gallery_id = fields.Int(required=True)  # Ensure gallery_id is required
    gallery = fields.Nested('GallerySchema', dump_only=True)

class GallerySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    cover_image_url = fields.Str(dump_only=True)
    photos = fields.List(fields.Nested(PhotoSchema), dump_only=True)