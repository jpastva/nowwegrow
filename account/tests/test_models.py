''' Tests for account app models '''
from django.test import TestCase
from account.models import BusinessType, MerchantProfile, Address, Membership
from register.models import User
from orders.models import Order

class BusinessTypeModelTest(TestCase):
    ''' Tests for BusinessType model '''
    @classmethod
    def setUpTestData(cls):
        ''' Set up object data for test methods '''
        BusinessType.objects.create(type='Business', slug='business')

    def test_type_label(self):
        ''' Test type label '''
        business_type = BusinessType.objects.get(id=1)
        field_label = business_type._meta.get_field('type').verbose_name
        self.assertEqual(field_label, 'type')

    def test_type_max_length(self):
        ''' Test type length '''
        business_type = BusinessType.objects.get(id=1)
        max_length = business_type._meta.get_field('type').max_length
        self.assertEqual(max_length, 30)

    def test_slug_label(self):
        ''' Test slug label '''
        business_type = BusinessType.objects.get(id=1)
        field_label = business_type._meta.get_field('slug').verbose_name
        self.assertEqual(field_label, 'slug')

    def test_slug_max_length(self):
        ''' Test slug length '''
        business_type = BusinessType.objects.get(id=1)
        max_length = business_type._meta.get_field('slug').max_length
        self.assertEqual(max_length, 200)

    def test_get_absolute_url(self):
        ''' Test get URL '''
        business_type = BusinessType.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(business_type.get_absolute_url(), '/profile/business/')

class MerchantProfileModelTest(TestCase):
    ''' Tests for MerchantProfile model '''
    @classmethod
    def setUpTestData(cls):
        ''' Set up object data for test methods '''
        User.objects.create(username='testuser', password='Test_password123', first_name="Test", 
            last_name='User', email='test@email.com', is_active=True, is_merchant=True)
        user = User.objects.get(username='testuser')
        BusinessType.objects.create(type='test', slug='test')
        bus_type = BusinessType.objects.get(type='test')
        merchant = MerchantProfile(id = 1, user = user, merchant_name="Test Merchant", 
            merchant_email='merchant@email.com', merchant_phone='2158209998',
            merchant_website='www.business.com', merchant_street='218 Tech Rd', 
            merchant_zip='15205')
        merchant.merchant_type.add(bus_type)
        merchant.save()

    def test_name_label(self):
        ''' Test name label '''
        merchant = MerchantProfile.objects.get(id=1)
        field_label = merchant._meta.get_field('merchant_name').verbose_name
        self.assertEqual(field_label, 'Merchant Name')

    def test_name_max_length(self):
        ''' Test name length '''
        merchant = MerchantProfile.objects.get(id=1)
        max_length = merchant._meta.get_field('merchant_name').max_length
        self.assertEqual(max_length, 50)

    def test_email_label(self):
        ''' Test email label '''
        merchant = MerchantProfile.objects.get(id=1)
        field_label = merchant._meta.get_field('merchant_email').verbose_name
        self.assertEqual(field_label, 'merchant email')

    def test_email_max_length(self):
        ''' Test email length '''
        merchant = MerchantProfile.objects.get(id=1)
        max_length = merchant._meta.get_field('merchant_email').max_length
        self.assertEqual(max_length, 75)

    def test_phone_label(self):
        ''' Test phone label '''
        merchant = MerchantProfile.objects.get(id=1)
        field_label = merchant._meta.get_field('merchant_phone').verbose_name
        self.assertEqual(field_label, 'merchant phone')

    def test_website_label(self):
        ''' Test website label '''
        merchant = MerchantProfile.objects.get(id=1)
        field_label = merchant._meta.get_field('merchant_website').verbose_name
        self.assertEqual(field_label, 'merchant website')

    def test_website_max_length(self):
        ''' Test website length '''
        merchant = MerchantProfile.objects.get(id=1)
        max_length = merchant._meta.get_field('merchant_website').max_length
        self.assertEqual(max_length, 200)

    def test_street_label(self):
        ''' Test street label '''
        merchant = MerchantProfile.objects.get(id=1)
        field_label = merchant._meta.get_field('merchant_street').verbose_name
        self.assertEqual(field_label, 'merchant street')

    def test_street_max_length(self):
        ''' Test street length '''
        merchant = MerchantProfile.objects.get(id=1)
        max_length = merchant._meta.get_field('merchant_street').max_length
        self.assertEqual(max_length, 500)

    def test_zip_label(self):
        ''' Test zip label '''
        merchant = MerchantProfile.objects.get(id=1)
        field_label = merchant._meta.get_field('merchant_zip').verbose_name
        self.assertEqual(field_label, 'merchant zip')

    def test_zip_max_length(self):
        ''' Test zip length '''
        merchant = MerchantProfile.objects.get(id=1)
        max_length = merchant._meta.get_field('merchant_zip').max_length
        self.assertEqual(max_length, 12)

    def test_lat_label(self):
        ''' Test latitude label '''
        merchant = MerchantProfile.objects.get(id=1)
        field_label = merchant._meta.get_field('latitude').verbose_name
        self.assertEqual(field_label, 'latitude')

    def test_lat_max_length(self):
        ''' Test latitude length '''
        merchant = MerchantProfile.objects.get(id=1)
        max_length = merchant._meta.get_field('latitude').max_digits
        self.assertEqual(max_length, 9)

    def test_long_label(self):
        ''' Test longitude label '''
        merchant = MerchantProfile.objects.get(id=1)
        field_label = merchant._meta.get_field('longitude').verbose_name
        self.assertEqual(field_label, 'longitude')

    def test_long_max_length(self):
        ''' Test longitude length '''
        merchant = MerchantProfile.objects.get(id=1)
        max_length = merchant._meta.get_field('longitude').max_digits
        self.assertEqual(max_length, 9)

    def test_slug_label(self):
        ''' Test slug label '''
        merchant = MerchantProfile.objects.get(id=1)
        field_label = merchant._meta.get_field('slug').verbose_name
        self.assertEqual(field_label, 'slug')

    def test_slug_max_length(self):
        ''' Test slug max length '''
        merchant = MerchantProfile.objects.get(id=1)
        max_length = merchant._meta.get_field('slug').max_length
        self.assertEqual(max_length, 200)

class AddressModelTest(TestCase):
    ''' Tests for Address model '''
    @classmethod
    def setUpTestData(cls):
        ''' Set up object data for test methods '''
        User.objects.create(username='testuser', password='Test_password123', first_name="Test", 
            last_name='User', email='test@email.com', is_active=True, is_merchant=True)
        user = User.objects.get(id=1)
        address = Address(id = 1, user = user, nickname='Home', address1='123 E Main St',
            address2='Apt B',
            city='Carnegie', state='PA', zip='15106')
        address.save()

    def test_nickname_label(self):
        ''' Test nickname label '''
        address = Address.objects.get(id=1)
        field_label = address._meta.get_field('nickname').verbose_name
        self.assertEqual(field_label, 'Nickname')

    def test_nickname_max_length(self):
        ''' Test nickname max length '''
        address = Address.objects.get(id=1)
        max_length = address._meta.get_field('nickname').max_length
        self.assertEqual(max_length, 30)

    def test_address1_label(self):
        ''' Test address1 label '''
        address = Address.objects.get(id=1)
        field_label = address._meta.get_field('address1').verbose_name
        self.assertEqual(field_label, 'Address Line 1')

    def test_address1_max_length(self):
        ''' Test address1 max length '''
        address = Address.objects.get(id=1)
        max_length = address._meta.get_field('address1').max_length
        self.assertEqual(max_length, 30)

    def test_address2_label(self):
        ''' Test address2 label '''
        address = Address.objects.get(id=1)
        field_label = address._meta.get_field('address2').verbose_name
        self.assertEqual(field_label, 'Address Line 2')

    def test_address2_max_length(self):
        ''' Test address2 max length '''
        address = Address.objects.get(id=1)
        max_length = address._meta.get_field('address2').max_length
        self.assertEqual(max_length, 30)

    def test_city_label(self):
        ''' Test city label '''
        address = Address.objects.get(id=1)
        field_label = address._meta.get_field('city').verbose_name
        self.assertEqual(field_label, 'City')

    def test_city_max_length(self):
        ''' Test city max length '''
        address = Address.objects.get(id=1)
        max_length = address._meta.get_field('city').max_length
        self.assertEqual(max_length, 30)

    def test_state_label(self):
        ''' Test city label '''
        address = Address.objects.get(id=1)
        field_label = address._meta.get_field('state').verbose_name
        self.assertEqual(field_label, 'State')

    def test_state_max_length(self):
        ''' Test state max length '''
        address = Address.objects.get(id=1)
        max_length = address._meta.get_field('state').max_length
        self.assertEqual(max_length, 30)

    def test_zip_label(self):
        ''' Test zip label '''
        address = Address.objects.get(id=1)
        field_label = address._meta.get_field('zip').verbose_name
        self.assertEqual(field_label, 'Zip code')

    def test_zip_max_length(self):
        ''' Test zip max length '''
        address = Address.objects.get(id=1)
        max_length = address._meta.get_field('zip').max_length
        self.assertEqual(max_length, 12)

    class MembershipModelTest(TestCase):
        ''' Test Membership model '''
        @classmethod
        def setUpTestData(cls):
            ''' Set up object data for test methods '''
            User.objects.create(username='testuser', password='Test_password123', first_name="Test", 
                last_name='User', email='test@email.com', is_active=True, is_merchant=True)
            user = User.objects.get(username='testuser')
            address = Address(id = 1, user = user, nickname='Home', address1='123 E Main St',
                address2='Apt B', city='Carnegie', state='PA', zip='15106')
            address.save()
            order = Order.objects.create(user = user, address = address, total = 30, paid=True,
                braintree_id='123B')
            BusinessType.objects.create(type='test', slug='test')
            bus_type = BusinessType.objects.get(type='test')
            merchant = MerchantProfile(id = 1, user = user, merchant_name="Test Merchant",
                merchant_email='merchant@email.com', merchant_phone='2158209998',
                merchant_website='www.business.com', merchant_street='218 Tech Rd',
                merchant_zip='15205')
            merchant.merchant_type.add(bus_type)
            merchant.save()
            Membership.objects.create(merchant = merchant, order = order, price = 30)

        def test_price_label(self):
            ''' Test price label '''
            membership = Membership.objects.get(id=1)
            field_label = membership._meta.get_field('price').verbose_name
            self.assertEqual(field_label, 'price')

        def test_price_max_length(self):
            ''' Test price max length '''
            membership = Membership.objects.get(id=1)
            max_length = membership._meta.get_field('price').max_digits
            self.assertEqual(max_length, 10)
