from basketapp.models import Basket


def basket_context(request):
    baskets = []
    total_sum = total_quantity = 0
    if request.user.is_authenticated:
        baskets = Basket.objects.filter(user=request.user)
        total_sum = sum(basket.prod for basket in baskets)
        total_quantity = sum(basket.quantity for basket in baskets)
    return {
        'baskets': baskets,
        'total_sum': total_sum,
        'total_quantity': total_quantity,
    }
