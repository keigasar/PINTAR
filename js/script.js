document.addEventListener('DOMContentLoaded', function() {
    const url = 'pdfs/document.pdf';

    const loadingTask = pdfjsLib.getDocument(url);
    loadingTask.promise.then(function(pdf) {
        const container = document.getElementById('flipbook');
        for (let i = 1; i <= pdf.numPages; i++) {
            pdf.getPage(i).then(function(page) {
                const viewport = page.getViewport({ scale: 1 });
                const canvas = document.createElement('canvas');
                canvas.width = viewport.width;
                canvas.height = viewport.height;
                container.appendChild(canvas);
                
                const context = canvas.getContext('2d');
                const renderContext = {
                    canvasContext: context,
                    viewport: viewport
                };
                page.render(renderContext).promise.then(function() {
                    if (i === pdf.numPages) {
                        $(container).turn({
                            width: container.clientWidth,
                            height: container.clientHeight,
                            autoCenter: true
                        });
                    }
                });
            });
        }
    });
});
