from generators import *
__cols: list = []
def create_pipeline(*stages):
    """
    Create a processing pipeline from multiple generator functions.
    
    Usage:
        pipeline = create_pipeline(
            read_lines,
            parse_json,
            filter_valid,
            transform
        )
        
        for result in pipeline('input.json'):
            save(result)
    """
    def pipeline(filepath):
        result = read_lines(filepath)
        for stage in stages:
            result = stage(result)
        return result
    return pipeline

    


# Example pipeline stages:

def parse_csv_line(lines):
    """Convert CSV lines to dictionaries."""
    linesDict = []
    for line in lines:
        cleanedLine: list = [entry.strip() for entry in line.split(",")]
        linesDict.append(dict(zip(__cols, cleanedLine)))
    return linesDict


def validate_records(records: list[dict]):
    """Yield only valid records, skip invalid ones."""
    return list(filter_by(records, lambda record: None not in record.values()))


def enrich_records(records):
    """Add calculated fields to each record."""
    # what calculated field? I don't have a generator method for this
    pass

def deduplicate(records: list[dict], key_field):
    """Yield unique records based on a key field."""
    fieldVals = set()
    unique = []
    for record in records:
        if(record[key_field] not in fieldVals):
            fieldVals.add(record[key_field])
    for i in range(len(fieldVals)):
        unique.append(next(filter_by_field(records, key_field, fieldVals.pop())))
    return unique
