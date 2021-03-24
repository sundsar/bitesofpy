from collections import Counter


def calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    c = Counter([s for s in sequence.lower() if s in 'agct'])
    gc_content = c['g'] + c['c']
    res = gc_content / (sum(c.values())) * 100
    return(round(res, 2))
