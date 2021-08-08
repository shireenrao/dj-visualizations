import uuid

from customers.models import Customer
from profiles.models import Profile


def generate_code():
    code = str(uuid.uuid4()).replace("-", "")[:12]
    return code


def get_customer_from_id(val):
    cust = Customer.objects.get(id=val)
    return cust.name


def get_salesman_from_id(val):
    salesman = Profile.objects.get(id=val)
    return salesman.user.username
