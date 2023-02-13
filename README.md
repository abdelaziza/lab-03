# Lab 3
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- Abdelaziz Abdelrhman
- team member 2

## Lab Question Answers

Question 1: Why are RESTful APIs scalable?

	Systems that implement representational state transfer application programming interface, REST APIs, can scale efficiently because REST optimizes client-server interactions. Statelessness removes server load because the server does not have to retain past client request information. Well-managed caching partially or completely eliminates some client-server interactions. All these features support scalability without causing communication bottlenecks that reduce performance.

Question 2: According to the definition of “resources” provided in the AWS article above,
What are the resources the mail server is providing to clients?

	The resources the mail server is providing to the clients is a unique path to file that contains the mail. In this instance, the resource is a unique id that is formed everytime new mail is generated.

Question 3: What is one common REST Method not used in our mail server? How could
we extend our mail server to use this method?

	One common REST method not used in the mail server is OAuth (this server uses an HTTP bearer authentication instead). To extend the mail server to use this method, we would have the server first request a password. Then we would hve it ask for an additional token to complete the authorization process. It can check the token at any time and also over time with a specific scope and longevity.

Question 4: Why are API keys used for many RESTful APIs? What purpose do they
serve? Make sure to cite any online resources you use to answer this question!

	API keys are unique identifiers that give developers a set of access rights for certain features or data of an application. For example, a developer may need a specific API key to access a database user interface or API server. Or an IoS or Android user may be looking to load a mobile app that draws data from Google Cloud. Keys are usually assigned by the web application owner and can be revoked at any time. Many uses of API keys are as follows: restricting anonymous traffic, authentication, and data analysis.
    Resource : https://blog.dreamfactory.com/api-keys-explained-what-they-are-and-how-to-use-them/ 
...
