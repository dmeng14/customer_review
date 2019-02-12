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
    },
    "required": ["product_id", "star_rating"],
}

UPDATE_REVIEW_SCHEMA = {
    "$schema": "http://json-schema.org/schema#",
    "type": "object",
    "properties": {
        "review_id": {"type": "string"},
    },
    "required": ["review_id"],
}


def validate(schema, payload):
    errs = [err.message for err in Draft4Validator(schema).iter_errors(payload)]
    return not any(errs), errs


def validate_create_reivew(payload):
    return validate(REVIEW_SCHEMA, payload)


def validate_update_reivew(payload):
    return validate(UPDATE_REVIEW_SCHEMA, payload)
