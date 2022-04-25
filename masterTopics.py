import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
			if L[i].get("Field") < R[j].get("Field"):
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
			if arr[mid].get("Field") == x:
				return arr[mid].get("Topic")
	# If x is greater, ignore left half
			elif arr[mid].get("Field") < x:
				l = mid + 1
	# If x is smaller, ignore right half
			else:
				r = mid - 1
	# If we reach here, then the element was not present
		return -1

def main():
  df = pd.read_csv("masterTopics.csv")
  #infile = open("MasterTopics.txt", 'r')
  #topics = infile.readlines()
  df.drop(df.columns[4:252], axis=1, inplace=True)
  #for column in df.columns[:3]:
  itr = df.loc[df['Division'].isin([30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52])]

#needs some work
  result=[]
  user=input("Which topic are you searching for:")
  df.mergeSort(result)
  nodeID = binarysearchByValue(result, 0, len(result)-1, user)
  #Repeat for every Division
  if nodeID == df.loc[df['Group'].startswith == 'AGR']:
    if np.isnan(itr,where=False):
      for item in df.get(''):
        df['Field']=item.get("Field")
        df['Topic']=item.get("Topic")
      result.append()
    else:
        return("")
  #print(itr.shape)
  print(itr)
  print(nodeID)
main()
