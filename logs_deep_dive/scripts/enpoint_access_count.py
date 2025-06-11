import shlex

def extract_endpoint(log_split: list[str]):
    if len(log_split) < 7: return False
    endpoint = log_split[6]

    if endpoint.endswith('HTTP/1.1') or endpoint.endswith('HTTP/2'):
        return endpoint

    return False


if __name__ == "__main__":
    filename = "sample.log"
    endpoint_count = {}

    with open(filename) as f:
        for line in f:
            line = line.strip()
            line_split = shlex.split(line)
            endpoint = extract_endpoint(line_split)

            if endpoint:
                endpoint_count[endpoint] = endpoint_count.get(endpoint, 0) + 1

    print("================ Endpoint Counts ================")
    for k, v in endpoint_count.items():
        print('Endpoint: ', k)
        print('Count: ', v)
        print("\n")
            
            