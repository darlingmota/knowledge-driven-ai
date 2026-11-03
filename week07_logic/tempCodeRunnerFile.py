inferred = set(known_facts)

    changed = True
    while changed:
        changed = False
        for conditions, conclusion in rules:
            # rule fires if every condition is already known
            if all(c in inferred for c in conditions) and conclusion not in inferred:
                inferred.add(conclusion)
                changed = True  # new fact so go through the rules again
    return inferred