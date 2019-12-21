$(function () {

    $(".confirm").click(function () {

        console.log("change state");

        var $confirm = $(this);

        var $li = $confirm.parents("li");

        var cartid = $li.attr('cartid');

        $.getJSON("/App/changecartstate/", {'cartid': cartid}, function (data) {
            console.log(data);

            if (data.status === 'ok') {
                if (data.is_select) {
                    $confirm.find("span").find("span").html("√");
                }else{
                    $confirm.find("span").find("span").html("");
                }
                //改总价
                $('#totalprice').text(data.total_price)
                // $("#total_price").html(data['total_price']);
                // if (data['c_is_select']) {
                //     $confirm.find("span").find("span").html("√");
                // } else {
                //     $confirm.find("span").find("span").html("");
                // }
                // if (data['is_all_select']){
                //     $(".all_select span span").html("√");
                // }else{
                //     $(".all_select span span").html("");
                //
                // }
            }

        })

    })
    $(".addShopping").click(function () {

        var $addshopping = $(this);

        var $li = $addshopping.parents("li");

        var cartid = $li.attr("cartid");

        $.getJSON("/App/addshopping/", {"cartid": cartid}, function (data) {
            console.log(data);

            if (data.status === 'ok') {
                 $("#totalprice").text(data.total_price);
                 $addshopping.prev('span').text(data.cart_gooods_num)
            }

        })

    })
    $(".subShopping").click(function () {

        var $subshopping = $(this);

        var $li = $subshopping.parents("li");

        var cartid = $li.attr("cartid");

        $.getJSON("/App/subshopping/", {"cartid": cartid}, function (data) {
            console.log(data);

            if (data.status === 'ok') {
                 $("#totalprice").text(data.total_price);

                if (data.cart_gooods_num > 0) {
                    $subshopping.next('span').text(data.cart_gooods_num)
                } else {
                    $li.remove();
                }
            }

        })

    })

    $(".all_select").click(function () {

        var $all_select = $(this);

        var select_list = [];

        var unselect_list = [];

        $(".confirm").each(function () {

            var $confirm = $(this);

            var cartid = $confirm.parents("li").attr("cartid");

            if ($confirm.find("span").find("span").html().trim()) {
                select_list.push(cartid);
            } else {
                unselect_list.push(cartid);
            }

        })

        if (unselect_list.length > 0) {
            $.getJSON("/App/allselect/", {"cart_list": unselect_list.join("#")}, function (data) {
                console.log(data);
                if (data['status'] === 200) {
                    $(".confirm").find("span").find("span").html('√');
                    $all_select.find("span").find("span").html("√");
                    $("#total_price").html(data['total_price']);
                }
            })
        } else {
            if (select_list.length > 0) {
                $.getJSON("/App/allselect/", {"cart_list": select_list.join("#")}, function (data) {
                console.log(data);
                if (data['status'] === 200) {
                    $(".confirm").find("span").find("span").html('');
                    $all_select.find("span").find("span").html("");
                    $("#total_price").html(data['total_price']);
                }
            })
            }

        }


    })

    $("#make_order").click(function () {

        var select_list = [];

        var unselect_list = [];

        $(".confirm").each(function () {

            var $confirm = $(this);

            var cartid = $confirm.parents("li").attr("cartid");

            if ($confirm.find("span").find("span").html().trim()) {
                select_list.push(cartid);
            } else {
                unselect_list.push(cartid);
            }

        })

        if(select_list.length === 0){
            return
        }

        $.getJSON("/axf/makeorder/", function (data) {
            console.log(data);

            if (data['status'] === 200){
                window.open('/axf/orderdetail/?orderid=' + data['order_id'], target="_self");
            }

        })
    })


})