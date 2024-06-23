from apiflask import Schema
from marshmallow import fields, validate

class EventSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    date = fields.Date(required=True)

class GallerySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    photos = fields.List(fields.Nested('PhotoSchema', only=("id", "filename")))

class PhotoSchema(Schema):
    id = fields.Int(dump_only=True)
    filename = fields.Str(dump_only=True)  # Only dump the filename, do not require it in the input
    gallery_id = fields.Int(required=True)  # Ensure gallery_id is required
    gallery = fields.Nested('GallerySchema', dump_only=True)

