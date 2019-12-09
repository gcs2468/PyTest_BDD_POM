behave command ::

behave features/LoginFeature1.feature

To run tags ::

behave -t Regression features/LoginFeature.feature

Allure Reports ::

Download allure and setup allure manually then set bin dir path in environment variables ::

https://docs.qameta.io/allure/

install allure-behave library ::

pip install allure-behave

Command to run tests(Generates xml reports) ::

behave -t Regression features/LoginFeature.feature -f allure_behave.formatter:AllureFormatter -o ./Reports

Run below command to generate Allure html reports ::

allure serve ./Reports


Jenkins Setup ::

1. In Configure System -> Environment Variables add python home and scripts path.
2. In Manage Jenkins -> Global Tool Configure add Jdk home path.
3. In Manage Jenkins -> Global Tool Configure add git installation path.
4. In Manage Jenkins -> Manage Plugins install Allure report plugin.
5. In Manage Jenkins -> Global Tool Configure - at bottom add Allure Command Line installation path.
5. Create jenkins free style job.
6. In created job -> Configure -> Source Code Management -> add git repository url and credentials to get code from git repo.
7. In created job -> Configure -> Build Environment -> add "Execute windows batch command " and insert below commands in text box.
        set Path=%Python_Home%;%Path%
        rmdir /s /q Reports
        rmdir /s /q allure-report
        batchfiles/libs.bat
        behave -t Regression features/LoginFeature.feature -f allure_behave.formatter:AllureFormatter -o ./Reports
8. In created job -> Configure -> Post Build Actions -> add Reports path location (Reports)
9. In created job -> Configure -> Build Triggers -> Add schedule to run job automatically at fiven specified build time (H/15 * * * * => For every 15 minutes).















