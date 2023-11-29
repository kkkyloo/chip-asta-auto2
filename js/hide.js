function toggleText() {
    var moreText = document.getElementById("moreText");
    var btnText = document.getElementById("toggleBtn");
    var imgElement = document.querySelector('.img_none');
    var mobNavbar = window.getComputedStyle(navmob);

    var computedStyle = window.getComputedStyle(moreText);

    if (computedStyle.display === "none" && mobNavbar.display === "none") {
        moreText.style.display = "inline";
        btnText.innerHTML = "Скрыть";
        imgElement.style.marginTop = '23vh';
        imgElement.style.height = '60vh';
    } 
    else if (computedStyle.display === "inline" && mobNavbar.display === "none" ) {
        moreText.style.display = "none";
        btnText.innerHTML = "Подробнее";
        imgElement.style.marginTop = '3vh';
        imgElement.style.height = '40vh';

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

function toggleText2() {
    var moreText = document.getElementById("moreText2");
    var btnText = document.getElementById("toggleBtn2");
    var imgElement = document.querySelector('.img_none2');
    var mobNavbar = window.getComputedStyle(navmob);

    var computedStyle = window.getComputedStyle(moreText);

    if (computedStyle.display === "none" && mobNavbar.display === "none") {
        moreText.style.display = "inline";
        btnText.innerHTML = "Скрыть";
        imgElement.style.height = '62vh';
    } 
    else if (computedStyle.display === "inline" && mobNavbar.display === "none" ) {
        moreText.style.display = "none";
        btnText.innerHTML = "Подробнее";
        imgElement.style.height = '40vh';
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


