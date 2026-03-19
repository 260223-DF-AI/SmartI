import pytest
from generators import read_lines, batch, filter_by
from dotenv import load_dotenv
import os

def test_batch_correct_sizes():
    """Batch should yield correct batch sizes."""
    result = list(batch(range(7), 3))
    print(result)
    assert len(result) == 3
    assert len(result[0]) == 3
    assert len(result[2]) == 1

def test_filter_by_predicate():
    """Filter should only yield matching items."""
    testList = ["Generators", "and", "decorators", "are", "things", "I", "had", "first", "come", 'across', "at", "revature", "The", "closest", "thing", "to", "this", "that", "I", "learnt", "is", "the", "decorator", "pattern"]
    stopwords = [
    "a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "aren't", 
    "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can't", 
    "cannot", "could", "couldn't", "didn't", "do", "does", "doesn't", "doing", "don't", "down", "during", "each", 
    "few", "for", "from", "further", "had", "hadn't", "had not", "has", "hasn't", "have", "haven't", "having", "he", 
    "he'd", "he'll", "he's", "her", "here", "here's", "hereafter", "hers", "herself", "how", "how's", "howbeit", "I", 
    "I'd", "I'll", "I'm", "I've", "if", "in", "in front of", "inside", "instead of", "into", "is", "isn't", "it", 
    "it's", "its", "itself", "let's", "me", "more", "most", "much", "must", "mustn't", "my", "myself", "needn't", 
    "need not", "neither", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other", "ought", "oughtn't", 
    "our", "ours", "ourselves", "out", "outside", "over", "should", "shouldn't", "should not", "so", "some", "than", 
    "that", "that's", "that'd", "will", "done."]
    result = list(filter_by(testList, lambda word: word not in stopwords))
    assert result == [word for word in testList if word not in stopwords]

def test_read_lines_skips_empty():
    """Read lines should skip empty lines."""
    load_dotenv()
    filepath = os.getenv("FILEPATH")
    lines = list(read_lines(filepath))
    assert len(lines) == 3
    assert lines == ["Hello", 'This is my file', 'With empty lines for testing']