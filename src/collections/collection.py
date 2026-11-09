from typing import Self

class Collection[T]:
    """
    Generic collection class of type T with basic collection operations.
    """

    def contains(_self, e: T) -> bool:
        """
        Collection contains an element of type T.

        Args:
            e: element to test that it is in the collection.

        Returns:
            True if element is in the collection, False otherwise.
        """
        return False
    
    # def zip(_self, c1: Collection[Any], c2: Collection[Any], mode=0) -> Collection[tuple]:
    def zip(_self, c1: Self, c2: Self, mode=0) -> Self:
        """
        Create new Collection of tuple pairs of elements zipped from each
        input collection. Mode 0 ends the zip when one collection ends.
        Mode 1 has all elements and fills unmatched elements with None.

        Args:
            c1: the first input Collection.
            c2: the second input Collection.

        Returns:
            Collection of zipped pairs from each input Collection.
        """
        return []

    def pset(_self) -> set[set[T]]:
        """
        Create the power-set of this Collection.

        Returns:
            The power-set of this Collection.
        """
        return {}
    
    def perm(_self) -> list[list[T]]:
        """
        Create the list of permutations of this Collection.

        Returns:
            The list of permutations of this Collection.
        """
        return []

    def __init__(self, elements):
        pass
