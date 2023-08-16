$(document).ready(function(){
    $('span.day').html(function(){
        var date = new Date();
        return (date.getDate());
    });
    $('span.month').html(function(){
        var date = new Date();
        var month = ["January","February","March","April","May","June","July","August","September","October","November","December"][date.getMonth()];
        return month;
    });
});
