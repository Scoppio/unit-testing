from django.db import models


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def __repr__(self) -> str:
        return f'<Company id={self.id} name={self.name}>'


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    msrp = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    @property
    def deleted(self):
        return self.deleted_at is not None

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<Product id={self.id} name={self.name} msrp={self.msrp}>'


class ProductEntry(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def total_price(self):
        return self.quantity * self.price_per_unit

    def delete(self):
        raise NotImplementedError("ProductEntry cannot be deleted")


    def __str__(self):
        prefix_quantity = 'in: ' if self.quantity > 0 else 'out: '
        return f'{self.product.name} - {prefix_quantity}{abs(self.quantity)}, ${self.price_per_unit}/ppu, @{self.date} ({self.company.name})'
