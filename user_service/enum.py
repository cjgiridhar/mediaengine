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

progress_codes = (
        ('PENDING', _('Pending')),
        ('QUEUED', _('Queued')),
        ('INPROGRESS', _('InProgress')),
        ('COMPLETED', _('Completed')),
        ('CANCELLED', _('Cancelled')),
        ('FAILED', _('Failed')),
)

phase_codes = (
    ('DOWNLOAD', _('Download')), ('TRANSCODE', _('Transcode')), ('THUMBNAIL', _('Thumbnail')),
    ('SPRITE', _('Sprite')), ('UPLOAD', _('Upload')),
)

notification_codes = (
    ('EMAIL', _('Email')),
    ('SMS', _('Sms')),
)

error_levels = (('Info', 0), ('Warning', 1), ('Critical', 2))

job_priority_levels = (
    ('HIGH', _('High')),
    ('MEDIUM', _('Medium')),
    ('LOW', _('Low')),
)