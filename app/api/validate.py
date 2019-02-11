from jsonschema import Draft4Validator

REVIEW_SCHEMA = {
    "$schema": "http://json-schema.org/schema#",
    "type": "object",
    "properties": {
        "marketplace": {"type": "string"},
        "customer_id": {"type": "string"},
        "product_id": {"type": "string"},
        "product_title": {"type": "string"},
        "product_category": {"type": "string"},
        "star_rating": {"type": "number"},
        "review_headline": {"type": "string"},
        "review_body": {"type": "string"}
    }
}


def validate(schema, payload):
    errs = [err.message for err in Draft4Validator(schema).iter_errors(payload)]
    return not any(errs), errs


def validate_create_reivew(payload):
    return validate(REVIEW_SCHEMA, payload)
