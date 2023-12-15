function deleteStudent(id) {
    var result = confirm("Are you sure you want to delete this student with id $id?");
    if (result) {     
        window.location = "/delete/" + id;
    }
}