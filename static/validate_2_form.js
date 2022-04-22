function validateForm() {
    let x = document.forms["myForm"]["name"].value;
    let a = document.forms["myForm"]["e_mail"].value;
    let b = document.forms["myForm"]["mob_no"].value;
    let c = document.forms["myForm"]["domain"].value;
    let d = document.forms["myForm"]["coll_name"].value;
    let e = document.forms["myForm"]["branch"].value;
    let f = document.forms["myForm"]["month"].value;
    let g = document.forms["myForm"]["gender"].value;
    let h = document.forms["myForm"]["address"].value;
    let i = document.forms["myForm"]["trans_id"].value;

    if (x == "") {
        alert("Name must be filled out");
        return false;
    }
    if (a == "") {
        alert("Email must be filled out");
        return false;
    }
    if (b == "") {
        alert("Mobile number must be filled out");
        return false;
    }
    if (c == "0") {
        alert("Internship must be filled out");
        return false;
    }
    if (d == "") {
        alert("College Name must be filled out");
        return false;
    }
    if (e == "") {
        alert("Branch must be filled out");
        return false;
    }
    if (f == "0") {
        alert("Month must be filled out");
        return false;
    }
    if (g == "0") {
        alert("Gender must be filled out");
        return false;
    }
    if (h == "") {
        alert("Address must be filled out");
        return false;
    }
    if (i == "") {
        alert("Transaction Id must be filled out");
        return false;
    }

}