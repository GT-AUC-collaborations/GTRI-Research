import networkx as nx
from networkx.readwrite import json_graph
import sys
import json

dot_output_name = "topic_data.json"
## Takes dot file and dumps into a json file
def dot_to_json(dot_file):
  dot_graph = nx.nx_pydot.read_dot(dot_file)
  out_file = open(dot_output_name, "w")
  json.dump(json_graph.node_link_data(dot_graph),out_file)

# // change input dot file here:
dot_to_json("topic_data.dot")

## Uncomment after topic_data.json is created:
# // change input json file here:
input_file=open('topic_data.json', 'r')
# // change output json file here:
output_file=open('topic_data_cleaned.json', 'w')
json_decode=json.load(input_file)

## Rewrites json file
result = []
for item in json_decode.get('nodes'):
    my_dict={}
    my_dict['id']=item.get('id')
    my_dict['label']=item.get('label')
    my_dict['weight']=item.get("weight")
    # print(my_dict)
    result.append(my_dict)

json.dump(result, output_file)
