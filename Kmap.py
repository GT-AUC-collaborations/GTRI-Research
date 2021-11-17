# Merge Sort
def mergeSort(arr):
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
			if L[i][1] < R[j][1]:
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
			if arr[mid][1] == x:
				return mid[0]
	# If x is greater, ignore left half
			elif arr[mid][1] < x:
				l = mid + 1
	# If x is smaller, ignore right half
			else:
				r = mid - 1
	# If we reach here, then the element was not present
		return -1

#Each list contains a unique id number. This line reads data from the file
maps = {}

kmapsFile = open("topic_data.txt","r", encoding='utf-8')
if not kmapsFile:
	print("Error:file not found")
else:
	for line in kmapsFile:
        (key, value) = line.split()
    # Read in column names
        maps[key] = value

		if len(line) > 1 and line[1] != "":
			line = (line[0].strip('""'), line[1].strip('""') & line[1].strip('label='))
			maps.append(line)
		line = kmapsFile.readline()
kmapsFile.close()

# Merge sort financial aid list
mergeSort(maps)

# User Menu
desired = input("What topic are you looking for")
ID = binarysearchByValue(maps, 0, len(maps)-1, desired)
print("kmap:", ID)