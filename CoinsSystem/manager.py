from datetime import datetime, timedelta

from UsersDetails.models import UsersDetails
from CoinsSystem.models import CoinsSystem, CoinsRequest
import random
from django.http import FileResponse

from payments.models import paymentTransactions, paymentWithdrawal


class CoinsManager:

    @staticmethod
    def coins_management_handling(data):
        email = data.get("email", False)
        action = data.get("action", False)
        coins_to_update = data.get("coinsToUpdate", False)
        request_id = data.get("request_id", False)
        if(email and action and coins_to_update and request_id):
            user = UsersDetails.objects.get(email=email)
            coins_obj = CoinsSystem.objects.filter(user=user)
            if coins_obj:
                coins_obj = coins_obj[0]
            else:
                coins_obj = CoinsSystem.objects.create(user=user, coin=coins_to_update)
            if action == "add":
                coins_obj.coin = str(int(coins_obj.coin) + int(coins_to_update))
            elif action == "withdraw":
                coins_obj.coin = str(int(coins_obj.coin) - int(coins_to_update))

            coins_obj.save()
            request = CoinsRequest.objects.get(id = request_id)
            request.status = "completed"
            request.save()


    @staticmethod
    def coins_fetch_customer():
        return CoinsRequest.objects.all()

    @staticmethod
    def coins_user_request(data):
        unique_id = data.get("generatedKey", False)
        email = data.get("email", False)
        action = data.get("action", False)
        coins_to_update = data.get("amount", False)
        if(email and action and coins_to_update and unique_id):
            user = UsersDetails.objects.get(email=email)
            try:
                coins_obj = CoinsRequest.objects.create(user=user, coin_amount=coins_to_update, request_type=action)
            except:
                return False
            coins_obj.save()

    @staticmethod
    def coins_user_fetch(data):
        email = data.get("email", False)
        if email:
            try:
                coins_obj = CoinsRequest.objects.filter(user__email=email)
            except:
                return False
        return coins_obj



    @staticmethod
    def coins_admin(data):
        action = data.get("action", False)
        payment = []
        if action == "topup":
            payment = paymentTransactions.objects.filter().select_related("user")
        elif action == "withdraw":
            payment = paymentWithdrawal.objects.filter().select_related("user")
        return payment, action
