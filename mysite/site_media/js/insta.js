$(document).ready(function(){ 
    	alert("hello");
    	$(".remove").live('click', function () {
        id = $(this).parent().text();
        id = id.replace(/\s+/g, '');
        var num = parseInt($(this).parent().prev().children(':nth-child(2)').text());
        $(this).parent().parent().remove();
        price = $("#" + id).parent().parent().prev().children(':first-child').children(':first-child').text();
        $("#" + id).parent().replaceWith('<button class="btn add" id="' + id + '"><i class="icon-shopping-cart"></i>Add</button>'); 
        price = price.substring(1);
        var new_total = parseFloat($('#total').text()) - (parseFloat(num)*parseFloat(price));
        $('#total').text(new_total.toFixed(2));
    });
    $(".down").live('click', function () {
        var currqty = parseInt($(this).prev().text(), 10);
        var id = $(this).prev().attr("id");
        var newid = id.slice(0, -1);
        --currqty;
        if (currqty < 1) {
            $(this).prev().text(1);
            $("#" + newid).text(1);
        } else {
            $(this).prev().text(currqty);
            $("#" + newid).text(currqty);
            price = $("#" + newid).parent().parent().prev().children(':first-child').children(':first-child').text(); 
        	price = price.substring(1);
        	var new_total = parseFloat($('#total').text()) - parseFloat(price);
        	$('#total').text(new_total.toFixed(2));
        }
    });
    $(".up").live('click', function () {
        var currqty = parseInt($(this).next().text(), 10);
        var id = $(this).next().attr("id");
        var newid = id.slice(0, -1);
        ++currqty;
        $(this).next().text(currqty);
        $("#" + newid).text(currqty);
        price = $("#" + newid).parent().parent().prev().children(':first-child').children(':first-child').text(); 
        price = price.substring(1);
        var new_total = parseFloat($('#total').text()) + parseFloat(price);
        $('#total').text((new_total.toFixed(2)).toString());
    });
    $('.add').live('click', function () {
        row = '<tr><td><span class=" counter"><button class="btn btn-link up" style="text-decoration: none;color:black"><i class="icon-caret-up upcar"></i></button><span class="count" id="' + $(this).attr("id") + '1' + '">1</span><button class="btn btn-link down" style="text-decoration: none;color:black"><i class="icon-caret-down downcar"></i></button></span><span class="item"><b>' + $(this).attr("id") + '</b><img src="/site_media/pics/' + $(this).attr("id") + '.png" alt="" width="20%" height="20%" style="padding-left:1em"><button class="btn btn-link remove" style="text-decoration: none;color:red"><i class="icon-remove-sign"></i></button></span></td></tr>';
        $('table.table').append(row);
        price = $(this).parent().prev().children(':first-child').children(':first-child').text(); 
        price = price.substring(1);
        var new_total = parseFloat($('#total').text()) + parseFloat(price);
        $('#total').text(new_total.toFixed(2));
        $(this).replaceWith('<span id="qty" style="background-color:DarkGray;padding-top:9%;padding-bottom:4%;"><button class="btn btn-link caret-up" style="text-decoration: none;color:black" id="up"><i class="icon-caret-up"></i></button><span style="padding-left:1%;padding-right:0.1%;padding-top:1%;padding-bottom:1%;background-color:Gainsboro;font-size:14px" id="'+$(this).attr("id")+'">1</span><button class="btn btn-link caret-down" style="text-decoration: none;color:black" id="down"><i class="icon-caret-down"></i></button></span>');
        $(".caret-down").unbind();
        $(".caret-up").unbind();
        $(".caret-down").click(function () {
            var oldid = $(this).prev().attr("id");
            var id = $(this).prev().attr("id") + "1";
            var currqty = parseInt($(this).prev().text(), 10);
            --currqty;
            price = $(this).parent().parent().prev().children(':first-child').children(':first-child').text(); 
        	price = price.substring(1);
        	var new_total = parseFloat($('#total').text()) - parseFloat(price);
        	$('#total').text(new_total.toFixed(2));
            if (currqty === 0) {
                $("#" + id).parent().parent().remove();
                $(this).parent().replaceWith('<button class="btn add" id="' + oldid + '"><i class="icon-shopping-cart"></i>Add</button>');
            } else {
                $(this).prev().text(currqty);
                $("#" + id).text(currqty);
            }
        });
        $(".caret-up").click(function () {
            var id = $(this).next().attr("id") + "1";
            var currqty = parseInt($(this).next().text(), 10);
            ++currqty;
            $(this).next().text(currqty);
            $("#" + id).text(currqty);
            price = $(this).parent().parent().prev().children(':first-child').children(':first-child').text(); 
        	price = price.substring(1);
        	var new_total = parseFloat($('#total').text()) + parseFloat(price);
        	$('#total').text((new_total.toFixed(2)).toString());
        });
    });
    	
    	});