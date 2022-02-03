class Counter:
    """
    Counts occurrence count of elements.
    """

    def count(elements):
        """
        Counts occurrence of each element for given elements.
        
        Args:
            elements List of elements which should be counted.

        Returns:
            Element -> occurrence count mapping.
        """

        occurrence_count = {}

        for element in elements:
            if element not in occurrence_count:
                occurrence_count[element] = 1
            else:
                occurrence_count[element] += 1

        return occurrence_count

    def most_common(elements):
        """
        Returns most common element(s).
        
        Args:
            elements List of elements in which most common element(s) should be found.

        Returns:
            List of Most common element(s). In case of same occurence counts, returns all the most common elements.
        """

        occurrence_counts = Counter.count(elements)

        max_occurrence_count = 0
        most_common_elements = []

        for element, occurrence_cnt in occurrence_counts.items():
            if occurrence_cnt > max_occurrence_count:
                max_occurrence_count = occurrence_cnt
                most_common_elements = [element]
            elif occurrence_cnt == max_occurrence_count:
                most_common_elements.append(element)

        return most_common_elements
