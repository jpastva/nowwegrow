''' Tests for account app views '''
from django.test import TestCase
from django.urls import reverse
from register.models import User
from account.models import BusinessType, MerchantProfile
from shop.models import Product, Category

class ProfileViewTest(TestCase):
    ''' Class to test dashboard view '''
    def setUp(self):
        ''' Set up test data for views '''
        # Create a test merchant user
        test_merchant = User.objects.create_user(username='testmerchant', password='2HJ1vRV0Z&3iD', first_name='Merchant', last_name='Name', email='merchant@email.com', is_active=True, is_merchant=True)
        test_merchant.save()
        # Create a test business type
        BusinessType.objects.create(type='test', slug='test')
        bus_type = BusinessType.objects.get(type='test')
        merch_user = User.objects.get(username='testmerchant')
        # Create a test merchant profile
        merchant = MerchantProfile(id = 1, user = merch_user, merchant_name="Test Merchant", 
            merchant_email='merchant@email.com', merchant_phone='2158209998',
            merchant_website='www.business.com', merchant_street='218 Tech Rd', 
            merchant_zip='15205')
        merchant.merchant_type.add(bus_type)
        merchant.save()

    def test_profile_redirect_if_not_logged_in(self):
        ''' Make sure redirect if not logged in for dashboard '''
        response = self.client.get(reverse('dashboard'))
        self.assertRedirects(response, '/accounts/login/?next=/profile/')
    
    def test_logged_in_uses_correct_template(self):
        ''' Make sure correct dashboard template renders '''
        login = self.client.login(username='testmerchant', password='2HJ1vRV0Z&3iD')
        response = self.client.get(reverse('dashboard'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testmerchant')
        # Check for "success" response
        self.assertEqual(response.status_code, 200)

        # Check for correct template
        self.assertTemplateUsed(response, 'account/dashboard.html')

class EditViewTest(TestCase):
    ''' Class to test profile edit view '''
    def setUp(self):
        ''' Set up test data for views '''
        # Create a test merchant user
        test_merchant = User.objects.create_user(username='testmerchant', password='2HJ1vRV0Z&3iD', first_name='Merchant', last_name='Name', email='merchant@email.com', is_active=True, is_merchant=True)
        test_merchant.save()
        # Create a test business type
        BusinessType.objects.create(type='test', slug='test')
        bus_type = BusinessType.objects.get(type='test')
        merch_user = User.objects.get(username='testmerchant')
        # Create a test merchant profile
        merchant = MerchantProfile(id = 1, user = merch_user, merchant_name="Test Merchant", 
            merchant_email='merchant@email.com', merchant_phone='2158209998',
            merchant_website='www.business.com', merchant_street='218 Tech Rd', 
            merchant_zip='15205')
        merchant.merchant_type.add(bus_type)
        merchant.save()

    def test_profile_edit_redirect_if_not_logged_in(self):
        ''' Make sure redirect if not logged in for profile edit '''
        response = self.client.get(reverse('edit'))
        self.assertRedirects(response, '/accounts/login/?next=/profile/edit/')
    
    def test_logged_in_uses_correct_template(self):
        ''' Make sure correct profile edit template renders '''
        login = self.client.login(username='testmerchant', password='2HJ1vRV0Z&3iD')
        response = self.client.get(reverse('edit'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testmerchant')
        # Check for "success" response
        self.assertEqual(response.status_code, 200)

        # Check for correct template
        self.assertTemplateUsed(response, 'account/edit.html')

class UserOrdersViewTest(TestCase):
    ''' Class to test user orders view '''
    def setUp(self):
        ''' Set up test data for views '''
        # Create a test merchant user
        test_merchant = User.objects.create_user(username='testmerchant', password='2HJ1vRV0Z&3iD', first_name='Merchant', last_name='Name', email='merchant@email.com', is_active=True, is_merchant=True)
        test_merchant.save()
        # Create a test business type
        BusinessType.objects.create(type='test', slug='test')
        bus_type = BusinessType.objects.get(type='test')
        merch_user = User.objects.get(username='testmerchant')
        # Create a test merchant profile
        merchant = MerchantProfile(id = 1, user = merch_user, merchant_name="Test Merchant", 
            merchant_email='merchant@email.com', merchant_phone='2158209998',
            merchant_website='www.business.com', merchant_street='218 Tech Rd', 
            merchant_zip='15205')
        merchant.merchant_type.add(bus_type)
        merchant.save()

    def test_orders_redirect_if_not_logged_in(self):
        ''' Make sure redirect if not logged in for orders '''
        response = self.client.get(reverse('user_orders'))
        self.assertRedirects(response, '/accounts/login/?next=/profile/orders/')
    
    def test_cancel_orders_redirect_if_not_logged_in(self):
        ''' Make sure redirect if not logged in for orders '''
        response = self.client.get(reverse('cancel_order'))
        self.assertRedirects(response, '/accounts/login/?next=/profile/orders/cancel/')
    
    def test_order_items_redirect_if_not_logged_in(self):
        ''' Make sure redirect if not logged in for orders '''
        response = self.client.get(reverse('user_order_items'))
        self.assertRedirects(response, '/accounts/login/?next=/profile/orders/items/')
    
    def test_logged_in_uses_correct_template(self):
        ''' Make sure correct orders template renders '''
        login = self.client.login(username='testmerchant', password='2HJ1vRV0Z&3iD')
        response = self.client.get(reverse('user_orders'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testmerchant')
        # Check for "success" response
        self.assertEqual(response.status_code, 200)

        # Check for correct template
        self.assertTemplateUsed(response, 'account/orders.html')

class UserAddressesViewTest(TestCase):
    ''' Class to test user addresses view '''
    def setUp(self):
        ''' Set up test data for views '''
        # Create a test merchant user
        test_merchant = User.objects.create_user(username='testmerchant', password='2HJ1vRV0Z&3iD', first_name='Merchant', last_name='Name', email='merchant@email.com', is_active=True, is_merchant=True)
        test_merchant.save()
        # Create a test business type
        BusinessType.objects.create(type='test', slug='test')
        bus_type = BusinessType.objects.get(type='test')
        merch_user = User.objects.get(username='testmerchant')
        # Create a test merchant profile
        merchant = MerchantProfile(id = 1, user = merch_user, merchant_name="Test Merchant", 
            merchant_email='merchant@email.com', merchant_phone='2158209998',
            merchant_website='www.business.com', merchant_street='218 Tech Rd', 
            merchant_zip='15205')
        merchant.merchant_type.add(bus_type)
        merchant.save()

    def test_addresses_redirect_if_not_logged_in(self):
        ''' Make sure redirect if not logged in for addresses '''
        response = self.client.get(reverse('user_addresses'))
        self.assertRedirects(response, '/accounts/login/?next=/profile/addresses/')
    
    def test_add_addresses_redirect_if_not_logged_in(self):
        ''' Make sure redirect if not logged in for adding addresses '''
        response = self.client.get(reverse('add_address'))
        self.assertRedirects(response, '/accounts/login/?next=/profile/addresses/new/')
    
    def test_logged_in_uses_correct_template(self):
        ''' Make sure correct addresses template renders '''
        login = self.client.login(username='testmerchant', password='2HJ1vRV0Z&3iD')
        response = self.client.get(reverse('user_addresses'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testmerchant')
        # Check for "success" response
        self.assertEqual(response.status_code, 200)

        # Check for correct template
        self.assertTemplateUsed(response, 'account/addresses.html')

class UserPasswordViewTest(TestCase):
    ''' Class to test user password view '''
    def setUp(self):
        ''' Set up test data for views '''
        # Create a test merchant user
        test_merchant = User.objects.create_user(username='testmerchant', password='2HJ1vRV0Z&3iD', first_name='Merchant', last_name='Name', email='merchant@email.com', is_active=True, is_merchant=True)
        test_merchant.save()
        # Create a test business type
        BusinessType.objects.create(type='test', slug='test')
        bus_type = BusinessType.objects.get(type='test')
        merch_user = User.objects.get(username='testmerchant')
        # Create a test merchant profile
        merchant = MerchantProfile(id = 1, user = merch_user, merchant_name="Test Merchant", 
            merchant_email='merchant@email.com', merchant_phone='2158209998',
            merchant_website='www.business.com', merchant_street='218 Tech Rd', 
            merchant_zip='15205')
        merchant.merchant_type.add(bus_type)
        merchant.save()

    def test_password_redirect_if_not_logged_in(self):
        ''' Make sure redirect if not logged in for password reset '''
        response = self.client.get(reverse('password_change'))
        self.assertRedirects(response, '/accounts/login/?next=/profile/password_change/')
    
    def test_logged_in_success(self):
        ''' Make sure logging in works '''
        login = self.client.login(username='testmerchant', password='2HJ1vRV0Z&3iD')
        response = self.client.get(reverse('password_change'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testmerchant')
        # Check for "success" response
        self.assertEqual(response.status_code, 200)

class MembershipViewTest(TestCase):
    ''' Class to test membership view '''
    def setUp(self):
        ''' Set up test data for views '''
        # Create a test merchant user
        test_merchant = User.objects.create_user(username='testmerchant', password='2HJ1vRV0Z&3iD', first_name='Merchant', last_name='Name', email='merchant@email.com', is_active=True, is_merchant=True)
        test_merchant.save()
        # Create a test business type
        BusinessType.objects.create(type='test', slug='test')
        bus_type = BusinessType.objects.get(type='test')
        merch_user = User.objects.get(username='testmerchant')
        # Create a test merchant profile
        merchant = MerchantProfile(id = 1, user = merch_user, merchant_name="Test Merchant", 
            merchant_email='merchant@email.com', merchant_phone='2158209998',
            merchant_website='www.business.com', merchant_street='218 Tech Rd', 
            merchant_zip='15205')
        merchant.merchant_type.add(bus_type)
        merchant.save()
        Category.objects.create(name='Test category')
        test_cat = Category.objects.get(name='Test category')
        Product.objects.create(merchant=test_merchant,name='NowWeGrow Membership',
            category=test_cat,description="Test",sale_unit='Membership',unit_price=60)

    def test_membership_redirect_if_not_logged_in(self):
        ''' Make sure redirect if not logged in for memberships '''
        response = self.client.get(reverse('merchant_membership'))
        self.assertRedirects(response, '/accounts/login/?next=/profile/membership/')
    
    def test_renew_membership_redirect_if_not_logged_in(self):
        ''' Make sure redirect if not logged in for renew memberships '''
        response = self.client.get(reverse('renew_membership'))
        self.assertRedirects(response, '/accounts/login/?next=/profile/membership/renew/')
    
    def test_logged_in_uses_correct_template(self):
        ''' Make sure correct membership template renders '''
        login = self.client.login(username='testmerchant', password='2HJ1vRV0Z&3iD')
        response = self.client.get(reverse('merchant_membership'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testmerchant')
        # Check for "success" response
        self.assertEqual(response.status_code, 200)

        # Check for correct template
        self.assertTemplateUsed(response, 'account/merchants/membership.html')

class MerchantProductViewTest(TestCase):
    ''' Class to test product view '''
    def setUp(self):
        ''' Set up test data for views '''
        # Create a test merchant user
        test_merchant = User.objects.create_user(username='testmerchant',
            password='2HJ1vRV0Z&3iD', first_name='Merchant', last_name='Name',
            email='merchant@email.com', is_active=True, is_merchant=True)
        test_merchant.save()
        # Create a test business type
        BusinessType.objects.create(type='test', slug='test')
        bus_type = BusinessType.objects.get(type='test')
        merch_user = User.objects.get(username='testmerchant')
        # Create a test merchant profile
        merchant = MerchantProfile(id = 1, user = merch_user, merchant_name="Test Merchant", 
            merchant_email='merchant@email.com', merchant_phone='2158209998',
            merchant_website='www.business.com', merchant_street='218 Tech Rd', 
            merchant_zip='15205', is_active=True)
        merchant.merchant_type.add(bus_type)
        merchant.save()
        Category.objects.create(name='Test category')
        test_cat = Category.objects.get(name='Test category')
        Product.objects.create(merchant=test_merchant,name='NowWeGrow Membership',
            category=test_cat,description="Test",sale_unit='Membership',unit_price=60)

    def test_password_redirect_if_not_logged_in(self):
        ''' Make sure redirect if not logged in for products '''
        response = self.client.get(reverse('merchant_products'))
        self.assertRedirects(response, '/accounts/login/?next=/profile/products/')

    def test_add_password_redirect_if_not_logged_in(self):
        ''' Make sure redirect if not logged in for add products '''
        response = self.client.get(reverse('add_product'))
        self.assertRedirects(response, '/accounts/login/?next=/profile/products/add/')
    
    def test_logged_in_success(self):
        ''' Make sure logging in works for products view '''
        login = self.client.login(username='testmerchant', password='2HJ1vRV0Z&3iD')
        response = self.client.get(reverse('merchant_products'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testmerchant')
        # Check for "success" response
        self.assertEqual(response.status_code, 200)

        # Check for correct template
        self.assertTemplateUsed(response, 'account/merchants/products.html')
    
    def test_edit_password_redirect_if_not_logged_in(self):
        ''' Make sure redirect if not logged in for products '''
        response = self.client.get(reverse('edit_products'))
        self.assertRedirects(response, '/accounts/login/?next=/profile/products/edit/')

class MerchantOrderViewTest(TestCase):
    ''' Class to test merchant orders view '''
    def setUp(self):
        ''' Set up test data for views '''
        # Create a test merchant user
        test_merchant = User.objects.create_user(username='testmerchant',
            password='2HJ1vRV0Z&3iD', first_name='Merchant', last_name='Name',
            email='merchant@email.com', is_active=True, is_merchant=True)
        test_merchant.save()
        # Create a test business type
        BusinessType.objects.create(type='test', slug='test')
        bus_type = BusinessType.objects.get(type='test')
        merch_user = User.objects.get(username='testmerchant')
        # Create a test merchant profile
        merchant = MerchantProfile(id = 1, user = merch_user, merchant_name="Test Merchant", 
            merchant_email='merchant@email.com', merchant_phone='2158209998',
            merchant_website='www.business.com', merchant_street='218 Tech Rd', 
            merchant_zip='15205')
        merchant.merchant_type.add(bus_type)
        merchant.save()

    def test_password_redirect_if_not_logged_in(self):
        ''' Make sure redirect if not logged in for orders '''
        response = self.client.get(reverse('merchant_orders'))
        self.assertRedirects(response, '/accounts/login/?next=/profile/merchants/orders/')
    
    def test_logged_in_success(self):
        ''' Make sure logging in works for orders view '''
        login = self.client.login(username='testmerchant', password='2HJ1vRV0Z&3iD')
        response = self.client.get(reverse('merchant_orders'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testmerchant')
        # Check for "success" response
        self.assertEqual(response.status_code, 200)

        # Check for correct template
        self.assertTemplateUsed(response, 'account/merchants/orderlist.html')
