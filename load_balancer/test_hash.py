from consistent_hash import ConsistentHash

servers = ["S1", "S2", "S3"]

ring = ConsistentHash(servers)

for client_id in [101, 202, 303, 404, 101]:
    print(client_id, "->", ring.get_server(client_id))