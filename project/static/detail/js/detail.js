$(document).ready(function () {
    // http://127.0.0.1:8000/detail/104751/4217/
    var url = location.href;
    spanIdStr = "yellow" + url.split("/")[4]
    $yellowSpan = $(document.getElementById(spanIdStr))
    $yellowSpan.addClass("yellowSlide")


    //点击分类和排序
    $("#allTypeBtn").bind("click", function () {
        $("#typediv").toggle();
        $("#sortdiv").hide();
    });
    $("#allSortBtn").bind("click", function () {
        $("#sortdiv").toggle();
        $("#typediv").hide();
    });
    $("#typediv").bind("click", func);
    $("#sortdiv").bind("click", func);
    function func() {
        $(this).hide()
    }


    //给分类添加颜色
    aIdStr = "type" + url.split("/")[5]
    $a = $(document.getElementById(aIdStr))
    $a.addClass("abg")
});