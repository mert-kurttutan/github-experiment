def get_version_dict(file_path):
    # reads json file and returns the version number
    import json
    with open(file_path) as json_file:
        data = json.load(json_file)
    return data
def flatten_dict(d):
    x = []
    for k, v in d.items():
        for i in v:
            x.append({"numpy_version": k, "python_version": i})
    return x

if __name__ == '__main__':
    import argparse
    # take single cli integer argument
    parser = argparse.ArgumentParser(description="This script takes a single integer argument")
    parser.add_argument("integer", type=int, help="an integer")
    args = parser.parse_args()
    version_id = args.integer

    file_path = '.github/version_map.json'
    version_dict = get_version_dict(file_path)
    version_list = flatten_dict(version_dict)
    print(f"version with id: {version_id} is {version_list[version_id]}")