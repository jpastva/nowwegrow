''' Tests for account forms '''
from django.test import TestCase
from account.forms import UserEditForm, MerchantEditForm, CustomerEditForm, AddProductForm, ProductEditForm, GetIDForm, AddAddressForm, EditAddressForm, GetOrderForm

class UserEditFormTest(TestCase):
    ''' Tests for UserEditForm '''
    def test_user_form_first_name_label(self):
        ''' Test first_name field '''
        form = UserEditForm()
        self.assertTrue(form.fields['first_name'].label is None or form.fields['first_name'].label == 'First name')

    def test_user_form_last_name_label(self):
        ''' Test last_name field '''
        form = UserEditForm()
        self.assertTrue(form.fields['last_name'].label is None or form.fields['last_name'].label == 'Last name')

    def test_user_form_email_label(self):
        ''' Test email field '''
        form = UserEditForm()
        self.assertTrue(form.fields['email'].label is None or form.fields['email'].label == 'Email address')

class MerchantEditFormTest(TestCase):
    ''' Tests for MerchantEditForm '''
    def test_merchant_form_name_label(self):
        ''' Test merchant_name field '''
        form = MerchantEditForm()
        self.assertTrue(form.fields['merchant_name'].label is None or form.fields['merchant_name'].label == 'Merchant Name')

    def test_merchant_form_type_label(self):
        ''' Test merchant_type field '''
        form = MerchantEditForm()
        self.assertTrue(form.fields['merchant_type'].label is None or form.fields['merchant_type'].label == 'Merchant type')

    def test_merchant_form_phone_label(self):
        ''' Test merchant_phone field '''
        form = MerchantEditForm()
        self.assertTrue(form.fields['merchant_phone'].label is None or form.fields['merchant_phone'].label == 'Merchant phone')

    def test_merchant_form_email_label(self):
        ''' Test merchant_email field '''
        form = MerchantEditForm()
        self.assertTrue(form.fields['merchant_email'].label is None or form.fields['merchant_email'].label == 'Merchant email')

    def test_merchant_form_street_label(self):
        ''' Test merchant_street field '''
        form = MerchantEditForm()
        self.assertTrue(form.fields['merchant_street'].label is None or form.fields['merchant_street'].label == 'Merchant street')

    def test_merchant_form_zip_label(self):
        ''' Test merchant_zip field '''
        form = MerchantEditForm()
        self.assertTrue(form.fields['merchant_zip'].label is None or form.fields['merchant_zip'].label == 'Merchant zip')

    def test_merchant_form_website_label(self):
        ''' Test merchant_website field '''
        form = MerchantEditForm()
        self.assertTrue(form.fields['merchant_website'].label is None or form.fields['merchant_website'].label == 'Merchant website')

    def test_merchant_form_image_label(self):
        ''' Test image field '''
        form = MerchantEditForm()
        self.assertTrue(form.fields['image'].label is None or form.fields['image'].label == 'Image')

    def test_merchant_form_description_label(self):
        ''' Test description field '''
        form = MerchantEditForm()
        self.assertTrue(form.fields['description'].label is None or form.fields['description'].label == 'Description')

    def test_merchant_form_url_label(self):
        ''' Test product_url field '''
        form = MerchantEditForm()
        self.assertTrue(form.fields['product_url'].label is None or form.fields['product_url'].label == 'Product url')
    
class CustomerEditFormTest(TestCase):
    ''' Tests for CustomerEditForm '''
    def test_customer_form_phone_label(self):
        ''' Test customer_phone field '''
        form = CustomerEditForm()
        self.assertTrue(form.fields['customer_phone'].label is None or form.fields['customer_phone'].label == 'Customer phone')

class AddProductFormTest(TestCase):
    ''' Tests for AddProductForm '''
    def test_addproduct_form_name_label(self):
        ''' Test product name field '''
        form = AddProductForm()
        self.assertTrue(form.fields['name'].label is None or form.fields['name'].label == 'Name')

class ProductEditFormTest(TestCase):
    ''' Tests for ProductEditForm '''
    def test_productedit_form_name_label(self):
        ''' Test product name field '''
        form = ProductEditForm()
        self.assertTrue(form.fields['name'].label is None or form.fields['name'].label == 'Name')

class GetIDFormTest(TestCase):
    ''' Tests for GetIDForm '''
    def test_getID_form_ID_label(self):
        ''' Test ID field '''
        form = GetIDForm()
        self.assertTrue(form.fields['prod_id'].label is None or form.fields['prod_id'].label == 'ID (read only)')

class AddAddressFormTest(TestCase):
    ''' Tests for AddaddressForm '''
    def test_addaddress_form_nickname_label(self):
        ''' Test nickname field '''
        form = AddAddressForm()
        self.assertTrue(form.fields['nickname'].label is None or form.fields['nickname'].label == 'Nickname')

class EditAddressFormTest(TestCase):
    ''' Tests for EditAddressForm '''
    def test_editaddress_form_nickname_label(self):
        ''' Test nickname field '''
        form = EditAddressForm()
        self.assertTrue(form.fields['nickname'].label is None or form.fields['nickname'].label == 'Nickname')
