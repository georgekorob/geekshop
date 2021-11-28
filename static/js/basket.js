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
        $.ajax(
            {
                url: `/baskets/add/${value}/`,
                success: function (data) {
                    $('.card_add_basket').html(data.result)
                }
            }
        );
        event.preventDefault()
    })
}