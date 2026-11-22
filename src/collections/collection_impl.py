from typing import Any, Iterator, TypeVar, Generic, Self

# restrict generic type T to only accept given types
T = TypeVar('T', str, int, 'Collection[int]', 'Collection[str]')

class Collection(Generic[T]):
    """
    Generic collection class of type T with basic collection operations.
    See: https://sgra64.github.io/py-fun.github.io/src.collections.html.
    """

    def __init__(self, *args, asSet=False):
        """
        Constructor of a Collection.

        Args:
            args: elements added to the Collection including
            number or string literals, sets and lists.
        """
        self._items = set() if asSet else list()
        for arg in args:
            self.add(arg)

    def add(self, item: T) -> Self:
        """
        Add an element of type T to the collection.

        Args:
            item: element to add to the collection.

        Returns:
            Chainable self-reference to the collection with the element added.
        """
        item = item if not isinstance(item, set | dict) else frozenset(item)
        if isinstance(self._items, list):
            self._items.append(item)
        else:
            # list cannot be added to a set since lists are mutable and therefore unhashable.
            self._items.add(item if not isinstance(item, list) else tuple(item))
        return self

    def contains(self, item: Any) -> bool:
        """
        Test that an item or subset exists in the collection.

        Args:
            item: element to test that it is in the collection.

        Returns:
            True if element is in the collection, False otherwise.
        """
        # Match the internal representation used by add().
        if isinstance(item, set | dict):
            item = frozenset(item)
        elif isinstance(self._items, set) and isinstance(item, list):
            item = tuple(item)

        return item in self._items

    def size(self) -> int:
        """
        Returns the number of items in the collection.

        Returns:
            the number of items in the collection.
        """
        return len(self._items)

    @classmethod
    def zip(cls, l1: 'Collection[list]', l2: 'Collection[list]') -> 'Collection[tuple]':
        """
        Return a new collection of two-item tuples zipped from the input collections.

        Args:
            c1: input Collection from which the left element is taken.
            c2: input Collection from which the right element is taken

        Returns:
            Collection of pairs zipped from each input Collection.
        """
        return cls(*(tuple(pair) for pair in zip(l1, l2)))

    def pset(self) -> list[set[T]]:
        """
        Return the power set of this Collection using backtracking.

        Returns:
            The power set of this Collection.
        """
        return list(self.pset_gen())

    def pset_gen(self) -> Iterator[set[T]]:
        """
        Generator that yields each subset using backtracking.
        
        Returns:
            Generator object for the power set of this Collection.
        """
        items = list(dict.fromkeys(self._items))
        subset = set()

        def backtrack(index):
            if index == len(items):
                yield set(subset)
                return

            yield from backtrack(index + 1)

            subset.add(items[index])
            yield from backtrack(index + 1)
            subset.remove(items[index])
        yield from backtrack(0)

    def perm(self) -> list[list[T]]:
        """
        Return all permutations of this Collection.

        Returns:
            The list of permutations of this Collection.
        """
        return list(self.perm_gen())

    def perm_gen(self) -> Iterator[list[T]]:
        """"
        Generator that yields permutations using backtracking.

        Returns:
            Generator object for the list of permutations of this Collection.
        """
        items = list(self._items)
        permutation = []
        used = [False] * len(items)

        def backtrack():
            if len(permutation) == len(items):
                yield list(permutation)
                return

            for i in range(len(items)):
                if not used[i]:
                    used[i] = True
                    permutation.append(items[i])

                    yield from backtrack()

                    permutation.pop()
                    used[i] = False

        yield from backtrack()


    def __contains__(self, item: Any) -> bool:
        """Checks if an item or subset exists in the collection (in-operator)."""
        return item in self._items

    def __len__(self) -> int:
        """Returns the number of items in the collection, invoked by len()."""
        return len(self._items)

    def __iter__(self) -> Iterator[Any]:
        """Returns an iterator over the items in the collection, invoked in loops."""
        return iter(self._items)

    def __repr__(self):
        """Custom representation for str() that formats inner frozenSets as { }."""
        elements = []
        for item in self._items:
            if isinstance(item, set | frozenset):
                elements.append(f"{{{", ".join(repr(e) for e in item)}}}")
            else:
                elements.append(repr(item))
        # 
        r = f"{', '.join(elements)}"
        return f"[{r}]" if isinstance(self._items, list) else f"{{{r}}}"
