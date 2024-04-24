import uuid


def generate_custom_uuid(prefix):
    """
    Generates a custom UUID based on a prefix

    Args:
        prefix(required, string): A prefix to generate a UUID for:

    Returns:
        str: A custom UUID based on a prefix
    """

    # Generate a UUID with length of 10
    base_uuid = uuid.uuid4().hex[:10]

    return f'{prefix}-{base_uuid}'
