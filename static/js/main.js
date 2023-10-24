const pdfUrl = "static/Git_course_IDMC_UL.pdf"

function toggleCollapsibleParagraphs() {
    var paragraphs = document.getElementById("collapsible-paragraphs");
    var button = document.getElementById("collapse-button");
    if (paragraphs.style.display === "none") {
        paragraphs.style.display = "block";
        button.innerHTML = "Read less";
    } else {
        paragraphs.style.display = "none";
        button.innerHTML = "Read more";
    }
}




