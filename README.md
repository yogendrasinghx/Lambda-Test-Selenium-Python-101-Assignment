<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  
</head>
<body>
  <p>This Assignment demonstrates 3 test scenarios using Selenium and Python's pytest framework. The test scenarios involve automating interactions with the LambdaTest Selenium Playground.
</p>
  
  <h2>Getting Started</h2>
  
  <h3>Prerequisites</h3>
  <ul>
    <li>Python 3.x installed on your machine.</li>
    <li>Pip package manager.</li>
  </ul>
  
  <h3>Installation</h3>
  <ol>
    <li>Clone this repository to your local machine.</li>
    <li>Navigate to the project directory.</li>
    <li>Install the required dependencies by running the following command:</li>
  </ol>
  <pre><code>pip install -r requirements.txt</code></pre>
  
  <h3>Configuration</h3>
  <p>Before running the tests, update the following variables in the code:</p>
  <ul>
    <li>Replace &lt;username&gt; and &lt;access_key&gt; in <code>conftest.py</code> file with your actual LambdaTest credentials.</li>
  </ul>
  
  <h3>Running the Tests</h3>
  <p>To run the test scenarios, execute the following command in the project directory:</p>
  <pre><code>py.test --worker 2 -v -s</code></pre>
  <p>The tests will be parallelly executed the tests using configured browser and platform combinations.</p>
  
  <h3>Viewing Test Results</h3>
  <p>The test results, including any failures or errors, will be displayed in the console output.</p>
  <p>Additionally, the status of each test scenario will be set in LambdaTest. You can log in to your LambdaTest account and view the test session results there.</p>
  
</body>
</html>
