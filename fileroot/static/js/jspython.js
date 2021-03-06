// 
// Integer Extension
// 

int = parseInt;

// 
// String Extension
// 

String.prototype.find =  String.prototype.indexOf;
String.prototype.format = function() {
	var args = arguments;
	var new_text = this;
	for (var i=0;i<args.length;i++) {
		if (new_text.indexOf("{}") != -1) {
			new_text = new_text.replace("{}", args[i]);
		}
	}

	return new_text;
}
String.prototype.remove = function (str) {
	return this.replace(new RegExp(str.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), "g"), "");
}
String.prototype.rreplace = function (from, to) {
	return this.replace(new RegExp(from.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), "g"), to);
}

str = String;

// 
// Array Extension
// 

Array.prototype.index = Array.prototype.indexOf;
Array.prototype.append = Array.prototype.push;
Array.prototype.remove = function(ele, num) {
	num = num==undefined? 1: num;
	if (num <= 0) {
		throw "The number of element remove need to be bigger than 0";
	}
	
	var find = this.index(ele);
	var removed = 0;
	while (find >= 0 && (removed < num || num == -1)) {
		this.splice(find, 1);
		find = this.index(ele);
		removed += 1;
	}
}

Array.prototype.count = function(ele) {
	var count = 0;
	for (var i=0;i<this.length;i++) {
		if (this[i] == ele) {
			count += 1;
		}
	}

	return count;
}

Array.prototype.pop = function(index) {
	index = index==undefined? (this.length - 1): index;
	if (this[index] == undefined) {
		throw "Index must not bigger than list length";
	}

	return this.splice(index, 1)[0];
}

Array.prototype.insert = function(index, ele) {
	if (index == undefined || ele == undefined) {
		throw "Missing argument";
	}

	this.splice(index, 0, ele);
}

// 
// Random Module
// 

var Random = function() {
	var self = this;

	this.randint = function(start_num, end_num) {
		return int(Math.random() * (end_num - start_num + 1) + start_num);
	}

	this.random = function() {
		return Math.random();
	}

	this.shuffle = function(list) {
		var j, x, i;
		for (i = list.length - 1; i > 0; i--) {
			j = Math.floor(Math.random() * (i + 1));
			x = list[i];
			list[i] = list[j];
			list[j] = x;
		}
	}

	this.choice = function(list) {
		return list[self.randint(0, list.length - 1)];
	}

	this.sample = function(list, num) {
		if (num > list.length) {
			throw "Sample larger than population";
		}

		var picks = [];

		for (i=0;i<num;i++) {
			pick = self.choice(list);

			while (picks.index(pick) >= 0) {
				pick = self.choice(list);
			}

			picks.push(pick);
		}

		return picks;
	}
}

random = new Random();

// For loop
foreach = function (iterate_object, iterate_function) {
	keys = Object.keys(iterate_object);
	for (i=0;i<keys.length;i++) {
		iterate_function(keys[i], iterate_object[keys[i]]);
	}
}

// Date
Date.prototype.strftime = function (format) {
	str = format.replace("%Y", this.getFullYear());
	str = str.replace("%m", this.getMonth() + 1);
	str = str.replace("%d", this.getDate());
	str = str.replace("%H", this.getHours());
	str = str.replace("%M", this.getMinutes());
	str = str.replace("%S", this.getSeconds());
	return str;
}
