$(function () {

    $("#all_types").click(function () {

        console.log("全部类型");

        var $all_types_container = $("#all_types_container");

        $all_types_container.show();

        var $all_type = $(this);



        var $span = $all_type.find("span").find("span");

        $span.removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up");

        var $sort_rule_container = $("#sort_rule_container");

        $sort_rule_container.slideUp();

        var $sort_rule = $("#sort_rule");

        var $span_sort_rule = $sort_rule.find("span").find("span");

        $span_sort_rule.removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down");

    })

    $("#all_types_container").click(function () {

        var $all_type_container = $(this);

        $all_type_container.hide();

        var $all_type = $("#all_types");

        var $span = $all_type.find("span").find("span");

        $span.removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down");

    })


    $("#sort_rule").click(function () {

        console.log("排序规则");

        var $sort_rule_container = $("#sort_rule_container");

        $sort_rule_container.slideDown();

        var $sort_rule = $(this);

        var $span = $sort_rule.find("span").find("span");

        $span.removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up");

        var $all_type_container = $("#all_types_container");

        $all_type_container.hide();

        var $all_type = $("#all_types");

        var $span_all_type = $all_type.find("span").find("span");

        $span_all_type.removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down");


    })

    $("#sort_rule_container").click(function () {

        var $sort_rule_container = $(this);

        $sort_rule_container.slideUp();

        var $sort_rule = $("#sort_rule");

        var $span = $sort_rule.find("span").find("span");

        $span.removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down");

    })

    //
    // $(".subShopping").click(function () {
    //     console.log('sub');
    //
    //
    //     // var goodsid = $add.attr("goodsid");
    //     // var goodsid = $add.prop("goodsid");
    //     //
    // })
    $(".subShopping").click(function () {
        console.log('sub');

        var $sub = $(this);

        //点击哪个商品，实现哪个商品的添加，首先要先找到那个商品
        // 根据属性名拿到属性值（根据id，拿到商品的名称
        var id1 = $sub.attr("gid")
        $.getJSON('/App/subcart',{'gid':id1},function (data) {
            console.log(data)
            if (data.status == 'fail'){
                window.location.href = '/App/login/'
                }else if (data.status == 'ok') {
                // window.location.href = '/App/login/'
            //直接通过prev方法拿去span标签，修改标签里面的内容
                $sub.next('span').text(data.goods_num)
            }
        })

    })


    //设置点击事件
    $(".addShopping").click(function () {
        console.log('add');

        var $add = $(this);

        //点击哪个商品，实现哪个商品的添加，首先要先找到那个商品
        // 根据属性名拿到属性值（根据id，拿到商品的名称
        var id1 = $add.attr('gid')
        $.getJSON('/App/addcart',{'gid':id1},function (data) {
            console.log(data)
            if (data.status == 'fail'){
                window.location.href = '/App/login/'
                }else if (data.status == 'ok') {
                // window.location.href = '/App/login/'
            //直接通过prev方法拿去span标签，修改标签里面的内容
                $add.prev('span').text(data.goods_num)
            }
        })







        // console.log($add.attr('class'));
        // console.log($add.prop('class'));
        //
        // console.log($add.attr('goodsid'));
        // console.log($add.prop('goodsid'));

        // var goodsid = $add.attr('goodsid');
        //
        // $.get('/axf/addtocart/', {'goodsid': goodsid}, function (data) {
        //     console.log(data);
        //
        //     if (data['status'] === 302){
        //         window.open('/axf/login/', target="_self");
        //     }else if(data['status'] === 200){
        //         $add.prev('span').html(data['c_goods_num']);
        //     }
        //
        // })

    })

})