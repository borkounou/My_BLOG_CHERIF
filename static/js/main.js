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

// let pdfjsLib = window['static/js/pdfjs/build/pdf'];
const container = document.getElementById('pdfViewer');

pdfjsLib.getDocument(pdfUrl).promise.then(function(pdf){
    for(let pageNumber=1; pageNumber<=pdf.numPages; pageNumber){

        pdf.getPage(pageNumber).then(function(page){
            const canvas = document.createElement('canvas');
            container.appendChild(canvas);
            const viewport = page.getViewport({scale:1.5});
            canvas.width = viewport.width;
            canvas.height = viewport.height;
            const context = canvas.getContext('2d');

            page.render({
                canvasContext:context,
                viewport: viewport
            });

        });

    }
}).catch(function(error){console.error("Error loading Pdf", error)});





