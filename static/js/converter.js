$(document).ready(function () {
    $('button[name=trigger_converter]').click(function () {
        var cLeft = this.id;
        var cValue = $(this).data().value;
        var cRight = $('select[id=' + this.id + '').val();
        var resultBlock = $('span[id=' + this.id + '');
        $.ajax({
            url: '/convert',
            data: {'cLeft': cLeft, 'cRight': cRight, 'cValue': cValue}
        }).done(function (response) {
            resultBlock.text(response.result);
        });
    })
});