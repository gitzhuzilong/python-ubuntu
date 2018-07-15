$(document).ready(function () {
    $(".ischose").bind("click",function () {
        var cartid = $(this).attr("cartid");
        $.post("/changecart2/", {"cartid":cartid}, function (data,status) {
            if (data.error == 0) {
                if (data.flag) {
                    $(document.getElementById(cartid)).html("√")
                } else {
                    $(document.getElementById(cartid)).html("")
                }
            }
        });
    });

   $("#ok").bind("click", function () {
       var f = confirm("不减肥了？");
       if (f) {
           $.post("/order/", function (data, status) {
               if(data.error == 0){
                   location.href = "http://127.0.0.1:8000/cart/"
               }
           });
       }
   }) ;
});