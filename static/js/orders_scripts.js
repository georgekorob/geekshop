"use strict";
let quantity, price, orderitem_num, delta_quantity, delta_cost;
let quantity_arr = []
let price_arr = []
let total_forms, order_total_quantity, order_total_cost;
let $orderForm, $orderTotalQuantityDOM, $orderTotalCostDOM;

function orderSummaryUpdate(orderitem_price, delta_quantity) {
    delta_cost = orderitem_price * delta_quantity;
    order_total_cost = (order_total_cost + delta_cost);
    order_total_quantity = order_total_quantity + delta_quantity;
    $orderTotalQuantityDOM.html(order_total_quantity.toString());
    $orderTotalCostDOM.html(order_total_cost.toFixed(2));
}

function deleteOrderItem(row) {
    let target_name = row[0].querySelector('input[type="number"]').name;
    orderitem_num = parseInt(target_name.replace('orderitems-', '').replace('-quantity', ''));
    delta_quantity = -quantity_arr[orderitem_num];
    orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
}

function parseOrderForm() {
    total_forms = parseInt($('input[name=orderitems-TOTAL_FORMS]').val());
    for (let i = 0; i < total_forms; i++) {
        quantity = parseInt($('input[name=orderitems-' + i + '-quantity]').val());
        price = parseInt($('.orderitems-' + i + '-price').text().replace(',', '.'));
        quantity_arr[i] = quantity;
        price_arr[i] = price ? price : 0;
    }
    console.info('QUANTITY', quantity_arr);
    console.info('PRICE', price_arr);
}

function changeOrderItemPk(event) {
    let target = event.target;
    let orderitem_num_select = parseInt(target.name.replace('orderitems-', '').replace('-product', ''));
    let orderitem_product_pk = target.options[target.selectedIndex].value;
    if (orderitem_product_pk) {
        $.ajax({
            url: `/products/price/${orderitem_product_pk}/`,
            success: function (data) {
                console.log('price object: ', data);
                if (data.price) {
                    price_arr[orderitem_num_select] = parseFloat(data.price);
                    if (isNaN(quantity_arr[orderitem_num_select])) {
                        quantity_arr[orderitem_num_select] = 0
                    }
                    let priceHtml = `<span>${data.price.replace('.', ',')}</span> руб`;
                    // $orderTotalCostDOM.html(Number(order_total_cost.toFixed(2)).toString());
                    let currentTr = $('.order_form table').find('tr:eq(' + (orderitem_num_select + 1) + ')');
                    currentTr.find('td:eq(2)').html(priceHtml);
                    let current_quantity = currentTr.find('input[type="number"]').val();
                    if (isNaN(current_quantity) || current_quantity === '') {
                        currentTr.find('input[type="number"]').val(0)
                    }
                    orderSummary();
                }
            },
        });
    }
    event.preventDefault();
}

function editQuantity(event) {
    let target = event.target;
    orderitem_num = parseInt(target.name.replace('orderitems-', '').replace('-quantity', ''));
    if (price_arr[orderitem_num]) {
        let orderitem_quantity = parseInt(target.value)
        delta_quantity = orderitem_quantity - quantity_arr[orderitem_num];
        quantity_arr[orderitem_num] = orderitem_quantity;
        orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
    }
}

function deleteItemInForm(event) {
    let target = event.target;
    orderitem_num = parseInt(target.name.replace('orderitems-', '').replace('-DELETE', ''));
    if (target.checked) {
        delta_quantity = -quantity_arr[orderitem_num];
    } else {
        delta_quantity = quantity_arr[orderitem_num];
    }
    orderSummaryUpdate(price_arr[orderitem_num], delta_quantity);
}

function orderSummary() {
    order_total_quantity = 0;
    order_total_cost = 0;
    for (let i = 0; i < total_forms; i++) {
        order_total_quantity += quantity_arr[i];
        order_total_cost += quantity_arr[i] * price_arr[i];
    }
    $orderTotalQuantityDOM.html(order_total_quantity.toString());
    $orderTotalCostDOM.html(order_total_cost.toFixed(2));
}

window.onload = function () {
    $orderTotalQuantityDOM = $('.order_total_quantity');
    $orderTotalCostDOM = $('.order_total_cost')
    $orderForm = $('.order_form');

    parseOrderForm();

    order_total_quantity = parseInt($orderTotalQuantityDOM.text()) || 0;
    order_total_cost = parseInt($orderTotalCostDOM.text().replace(',', '.')) || 0;

    // количество
    $orderForm.on('click', 'input[type=number]', (event) => editQuantity(event));

    // удалить
    $orderForm.on('click', 'input[type=checkbox]', (event) => deleteItemInForm(event));

    $('.formset_row').formset({
        addText: 'добавить продукт',
        deleteText: 'удалить',
        prefix: 'orderitems',
        removed: deleteOrderItem,
    });

    // при изменении поля товара
    $orderForm.on('change', 'select', (event) => changeOrderItemPk(event));
}