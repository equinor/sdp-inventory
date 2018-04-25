$(document).ready(function() {
    $(".hostTableItem").click(function() {
        $(this).next(".hostTableItemDetails").toggle();
    });
    $(".hostTableItemDetails").click(function() {
        $(this).hide();
    });
    $("#expandAll").click(function() {
        $(".hostTableItemDetails").show();
    });
    $("#collapseAll").click(function() {
        $(".hostTableItemDetails").hide();
    });
});
