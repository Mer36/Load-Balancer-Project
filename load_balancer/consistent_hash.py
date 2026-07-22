import hashlib
import bisect


class ConsistentHash:

    def __init__(self, servers):

        self.ring = {}
        self.sorted_keys = []

        for server in servers:
            self.add_server(server)

    def hash_function(self, key):

        return int(
            hashlib.md5(
                str(key).encode()
            ).hexdigest(),
            16
        )

    def add_server(self, server):

        for replica in range(10):

            virtual_node = (
                f"{server}#{replica}"
            )

            key = self.hash_function(
                virtual_node
            )

            self.ring[key] = server

            bisect.insort(
                self.sorted_keys,
                key
            )
    def get_server(self, request_id):

        if not self.sorted_keys:
            return None

        hash_key = self.hash_function(
            request_id
        )

        index = bisect.bisect(
            self.sorted_keys,
            hash_key
        )

        if index == len(self.sorted_keys):
            index = 0

        return self.ring[
            self.sorted_keys[index]
        ]