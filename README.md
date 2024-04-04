# Just Order - Online Order System based on Cloud

- "Just Click" is a **SAAS model backend system** in which a user is supposed to upload an image of handwritten notes of vegetable items vs. quantity. After that using
  Amazon's Machine Learning-based service,   we will extract important information and check against the vegetable items database with the quantity. If all
  the items are matched, the full order email will be sent otherwise a partial order will be delivered. I have focused here mostly on the backend part to use
  different types of cloud services based on storage, network, serverless functions, computing, and other services.

# Beauty of this project 

- **Cloud Formation** - Just imagine, you're a newbie to Amazon and don't know how to push buttons to create resources but you know how to write code. Don't worry here is the solution.
  Cloud formation basically works on the concept of **Infrastructure as Code (IaC)** and it helps you model and set up your AWS resources so that you can spend less time managing
  those resources and more time focusing on your applications that run in AWS.

# Backend Architecture 

![image](https://github.com/HVMS/CloudProect/assets/38061955/eafbb9eb-de7d-4b47-bbfb-f9a285405478)

# Amazon Services Used

- **Storage**
  - Amazon Simple Storage Service S3 ( Object Storage )
  - Amazon DynamoDB ( NoSQL Data Storage )

- **Network**
  - Amazon API Gateway ( RESTFul Architecture APIs )
 
- **Compute**
  - AWS Lambda ( To execute shorter computation with less time )
  - AWS Step Function ( To execute workflow seamlessly and faster execution )
 
- **Others**
  - Amazon SNS (To Send an email to a group of users)
  - Amazon Textract ( TO extract image data - own algorithm implemented )
 
 

