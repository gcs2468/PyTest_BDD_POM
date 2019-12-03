behave command ::

behave features/LoginFeature1.feature

To run tags ::

behave -v -t Regression features/LoginFeature.feature

Allure Reports ::

Download allure and setup allure manually then set bin dir path in environment variables ::

https://docs.qameta.io/allure/

install allure-behave library :: pip install allure-behave

Command to run tests(Generates xml reports) :: behave -t Regression features/LoginFeature.feature -f allure_behave.formatter:AllureFormatter -o ./reports

Run below command to generate Allure html reports :: allure serve ./reports


allure serve E:\Workspace\PyCharm\PyTest_BDD_POM\reports






