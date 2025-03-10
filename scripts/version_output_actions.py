# reads json file and prints the version number


import json

def json_to_output_versions(file_path):

    # now use pydantic to validate the json file, where k is version number and v is the list of version number
    from pydantic import BaseModel
    from pydantic.fields import Field
    class VersionMap(BaseModel):
        version: str =  Field(pattern=r'^\d+\.\d+\.\d+$')
        versions: list[str] = list[Field(pattern=r'^\d+\.\d+\.\d+$')]
    
    with open(file_path) as json_file:
        data = json.load(json_file)
        output_dict = {"include": []}
        for k, v_list in data.items():
            for v in v_list:
                output_dict["include"].append({"numpy_version": k, "python_version": v})
        print(json.dumps(output_dict, indent=4))



if __name__ == '__main__':
    file_path = '.github/version_map.json'
    json_to_output_versions(file_path)