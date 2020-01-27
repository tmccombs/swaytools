class Node:
    def __init__(self, data: dict):
        self._data = data
        self._nodes = map(Node, data.get('nodes', []))
        self._floating_nodes = map(Node, data.get('floating_nodes', []))

    def __getitem__(self, key):
        return self._data[key]

    def get(self, key, default=None):
        return self._data.get(key, default)

    def descendants(self):
        '''
        Iterate through all descendents of the node in depth-first order.

        Floating nodes are iterated after normal nodes.
        '''
        for node in self._nodes:
            yield node
            yield from node.descendants()
        for node in self._floating_nodes:
            yield node
            yield from node.descendants()

    def views(self):
        '''
        Find all descendants that are "views". That is, they are named containers.
        '''
        for node in self.descendants():
            if node.is_view():
                yield node

    def is_view(self):
        '''
        Check if the window is a view. That is, if it is a named container.
        '''
        ctype = self._data['type']
        return (ctype == 'con' or ctype == 'floating_con') and self._data.get('name')
