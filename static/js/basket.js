window.onload = function (event) {
    $('.basket_list').on('change', 'input[type="number"]', function (event) {
        let t_href = event.target;
        $.ajax(
            {
                url: `/baskets/edit/${t_href.name}/${t_href.value}/`,
                success: function (data) {
                    $('.basket_list').html(data.result)
                }
            }
        );
        event.preventDefault()
    })
    $('.card_add_basket').on('click', 'button[type="button"]', function (event) {
        let value = event.target.value;
        let page = $('#current_page').html()
        let cat_id = $('#current_cat').html()
        $.ajax(
            {
                url: `/baskets/add/${value}/`,
                data: {
                    'page': page,
                    'cat_id': cat_id
                },
                success: function (data) {
                    $('.card_add_basket').html(data.result)
                }
            }
        );
        event.preventDefault()
    })
}