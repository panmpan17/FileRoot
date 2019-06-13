host = window.location.origin + "/rest/";

function join_path () {
	var new_path = ""
	for (path of arguments) {
		if (!new_path.endsWith("/")) {
			new_path += "/";
		}
		new_path += path;
	}
	return new_path;
}

function DisplayFiles (files, dirs, hidden_files, hidden_dirs) {
	var html = "";

	files = files.concat(hidden_files);
	dirs = dirs.concat(hidden_dirs);

	$.each(dirs, function (_, dir) {
		html += `<li class="dir" data-blob-type="dir" data-blob="${dir}/" onclick="BlobClicked(this)">${dir}/</li>`
	});

	$.each(files, function (_, file) {
		html += `<li data-blob-type="file" data-blob="${file}" onclick="BlobClicked(this)">${file}</li>`
	});

	blob_list.innerHTML = html;
}

function GoToParentDir () {
	JumpToPath("...");
}

function JumpToPath (new_path) {
	var paths = join_path(path, new_path).split("/");
	paths.remove("");

	var params = decodeURIComponent($.param({rel_path: paths}));
	params = params.rreplace("...", "..");

	$.ajax({
		url: host + "tree/?" + params.remove("[]"),
		success: function (msg) {
			path = msg.rel_path.rreplace("..", "...");

			var rel_path = join_path("tree", path);
			if (!rel_path.endsWith("/")) {
				rel_path += "/";
			}

			window.history.pushState({}, "", rel_path);

			DisplayFiles(msg.files, msg.dirs, msg.hidden_files, msg.hidden_dirs);
		}
	})
}

function BlobClicked (ele) {
	var targetNode = $(ele);
	var blobType = targetNode.data("blob-type");
	var blob = targetNode.data("blob");

	if (blobType == "dir") {
		if (window.location.pathname.endsWith("/")) {
			JumpToPath(blob);
		}
		else {
			window.location.pathname += "/" + blob;
		}
	}
	else {
		console.log("show file", blob);
	}
}


$(document).ready(function () {
	DisplayFiles(files, dirs, hidden_files, hidden_dirs);

	path = window.location.pathname;
	path = path.remove("/tree/");
});