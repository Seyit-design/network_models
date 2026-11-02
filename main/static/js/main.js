// Umumy animasiýa funksiýalary
function animatePacket(layerFrom, layerTo) {
    // Paket animasiýasy
    console.log(`Paket ${layerFrom} - ${layerTo} aralykda hereket edýär`);
}

// Gatlaklary görkezmek üçin
$(document).ready(function() {
    // Her bir gatlak kartasyna animasiýa goşmak
    $('.layer-card').addClass('layer-transition');
});