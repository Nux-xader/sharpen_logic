// please using node js for testing this function

function array_divider(count_sublist, data) {
	var result = [];
	var subres = [];

	for (var i=0; i < data.length; i++) {
		subres.push(data[i]);

		if ((i+1)%count_sublist == 0) {
			result.push(subres);
			subres = [];
		}
	}

	if (subres.length > 0) {
		result.push(subres);
	}

	// for x, y in enumerate(list_obj):
	// 	subres.append(y)
	// 	if (x+1)%count_subtask == 0:
	// 		result.append(subres)
	// 		subres = []
	// if len(subres) > 0:
	// 	result.append(subres)

	return result;
}

var my_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"];
var divided = array_divider(3, my_array);
console.log(divided);