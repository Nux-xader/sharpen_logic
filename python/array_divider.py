def main(count_subtask, list_obj):
	return list(map(lambda x: list_obj[x:x+count_subtask], range(0, len(list_obj), count_subtask)))

# sample to use
if __name__ == '__main__':
	my_task_obj = [f"Obj {x}" for x in range(1, 11)]
	count_subtask = 3
	result = main(count_subtask, my_task_obj)
	print(result) # Do something