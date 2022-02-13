def main(count_subtask, list_obj):
	result = []
	subres = []
	for x, y in enumerate(list_obj):
		subres.append(y)
		if (x+1)%count_subtask == 0:
			result.append(subres)
			subres = []
	if len(subres) > 0:
		result.append(subres)

	return result

# sample to use
if __name__ == '__main__':
	my_task_obj = [f"Obj {x}" for x in range(1, 11)]
	count_subtask = 3
	result = main(count_subtask, my_task_obj)
	print(result) # Do something