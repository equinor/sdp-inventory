$(document).ready(function() {
    $(".hostTableItem").click(function() {
        $(this).next(".hostTableItemDetails").toggle();
    });
    $(".hostTableItemDetails").click(function() {
        $(this).hide();
    });
});
