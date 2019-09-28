from django.db import models

# TODO: you'll need to fill in the models that you create here!

# the class containing a portfolio of stocks
class PortfolioModel(models.Model):
    class Meta:
        app_label = 'api'

    cash = models.FloatField()

# the class containing your user information (including their api token and password, etc)
class UserModel(models.Model):
    class Meta:
        app_label = 'api'

    first_name = models.TextField()
    last_name = models.TextField()
    api_token = models.TextField()
    password = models.TextField()
    username = models.TextField()
    portfolio = models.OneToOneField(PortfolioModel, on_delete=models.CASCADE)

# a class containing what happened in a purchase (who made it, when it was made, what it traded)
class PurchaseModel(models.Model):
    class Meta:
        app_label = 'api'

    timestamp = models.DateField()
    reporter = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=5)
    price = models.FloatField()
    quantity = models.IntegerField()

# a class containing a simple set of data on a stock within a portfolio
class StockModel(models.Model):
    class Meta:
        app_label = 'api'

    portfolio = models.ForeignKey(PortfolioModel, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=5)
    quantity = models.IntegerField()


