import unittest
from optparse import OptionParser
from auth.register_test import RegisterTest
from auth.login_test import LoginTest
from auth.forgot_password_test import ForgotPasswordTest
from task.manage_task import ManageTaskTest
from task.task_access import TaskAccessTest

import config

parser = OptionParser()
parser.add_option("-m", "--mobile", action="store_true", default=False, help="Run test on mobile")
parser.add_option("-d", "--dev", action="store_true", default=False, help="Run dev test")
parser.add_option("-c", "--chrome", action="store_true", default=False, help="Run in chrome")
parser.add_option("-f", "--firefox", action="store_true", default=False, help="Run in firefox")
parser.add_option("-s", "--safari", action="store_true", default=False, help="Run in safari")
parser.add_option("-w", "--wait", action="store_true", default=False, help="Use sleep")

(options, args) = parser.parse_args()

config.mobile_test = options.mobile

if config.mobile_test:
    print("Running test in mobile")

if options.chrome:
    config.driver = 'Chrome'
elif options.firefox:
    config.driver = 'Firefox'
elif options.safari:
    config.driver = 'Safari'

if options.wait:
    config.sleep_on_wait = True


if options.dev:
    # troubleshooting / dev
    devTestSuite = unittest.TestSuite([
        # unittest.TestLoader().loadTestsFromTestCase(ManageTaskTest),
        unittest.TestLoader().loadTestsFromTestCase(TaskAccessTest),
    ])

    unittest.TextTestRunner(verbosity=2).run(devTestSuite)
else:
    # we should add all test here
    sanityTestSuite = unittest.TestSuite([
        unittest.TestLoader().loadTestsFromTestCase(LoginTest),
        unittest.TestLoader().loadTestsFromTestCase(RegisterTest),
        unittest.TestLoader().loadTestsFromTestCase(ForgotPasswordTest),
        unittest.TestLoader().loadTestsFromTestCase(ManageTaskTest),
        unittest.TestLoader().loadTestsFromTestCase(TaskAccessTest),
    ])
    
    unittest.TextTestRunner(verbosity=2).run(sanityTestSuite)

