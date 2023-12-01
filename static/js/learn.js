const search = () => {
    const searchBox = document.getElementById("search-bar").value.toUpperCase();
    const langList = document.getElementById("language");
    const languages = document.querySelectorAll(".lang-card");
    const lname = document.getElementsByTagName("h3")

    for(var i = 0; i < lname.length; i++) {
        let match = languages[i].getElementsByTagName('h3')[0];

        if(match) {
            let textValue = match.textContent || match.innerHTML

            if(textValue.toUpperCase().indexOf(searchBox) > -1) {
                languages[i].style.display = "";
            } else {
                languages[i].style.display = "none";
            }
        }
    }
}