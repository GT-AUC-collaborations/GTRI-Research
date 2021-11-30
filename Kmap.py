import networkx as nx
from networkx.readwrite import json_graph
import sys
import json

# Merge Sort
def mergeSort(arr):
	# list contains dict with id, label, and weight
	# we will sort by label name
	 
	if len(arr) > 1:
	# Finding the mid of the array
		mid = len(arr)//2
	# Dividing the array elements
		L = arr[:mid]
	# into 2 halves
		R = arr[mid:]
	# Sorting the first half
		mergeSort(L)
	# Sorting the second half
		mergeSort(R)
		i = j = k = 0
	# Copy data to temp arrays L[] and R[]
		while i < len(L) and j < len(R):
		# 1 is the value in array
			# print("print L[i]", L[i].get("label"))
			#.get is to search for the label throughout the dicionary
			if L[i].get("label") < R[j].get("label"):
				arr[k] = L[i]
				i += 1
			else:
				arr[k] = R[j]
				j += 1
			k += 1
	# Checking if any element was left
		while i < len(L):
			arr[k] = L[i]
			i += 1
			k += 1
		while j < len(R):
			arr[k] = R[j]
			j += 1
			k += 1

#Binary Search
def binarysearchByValue(arr, l, r, x):
		while l <= r:
			mid = l + (r - l) // 2
	# Check if x is present at mid
			if arr[mid].get("label") == x:
				return arr[mid].get("id")
	# If x is greater, ignore left half
			elif arr[mid].get("label") < x:
				l = mid + 1
	# If x is smaller, ignore right half
			else:
				r = mid - 1
	# If we reach here, then the element was not present
		return -1

dot_output_name = "topic_data.json"
## Takes dot file and dumps into a json file
def dot_to_json(dot_file):
  dot_graph = nx.nx_pydot.read_dot(dot_file)
  out_file = open(dot_output_name, "w")
  json.dump(json_graph.node_link_data(dot_graph),out_file)

# change input dot file here:
dot_to_json("topic_data.dot")

## Uncomment after topic_data.json is created:
# change input json file here:
input_file=open('topic_data.json', 'r')
# change output json file here:
output_file=open('topic_data_cleaned.json', 'w')
json_decode=json.load(input_file)

## Rewrites json file
# since "nodes" is already a list, we can put the nodes into a list "result" by using the line:
# result = json_decode.get('nodes')

result = []
for item in json_decode.get('nodes'):
    my_dict={}
    my_dict['id']=item.get('id')
    my_dict['label']=item.get('label').strip('""')
    my_dict['weight']=item.get("weight")
    result.append(my_dict)

json.dump(result, output_file)

input_file.close()
output_file.close()

# User Menu
desired = input("What topic are you looking for?:")
mergeSort(result)
nodeID = binarysearchByValue(result, 0, len(result)-1, desired)
print(nodeID)

# Find child node of the variable desired
