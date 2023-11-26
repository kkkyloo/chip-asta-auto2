function toggleText() {
    var moreText = document.getElementById("moreText");
    var btnText = document.getElementById("toggleBtn");
    var imgElement = document.querySelector('.img_none');
    var mobNavbar = window.getComputedStyle(navmob);

    var computedStyle = window.getComputedStyle(moreText);

    if (computedStyle.display === "none" && mobNavbar.display === "none" ) {
        moreText.style.display = "inline";
        btnText.innerHTML = "Скрыть";
        imgElement.style.height = '70vh';
    } 
    else if (computedStyle.display === "inline" && mobNavbar.display === "none" ) {
        moreText.style.display = "none";
        btnText.innerHTML = "Подробнее";
        imgElement.style.height = '36vh';
    }
    else if (computedStyle.display === "none" && mobNavbar.display === "block" ) {
        moreText.style.display = "inline";
        btnText.innerHTML = "Скрыть";
    }
    else{
        moreText.style.display = "none";
        btnText.innerHTML = "Подробнее";
    }
}
