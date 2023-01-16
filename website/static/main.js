$('#formId').on('keydown', function (e) {
    var keyCode = e.keyCode || e.which;
    var tag = e.target.tagName
    if (keyCode === 13 && tag !== "TEXTAREA") {
        console.log("Enter prevented")
        e.preventDefault();
        return false;
    } else {
        console.log("Enter is ok...")
    }
});