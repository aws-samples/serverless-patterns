def lambda_handler(event, context):
    """Standard Lambda function that processes sample values."""
    values = event.get("values", [])
    operation = event.get("operation", "sum_and_average")

    if not values:
        return {"error": "No values provided"}

    total = sum(values)
    average = total / len(values)
    maximum = max(values)
    minimum = min(values)

    return {
        "operation": operation,
        "count": len(values),
        "sum": total,
        "average": average,
        "max": maximum,
        "min": minimum,
    }
