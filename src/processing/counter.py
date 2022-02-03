class Counter:
    """
    Counts occurrence count of elements.
    """

    def count(objects):
        """
        Counts occurrence of each element for given elements.
        
        Args:
            elements List of elements which should be counted.

        Returns:
            Element -> occurrence count mapping.
        """

        occurrence_count = {}

        for object in objects:
            if object not in occurrence_count:
                occurrence_count[object] = 1
            else:
                occurrence_count[object] += 1

        return occurrence_count