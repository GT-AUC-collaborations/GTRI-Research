import networkx as nx
from networkx.readwrite import json_graph
import sys
import json

dot_output_name = "topic_connection.json"
## Takes dot file and dumps into a json file
def dot_to_json(dot_file):
  dot_graph = nx.nx_pydot.read_dot(dot_file)
  out_file = open(dot_output_name, "w")
  json.dump(json_graph.node_link_data(dot_graph),out_file)

# # // change input dot file here:
# dot_to_json("topic_connection.dot")

## Uncomment after topic_data.json is created:
# # // change input json file here:
# input_file=open('topic_connection.json', 'r')
# # // change output json files here:
# node_output_file=open('topic_data_cleaned.json', 'w')
# links_output_file=open('topic_connection_cleaned.json', 'w')
# json_decode=json.load(input_file)

# ## Rewrites json file
# node_result = []
# for item in json_decode.get('nodes'):
#   node_dict = {}
#   node_dict['id']=item.get('id')
#   node_dict['label']=item.get('label')
#   node_dict['weight']=item.get("weight")
#   node_result.append(node_dict)

# json.dump(node_result, node_output_file)


# link_result = []
# for item in json_decode.get('links'):
#   link_dict = {}
#   link_dict["weight"]=item.get("weight")
#   link_dict["source"]=item.get("source")
#   link_dict["target"]=item.get("target")
#   link_result.append(link_dict)

# json.dump(link_result, links_output_file)



