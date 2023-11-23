from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Customers, Suppliers, Categories, Products, Orders, Orderdetails, Employees

class SerializadorPadre(ModelSerializer):
    class Meta:
        fields = '__all__'

class CustomerSerializer(SerializadorPadre):
    class Meta:
        model = Customers
        fields = '__all__'

class SupplierSerializer(SerializadorPadre):
    class Meta:
        model = Suppliers
        fields = '__all__'

class CategorieSerializer (SerializadorPadre):
   class Meta:
      model = Categories
      fields = '__all__'

class ProductSerializer (SerializadorPadre):
   supplierid = SupplierSerializer(many=False,required=False)
   categoryid = CategorieSerializer(many=False, required=False)

   class Meta:
      model = Products
      fields = '__all__'

class OrderdetailSerializer (SerializadorPadre):
   class Meta:
      model = Orderdetails
      fields = '__all__'

class OrderSerializer(SerializadorPadre):
   order_details = OrderdetailSerializer(many=True, read_only=True)

   class Meta:
      model = Orders
      fields = '__all__'

class EmployeeSerializer (SerializadorPadre):
   class Meta:
      model = Employees
      fields = '__all__'


class EmployeesSerializer(serializers.ModelSerializer):
    NombreCompleto = serializers.CharField(source='full_name', read_only=True)
    class Meta:
        model = Employees
        fields = ['EmployeeID', 'NombreCompleto', 'GananciasTotales', 'HireDate']




class ProductUpdateSerializer(serializers.ModelSerializer):
    Category = CategorieSerializer(read_only=True)
    PreviousPrice = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = ['ProductID', 'Category', 'PreviousPrice', 'PercentageIncrease']  # Agrega más campos según sea necesario

    def get_PreviousPrice(self, obj):
        return obj.unitprice / (1 + obj.aumento)
