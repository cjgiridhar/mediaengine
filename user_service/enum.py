__author__ = 'cgiridhar'
from django.utils.translation import ugettext_lazy as _

guest_status_choices = (
    ('UNKNOWN', _('Unknown')),
    ('INVITED', _('Invitation Sent (only email known)')),
    ('IDENTIFIED', _('Identified (email and name known)')),
    ('VERIFIED', _('Verified e-mail address')),
    ('USER', _('Signed Up')),
)

user_billing_plan_choices = (
    ('FREE', _('Free')),
    ('PAY_PER_USE', _('Pay_Per_Use')),
    ('MONTHLY', _('Monthly')),
    ('QUARTERLY', _('Quarterly')),
    ('YEARLY', _('Yearly')),
)

transcode_error_codes = (
    (0, 'Success'),
    (1, 'Input_File_Not_Found'),
)