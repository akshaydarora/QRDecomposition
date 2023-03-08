import json
import os

class Initializer(object):

    def load_file(self,dir_path,file_name)->dict:

        with open(os.path.join(dir_path,file_name),"r",encoding='utf-8') as f:
            file_data=json.load(f)

        return file_data 

    def initialize_vars(self):
        
        method_config = self.load_file(dir_path="config",
                        file_name="method_config.json")
        input_config = self.load_file(dir_path="config",
                            file_name="input_config.json")
        method_type = input_config["method_type"]
        method_name = input_config["method_name"]
        input_data = self.load_file(dir_path=method_config[method_type][method_name]["input"]["file_dir"],
                            file_name=method_config[method_type][method_name]["input"]["file_name"])
        constraint_matrix = input_data["constraint_matrix"]
        output_data = self.load_file(dir_path=method_config[method_type][method_name]["output"]["file_dir"],
                            file_name=method_config[method_type][method_name]["output"]["file_name"])
        rhs_matrix = output_data["rhs_matrix"]

        return constraint_matrix, rhs_matrix, method_config, input_config