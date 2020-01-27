from .ipc import I3Ipc


class WindowInfo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        with I3Ipc() as i3:
            self.tree = i3.get_raw_tree()

    def _contains_point(self, node):
        rect = node['rect']
        return ((rect['x'] < self.x < rect['x'] + rect['width'])
                and (rect['y'] < self.y < rect['y'] + rect['height']))

    def _process_node(self, node):
        for n in node['nodes']:
            if self._contains_point(n):
                if n.get("visible", False):
                    self._print_node(n)
                    return True
                if self._process_node(n):
                    return True

    def _process_workspace(self, workspace):
        for n in reversed(workspace['floating_nodes']):
            if self._contains_point(n):
                self._print_node(n)
                return
        self._process_node(workspace)

    def _process_output(self, out):
        active_ws = out['current_workspace']
        for ws in out['nodes']:
            if ws['name'] == active_ws:
                self._process_workspace(ws)
                break

    def _print_node(self, node):
        print(f"title={node['name']}")
        print(f"con_id={node['id']}")
        print(f"app_id={node.get('app_id', 'null')}")

        pid = node.get("pid")
        if pid:
            print(f"pid={pid}")
        win_id = node.get("window")
        if win_id:
            print(f"id={win_id}")
        win_props = node.get("window_properties")
        if win_props:
            print(f"class={win_props['class']}")
            print(f"instance={win_props['instance']}")
            print(f"window_role={win_props['window_role']}")
        if node.get("urgent"):
            print("urgent")
        if node.get("focused"):
            print("focused")
        print()

    def print_info(self):
        'Print info for all nodes that contain the point'
        for output in self.tree['nodes']:
            if output.get('active') and self._contains_point(output):
                assert output['type'] == 'output', 'Unexpected child of root'
                self._process_output(output)
                break


def main():
    import subprocess

    point = subprocess.run(['slurp', '-f', '%x,%y', '-p'], check=True, text=True, capture_output=True).stdout
    (x, y) = map(int, point.split(','))
    info = WindowInfo(x, y)
    info.print_info()

